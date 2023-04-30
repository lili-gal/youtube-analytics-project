import os
import json
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()


class Channel:
    """Класс для ютуб-канала"""
    # YT_API_KEY = os.getenv('YT_API_KEY')
    # youtube = build('youtube', 'v3', developerKey=YT_API_KEY)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        # self.channel_info = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = ''
        self.url = ''
        self.video_count = 0

        YT_API_KEY = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=YT_API_KEY)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        if channel['items']:
            channel = channel['items'][0]
            self.title = channel['snippet']['title']
            self.url = f"https://www.youtube.com/channel/{self.channel_id}"
            self.video_count = channel['statistics']['videoCount']

    @staticmethod
    def get_service():
        """Возвращает объект для работы с API."""
        YT_API_KEY = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=YT_API_KEY)
        return youtube

    def to_json(self, file_name: str) -> None:
        """Сохраняет данные о канале в JSON-файл."""
        data = {
            'channel_id': self.channel_id,
            'title': self.title,
            'url': self.url,
            'video_count': self.video_count,

        }
        with open(file_name, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def print_info(self):
        """Выводит информацию о канале"""
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(channel)
        # print(json.dumps(self.channel_info, indent=2, ensure_ascii=False))
