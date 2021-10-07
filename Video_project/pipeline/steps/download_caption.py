from Video_project.pipeline.steps.step import Step, StepException
from youtube_transcript_api import YouTubeTranscriptApi
import time
import json

class DownloadCaptions(Step):

    def process(self, data, inputs, utils):
        start = time.perf_counter()
        threads = []
        for yt in data:
            print('Downloading caption for', yt.id)
            if utils.caption_file_exist(yt):
                print('Caption file existed for video id:', yt.id)
                continue

            # threads.append(Thread(target=self.get_caption, args=(yt,)))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        end = time.perf_counter()
        print(f'Captions downloading elapsed time:{round(end - start, 2)} secs.')

        return data

    def get_caption(self, yt):
        try:
            captions = YouTubeTranscriptApi.get_transcript(yt.id)
            captions_l = list(json.dumps(i) for i in captions)
            with open(yt.caption_filepath, 'w', encoding='utf-8') as fp:
                for i in captions_l:
                    fp.write(i + '\n')
        except:
            print('Subtitle is disabled for video id:', yt.id)

