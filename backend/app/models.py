from sqlalchemy import Column, Integer, String, DateTime, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False,unique=True)
    phone = Column(Integer, nullable=False)
    gender = Column(String(7), nullable=False)
    dob = Column(DateTime, nullable=False)
    bio = Column(String(255), nullable=False)
    resume_path = Column(String(255), nullable=False)
    payment_id = Column(Integer, nullable=True)
    payment_status = Column(SmallInteger, default=0, nullable=False)

