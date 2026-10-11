"""Preserve obsolete draft IDs while reusing verified media for inspected questions."""
import re


def validate_reuse(doc):
    for vid,v in doc['videos'].items():
        targets=v.get('reuse_video_ids')
        if targets is None:continue
        assert v['production_status']=='retired' and targets and len(targets)==len(set(targets)),vid
        assert vid not in targets,vid
        for target in targets:
            assert target in doc['videos'],(vid,target)
            state=doc['videos'][target]['production_status']
            assert state=='rendered' or (state in {'needs_revision','in_progress'} and doc['videos'][target]['assets']['mp4']),(vid,target)
            assert not doc['videos'][target].get('reuse_video_ids'),(vid,target)
    for file,w in doc['worksheets'].items():
        for qid,p in w['problems'].items():
            for link in p['video_links']:
                assert doc['videos'][link['video_id']]['production_status']!='retired',(file,qid,link['video_id'])


def merge_reviewed_duplicate(doc,old_id,ref_targets):
    """ref_targets explicitly enumerates ALL inspected references; no inferred merges."""
    old=doc['videos'][old_id]
    assert old['production_status']=='planned',old_id
    assert not old['youtube']['video_id'] and all(v is None for v in old['assets'].values()),old_id
    actual={(f,q) for f,w in doc['worksheets'].items() for q,p in w['problems'].items()
            if any(l['video_id']==old_id for l in p['video_links'])}
    assert actual and actual==set(ref_targets),(old_id,'Review every linked question before merging',actual)
    for ref,target in ref_targets.items():
        assert target!=old_id and doc['videos'][target]['production_status']=='rendered',target
        p=doc['worksheets'][ref[0]]['problems'][ref[1]]
        assert len(p['video_links'])==1 and not p['requires_source_visual'],ref
    # Validate the whole change before any mutation, preserving uploaded/media-bearing IDs.
    targets=sorted(set(ref_targets.values()))
    for (file,qid),target in ref_targets.items():
        p=doc['worksheets'][file]['problems'][qid]
        p['video_links'][0]['video_id']=target
        p.update(mapping_method='manual',mapping_status='reviewed',mapping_rule='verified-video-reuse-1',
                 notes=f'Inspected duplicate teaching method: uses the verified analogous example {target}. Original draft video ID {old_id} is retained as a reuse record.')
    old.update(production_status='retired',reuse_video_ids=targets,
               notes='Duplicate draft method, fully covered by verified shared videos. No separate export or upload is needed. Original ID retained for lookup.')
    old['planning']['review_status']='reviewed'


def append_upload_row(content,vid,title):
    prefix,separator,footer=content.partition('\n## Shared video reuse\n')
    return prefix.rstrip()+f'\n| {title} | {vid}.mp4 |  |\n'+(separator+footer if separator else '')


def update_reuse_checklist(content,doc):
    retired={vid:v for vid,v in doc['videos'].items() if v.get('reuse_video_ids')}
    # Rebuild the explanatory footer idempotently; active upload cells stay byte-for-byte.
    content=content.split('\n## Shared video reuse\n')[0]
    lines=[]
    for line in content.splitlines():
        match=re.search(r'\| ([a-z0-9-]+)\.mp4 \|',line)
        if match and match[1] in retired:
            assert not line.split('|')[3].strip(),'Cannot remove a row with a user-entered YouTube ID'
            continue
        lines.append(line)
    count=sum(v['production_status']!='retired' for v in doc['videos'].values())
    text='\n'.join(lines).rstrip()+'\n'
    text=re.sub(r'All [\d,]+ videos in the current plan\.',f'All {count:,} videos in the current plan.',text)
    if retired:
        text+='\n## Shared video reuse\n\nThese retained draft IDs reuse completed videos. No separate file or upload is needed. Enter the YouTube ID on the shared video’s row above.\n\n'
        for vid,v in sorted(retired.items()):
            text+=f'- `{vid}` → '+', '.join(f'`{t}.mp4`' for t in v['reuse_video_ids'])+'\n'
    return text
