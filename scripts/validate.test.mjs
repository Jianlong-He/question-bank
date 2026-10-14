import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, mkdirSync, writeFileSync, copyFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';

const validator = join(dirname(fileURLToPath(import.meta.url)), 'validate.mjs');
const source = 'worksheets/Grade 1/G1Unit 1/G1U1W1.csv';
const image = 'worksheet-images/Grade 1/G1Unit 1/G1U1W1/WS-G1U1W1Q1I1.png';
const video = 'Grade 1/Unit 1/count.mp4';

function runFixture({ videoCell = video, imageCell = image, answer = '2',
  imageSource = source, asset = `videos/${video}`, missingManifest = false,
  curriculumSource = source } = {}) {
  const root = mkdtempSync(join(tmpdir(), 'question-bank-validator-'));
  const write = (file, text) => {
    mkdirSync(dirname(join(root, file)), { recursive: true });
    writeFileSync(join(root, file), text);
  };
  const json = (file, value) => write(file, JSON.stringify(value));
  try {
    write('scripts/validate.mjs', '');
    copyFileSync(validator, join(root, 'scripts/validate.mjs'));
    const rows = [['Question ID', 'Question Choices', 'Question Answers', 'image', 'video'],
      ['1', 'What is 1 + 1?', answer, imageCell, videoCell]];
    write(source, rows.map(row => row.map(v => `"${v.replaceAll('"', '""')}"`).join(',')).join('\n'));
    json('data/curriculum.json', [{ title: 'Course Contents' },
      { title: 'Worksheets', submenu: [{ title: 'Worksheet 1', url: `?file=${curriculumSource}` }] },
      { title: 'Games' }]);
    json('unit-tests/catalog/catalog.json', []);
    json('image-question-correspondence.json', { images: [{ source_csv: imageSource, image_file: `images/${image}` }] });
    if (!missingManifest) json('worksheet-video-correspondence.json', {
      worksheets: { [source]: {} }, videos: { count: { assets: { mp4: asset, captions: null } } },
    });
    // Deliberately no images/ or videos/ directories: CI has no local media.
    const result = spawnSync(process.execPath, [join(root, 'scripts/validate.mjs')], { encoding: 'utf8' });
    assert.ifError(result.error);
    return { status: result.status, output: result.stdout + result.stderr };
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
}

test('hosted media and root correspondence files pass without local assets', () => {
  const result = runFixture();
  assert.equal(result.status, 0, result.output);
  assert.match(result.output, /0 error\(s\), 0 warning\(s\)/);
});

test('blank, bar-separated, and JSON media cells are supported', () => {
  for (const videoCell of ['', `${video} | Grade 2/Unit 1/add.mp4`, JSON.stringify([video, 'Grade 2/Unit 1/add.mp4'])]) {
    const result = runFixture({ videoCell, imageCell: JSON.stringify([image]) });
    assert.equal(result.status, 0, result.output);
  }
});

test('invalid individual media paths still fail, including second video entries', () => {
  for (const path of ['../escape.mp4', '/absolute.mp4', 'videos/count.mp4',
    'https://example.com/count.mp4', 'a\\b.mp4', 'a//b.mp4', 'a/./b.mp4', '']) {
    const result = runFixture({ videoCell: `${video} | ${path}` });
    assert.equal(result.status, 1, result.output);
    assert.match(result.output, /invalid media path/);
  }
});

test('malformed JSON and non-string entries fail', () => {
  for (const videoCell of ['[broken', '[]', '[null]', '[42]']) {
    const result = runFixture({ videoCell });
    assert.equal(result.status, 1, result.output);
    assert.match(result.output, /invalid JSON|nonempty path array|invalid media path/);
  }
});

test('correspondence source CSVs and media path prefixes are checked', () => {
  for (const options of [{ imageSource: 'worksheets/missing.csv' }, { asset: '../escape.mp4' }, { asset: video }]) {
    const result = runFixture(options);
    assert.equal(result.status, 1, result.output);
    assert.match(result.output, /missing referenced source CSV|invalid media path/);
  }
});

test('missing correspondence, broken curriculum links, and empty answers still fail', () => {
  for (const options of [{ missingManifest: true }, { curriculumSource: 'worksheets/missing.csv' }, { answer: '' }]) {
    const result = runFixture(options);
    assert.equal(result.status, 1, result.output);
    assert.match(result.output, /ENOENT|not in this repo|empty Question Answers/);
  }
});
