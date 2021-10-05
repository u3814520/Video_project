import os
from Video_project.settings import CAPTIONS_DIR,VIDEOS_DIR,DOWNLOADS_DIR

class Utils:
    def __init__(self):
        pass
    def create_dir(self):
        os.makedirs(DOWNLOADS_DIR,exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
    @staticmethod
    def get_video_id(url):
        return  url.split("watch?v=")[-1]

    def get_caption_path(self,url):
        return os.path.join(CAPTIONS_DIR,self.get_video_id(url)+'.txt')