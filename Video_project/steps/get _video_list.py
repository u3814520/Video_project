import urllib.request
import json
from Video_project.settings import API_KEY as KEY
from Video_project.steps.step import Step , StepException

class GetVideoList(Step):
    def process(self,inputs):
        self.get_all_video_in_channe()
        channel_id= inputs['channel_id']
        api_key = KEY
        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
        first_url = base_search_url+f'key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=25'
        video_links = []
        url = first_url
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)
            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])
            try:
                next_page_token = resp['nextPageToken']
                url = first_url + f'&pageToken={next_page_token}'
            except KeyError:
                break
        return video_links

    video_list=get_all_video_in_channel(CHANNEL_ID)
