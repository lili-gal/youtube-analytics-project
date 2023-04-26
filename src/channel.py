import os
import json
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()


class Channel:
    """Класс для ютуб-канала"""
    YT_API_KEY = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=YT_API_KEY)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel_info = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

    def print_info(self):
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(self.channel_info, indent=2, ensure_ascii=False))



