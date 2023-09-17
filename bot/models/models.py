from sqlalchemy import Column, BigInteger, String, Boolean
from models import metadata, engine, base
from models.modelclass import Model

class User(base, Model):
    __tablename__ = 'client'

    id = Column(BigInteger, primary_key=True)
    tg_id = Column(BigInteger)
    username = Column(String)
    is_admin = Column(Boolean)

    def __init__(self, tg_id: int, username: str):
        self.tg_id = tg_id
        self.username = username
        self.is_admin = False

    def __repr__(self):
        return f'{self.id}. @{self.username} approved={self.is_approved} declined={self.is_declined} admin={self.is_admin}'

metadata.create_all(engine)