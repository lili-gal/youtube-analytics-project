import datetime
import os
import isodate
from googleapiclient.discovery import build
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()


class PlayList:
    def __init__(self, playlist_id):
        self.__link = ''
        self.__total_duration = datetime.timedelta(0, 0, 0)
        self.datetime = timedelta
        self.playlist_id = playlist_id
        # self.video_ids = video_ids
        YT_API_KEY = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=YT_API_KEY)
        playlist = youtube.playlists().list(part='contentDetails,snippet', id=self.playlist_id).execute()['items'][0][
            'snippet']
        self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"
        self.title = playlist['title']

    @property
    def total_duration(self):
        YT_API_KEY = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=YT_API_KEY)
        playlist_videos = youtube.playlistItems().list(playlistId=self.playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        # print(video_ids)

        '''
        вывести длительности видеороликов из плейлиста
        docs: https://developers.google.com/youtube/v3/docs/videos/list
        '''
        video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)
                                               ).execute()
        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            self.__total_duration += duration
        return self.__total_duration

    def show_best_video(self):
        YT_API_KEY = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=YT_API_KEY)
        playlist_videos = youtube.playlistItems().list(playlistId=self.playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        # print(video_ids)
       
        video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)
                                               ).execute()
        for video in video_response['items']:
            likes = int(video['statistics']['likeCount'])
            max_likes = 0
            if likes > max_likes:
                self.__link = f"https://youtu.be/{video['id']}"
            else:
                break

        return self.__link
                
        
    