from Video_project.pipeline.steps.get_video_list import GetVideoList
from Video_project.pipeline.steps.step import StepException
from Video_project.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UC5YKivGUTTQmhSuaXbxfZSg'  # user video id


def main():
    inputs = {'channel_id': CHANNEL_ID}
    steps = [GetVideoList(),]
    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
