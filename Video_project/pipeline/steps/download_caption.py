from Video_project.pipeline.steps.step import Step, StepException
from youtube_transcript_api import YouTubeTranscriptApi
import time
import json

class DownloadCaptions(Step):

    def process(self, data, inputs, utils):
        start = time.perf_counter()
        threads = []
        for url in data:
            print(f'Downloading caption for{url.id}')
            if utils.caption_file_exists(url):
                print(f'Caption file existed for video id:{url.id}')
                continue

            # threads.append(Thread(target=self.get_caption, args=(url,)))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        end = time.perf_counter()
        print(f'Captions downloading elapsed time:{round(end - start, 2)} secs.')

        return data

    def get_caption(self, url):
        try:
            captions = YouTubeTranscriptApi.get_transcript(url.caption_filepath)
            captions_l = list(json.dumps(i) for i in captions)
            with open(url.caption_filepath, 'w', encoding='utf-8') as fp:
                for i in captions_l:
                    fp.write(i + '\n')
        except:
            print(f'Subtitle is disabled for video id:{url.id}')

