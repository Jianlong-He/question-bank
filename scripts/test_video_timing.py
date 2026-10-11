"""Integration regression: a long final still must last through its narration."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from generate_sample_videos import encode_static_scenes,FPS

class TimingTests(unittest.TestCase):
    def test_sparse_stills_keep_last_hold_and_scene_boundary(self):
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder)
            for name,color in [('red',(255,0,0)),('blue',(0,0,255))]:
                (p/f'{name}.ppm').write_bytes(b'P6\n32 18\n255\n'+bytes(color)*(32*18))
            sequence=p/'scenes.txt'
            sequence.write_text("file 'red.ppm'\nduration 1\nfile 'blue.ppm'\nduration 4\nfile 'blue.ppm'\n")
            output=p/'video.mp4';encode_static_scenes(sequence,5,output)
            d=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-of','json',str(output)]))['streams'][0]
            self.assertEqual(int(d['nb_frames']),5*FPS)
            self.assertAlmostEqual(float(d['duration']),5,places=3)
            raw=subprocess.check_output(['ffmpeg','-v','error','-i',str(output),'-vf','scale=1:1','-pix_fmt','rgb24','-f','rawvideo','-'])
            colors=[tuple(raw[i:i+3]) for i in range(0,len(raw),3)]
            self.assertEqual(len(colors),5*FPS)
            self.assertGreater(colors[FPS-1][0],240)
            self.assertGreater(colors[FPS][2],240)
            self.assertGreater(colors[-1][2],240)

if __name__=='__main__':unittest.main()
