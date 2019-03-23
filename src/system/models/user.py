from flask_login import UserMixin
from sqlalchemy import Integer, String, DateTime, func, Column, Boolean

from system.database import Base


class User(Base, UserMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    date_added = Column(DateTime, default=func.now())
    date_changed = Column(DateTime, default=func.now(), onupdate=func.now())
    authenticated = Column(Boolean, default=True)

    def get_id(self):
        return self.id

    @property
    def is_authenticated(self):
        return self.authenticated



