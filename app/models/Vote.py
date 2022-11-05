from datetime import datetime
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property

class Vote(Base):
    __tablename__ = 'votes'
    id = Column(Integer, prrimary_key = True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('users.id'))
    vote_count = column_property(
  select([func.count(Vote.id)]).where(Vote.post_id == id)
)