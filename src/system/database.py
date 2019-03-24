from typing import List, Type

from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session


Base = declarative_base()


class Database:

    _instance = None
    _engine_info = {
        "drivername": "mysql",
        "database": "value_at_travel",
        "username": "root",
        "password": "",
        "port": 3307
    }

    def __init__(self):
        self.engine = None
        self.tables = {}
        self._construct()
        self.session = sessionmaker(bind=self.engine)

        Base.metadata.create_all(self.engine)

    def _construct(self):
        from system.models.user import User
        self.engine = create_engine(URL(**self._engine_info))
        self._construct_tables([User])

    def _construct_tables(self, models: List[Type[Base]]):
        meta_data = MetaData(self.engine)
        for model in models:
            Table(model, meta_data)

    def get_session(self) -> Session:
        return self.session()

    def commit(self, updates: any):
        session = self.get_session()

        if isinstance(updates, list):
            [session.add(update) for update in updates]
        else:
            session.add(updates)

        session.commit()
        session.close()

    @staticmethod
    def get_instance() -> 'Database':
        if Database._instance is None:
            Database._instance = Database()

        return Database._instance


