import uuid
from pydantic import (
    BaseModel,
)

from .models import Playlist


class PlaylistCreateSchema(BaseModel):
    title: str
    user_id: str  # uuid.UUID
