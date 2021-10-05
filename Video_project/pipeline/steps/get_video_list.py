import urllib.request
import json
from Video_project.settings import API_KEY as KEY
from Video_project.pipeline.steps.step import Step


class GetVideoList(Step):
    def process(self,data,inputs,utils):
        channel_id= inputs['channel_id']
        api_key = KEY
        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
        first_url = base_search_url+f'key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=25'
        # print(first_url)
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
        print(video_links)
        return video_links

