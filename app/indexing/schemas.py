import uuid
import json
from pydantic import BaseModel, Field , validator, root_validator
from typing import Optional


class VideoIndexSchema(BaseModel):
    objectID: str = Field(alias='host_id')
    objectType: str = "Video"
    title: Optional[str]
    path: str = Field(alias='host_id')

    @validator("path")
    def set_path(cls, v, values, **kwargs):
        host_id = v
        return f"/videos/{host_id}"


class PlaylistIndexSchema(BaseModel):
    objectID: uuid.UUID = Field(alias='db_id')
    objectType: str = "Playlist"
    title: Optional[str]
    path: str = Field(default='/')

    #     @validator("path")
    #     def set_path(cls, v, values, **kwargs):
    #         db_id = v
    #         return f"/playlists/{db_id}"

    @root_validator
    def set_default(cls, values):
        objectID = values.get('objectID')
        values['objectID'] = str(objectID)
        values['path'] = f"/playlist/{objectID}"
        return values

# video_q = [dict(x) for x in Video.objects.all()]
# videos_dataset = [VideoIndexSchema(**x).dict() for x in video_q]
#
# playlist_q = [dict(x) for x in Playlist.objects.all()]
# playlists_dataset = [PlaylistIndexSchema(**x).dict() for x in playlist_q]
#
# dataset = playlists_dataset + videos_dataset