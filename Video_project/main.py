from Video_project.pipeline.steps.get_video_list import GetVideoList
from Video_project.pipeline.steps.step import StepException
from Video_project.pipeline.pipeline import Pipeline
from Video_project.pipeline.steps.download_caption import DownloadCaptions
from Video_project.utils import Utils
from Video_project.pipeline.steps.preflight import Preflight
from Video_project.pipeline.steps.postflight import Postlight

CHANNEL_ID = 'UC5YKivGUTTQmhSuaXbxfZSg'  # user video id


def main():
    inputs = {'channel_id': CHANNEL_ID}
    steps = [Preflight(),GetVideoList(), DownloadCaptions(),Postlight()]
    utils = Utils
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
