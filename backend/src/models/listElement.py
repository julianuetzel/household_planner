import uuid
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from ..database import Base

class ListElement(Base):
    __tablename__ = 'list'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
    items = relationship('Item')

class Item(Base):
    __tablename__ = 'item'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    text = Column(String)
    status = Column(Integer, default=0)
    list_id = Column(UUID(as_uuid=True), ForeignKey('list.id'))




