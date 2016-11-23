from sqlalchemy import Column, Integer, Sequence, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PendingArticle(Base):
    """Persisted article awaiting user approval"""
    __tablename__ = "pending_articles"

    url = Column(Text, primary_key=True)
    title = Column(Text)
    snippet = Column(Text)

    def __repr__(self):
        return """
        PendingArticle -- url: {url}, title: {title}, snippet: {snippet}
        """.format(**self.__dict__)
