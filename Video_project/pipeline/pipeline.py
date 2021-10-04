from Video_project.pipeline.steps.step import StepException

class Pipeline:
    def __init__(self,steps):
        self.steps = steps

    def run(self,inputs):
        data = None
        for step in self.steps:
            try:
                data = step.process(inputs)
            except StepException as e:
                print('Exception happened:',e)
                break