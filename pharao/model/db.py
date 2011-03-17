from pharao.model import Base, DBSession
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime, PickleType, Boolean
from sqlalchemy.orm import relationship, backref
import datetime
import hashlib


class Page(Base):
    __tablename__ = 'pages'
    page_id = Column(Integer, primary_key=True)
    page_content = Column(String)
    

class PrincipalMembers(Base):
    __tablename__ = 'principalmembers'
    principalmembership_id = Column(Integer, primary_key=True)
    principal_id = Column(Integer, ForeignKey('principals.principal_id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))
    

class Principal(Base):
    __tablename__ = 'principals'
    def __init__(self, name):
        self.principal_name = name
    principal_id = Column(Integer, primary_key=True)
    
    principal_name = Column(String, unique=True)
    

class User(Base):
    __tablename__ = 'users'
    def __init__(self, username, password):
        self.username = username
        self.password = hashlib.sha1(password).hexdigest()
    user_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    principals = relationship(Principal, secondary=PrincipalMembers.__table__)
 
