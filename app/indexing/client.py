from algoliasearch.search_client import SearchClient

from app import config

settings = config.get_settings()
ALGOLIA_APP_ID = settings.algolia_app_id
ALGOLIA_API_KEY = settings.algolia_api_key
ALGOLIA_INDEX_NAME = settings.algolia_index_name


def get_index(name=ALGOLIA_INDEX_NAME):
    client = SearchClient.create(ALGOLIA_APP_ID, ALGOLIA_API_KEY, ALGOLIA_INDEX_NAME)
    index = client.init_index(name)
    return index


def update_index():
    index = get_index()
    pass
    return 


def search_index(query):
    index = get_index()
    return index.search(query)