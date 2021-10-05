from pytube import YouTube
from Video_project.pipeline.steps.step import Step, StepException

class DownloadCaptions(Step):
    def process(self, data, inputs,utils):  # 下載字幕
        for url in data:
            source = YouTube(url)
            en_caption = source.captions.get_by_language_code('a.en')  # a代表自動產生
            en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            print(en_caption_convert_to_srt)

            # save the caption to a file named Output.txt
            text_file = open(utils.get_video_id(url), "w")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
            break
