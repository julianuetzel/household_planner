import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from ..database import Base

class Note(Base):
    __tablename__ = 'note'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    text = Column(String)


