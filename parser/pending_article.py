from sqlalchemy import Column, Integer, Sequence, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PendingArticle(Base):
    """Persisted article awaiting user approval"""
    __tablename__ = "pending_articles"

    id = Column(Integer, Sequence("pending_article_id_seq"), primary_key=True)
    url = Column(Text)
    title = Column(Text)
    snippet = Column(Text)
