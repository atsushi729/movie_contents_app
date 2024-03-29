from algoliasearch.search_client import SearchClient

from app import config

from app.playlists.models import Playlist
from app.videos.models import Video

from .schemas import (
    PlaylistIndexSchema,
    VideoIndexSchema,
)

settings = config.get_settings()
ALGOLIA_APP_ID = settings.algolia_app_id
ALGOLIA_API_KEY = settings.algolia_api_key
ALGOLIA_INDEX_NAME = settings.algolia_index_name


def get_index(name=ALGOLIA_INDEX_NAME):
    client = SearchClient.create(
        ALGOLIA_APP_ID,
        ALGOLIA_API_KEY
    )
    index = client.init_index(name)
    return index


def get_dataset():
    playlist_q = [dict(x) for x in Playlist.objects.all()]
    playlists_dataset = [PlaylistIndexSchema(**x).dict() for x in playlist_q]
    video_q = [dict(x) for x in Video.objects.all()]
    videos_dataset = [VideoIndexSchema(**x).dict() for x in video_q]
    dataset = playlists_dataset + videos_dataset
    return dataset


def update_index():
    index = get_index()
    dataset = get_dataset()
    idx_resp = index.save_objects(dataset).wait()
    try:
        count = len(list(idx_resp)[0]['objectIDs'])
    except:
        count = None
    return count


def search_index(query):
    index = get_index()
    return index.search(query)
