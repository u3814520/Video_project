from Video_project.pipeline.steps import GetVideoList
from Video_project.pipeline.steps import StepException

CHANNEL_ID='UC5YKivGUTTQmhSuaXbxfZSg'  # user video id

steps=[GetVideoList(),]

for step in steps:
    try:
        step.process()
    except StepException as e:
        print('Exception happened:'e)
        break
