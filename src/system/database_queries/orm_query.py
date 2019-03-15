from sqlalchemy import Column, String, Integer, DATETIME, ForeignKey
from base import Base, session_factory
session = session_factory()

class UserDefinition(Base):
    __tablename__ = 'user_definition'
    id = Column(Integer, primary_key=True)
    user_definition_id = Column(Integer)
    user_definition = Column(String)

    def __init__(self, user_definition_id, user_definition):
        self.user_definition_id = user_definition_id
        self.user_definition = user_definition

    def get_user_definition(self):
        user_def = session.query(UserDefinition).all()
        for user_types in user_def:
            print("Type: ", user_types.user_definition)


class UserInfo(Base):
    __tablename__ = 'user_info'
    id = Column(Integer, primary_key=True)
    email_adress = Column(String)
    username = Column(String)
    password = Column(String)
    timestamp = Column(DATETIME)
    user_definition_id = Column(Integer, ForeignKey('user_definition.id'))

    def __init__(self):
        pass

    @staticmethod
    def get_user_info(username: str):
        user_info = session.query(UserInfo).filter_by(username=username).all()
        for user_types in user_info:
            print("Mail: ", user_types.email_adress)
            print("Username: ", user_types.username)
            print("Password: ", user_types.password)
            print("Password: ", user_types.user_definition_id)
    @staticmethod
    def register_user(email_adress: str, username: str, password: str, user_definition_id: int):
        user = UserInfo(email_adress=email_adress, username=username, password=password, user_definition_id=user_definition_id)
        session.add(user)
        session.commit()
        print("User registered")

#user_info = UserInfo()
UserInfo.get_user_info("ns")
#UserInfo.register_user("aapie@slinger.nl", "aapie", "banaan123", 1)

