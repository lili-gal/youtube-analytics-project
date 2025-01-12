import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
load_dotenv()


class Video:
    '''Реализуeт инициализацию реальными данными экземпляра класса Video'''
    def __init__(self, video_id):
        self.video_id = video_id
        YT_API_KEY = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=YT_API_KEY)
        try:
            video = youtube.videos().list(part='snippet,statistics', id=self.video_id).execute()
            self.title = video[0]['snippet']['title']
            self.url = f"https://www.youtube.com/watch?v={self.video_id}"
            self.views = int(
                youtube.videos().list(part='statistics', id=self.video_id).execute()['items'][0]['statistics'][
                    'viewCount'])
            self.like_count = int(
                youtube.videos().list(part='statistics', id=self.video_id).execute()['items'][0]['statistics'][
                    'likeCount'])
        except KeyError as e:
            print('Видео не найдено')
            self.title = None
            self.like_count = None
            self.url = None
            self.views = None

    def __str__(self):
        return self.title
        

class PLVideo(Video):
    '''PLVideo инициализируется 'id видео' и 'id плейлиста' '''
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        YT_API_KEY = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=YT_API_KEY)
        video = youtube.videos().list(part='snippet, statistics', id=self.video_id).execute()['items'][0]['snippet']
        self.title = video['title']
        self.url = f"https://www.youtube.com/watch?v={self.video_id}"
        self.views = int(
            youtube.videos().list(part='statistics', id=self.video_id).execute()['items'][0]['statistics']['viewCount'])
        self.likes = int(
            youtube.videos().list(part='statistics', id=self.video_id).execute()['items'][0]['statistics']['likeCount'])
        self.playlist_id = playlist_id
        # like_count: int = youtube.videos().list['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.title
