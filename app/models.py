# models.py
from sqlalchemy import Column, Integer, String, DateTime, Float, Text
from sqlalchemy.orm import declarative_base

Base_fonte = declarative_base()
Base_alvo = declarative_base()

class data_fonte(Base_fonte):
    __tablename__ = 'data'
    timestamp = Column(DateTime, primary_key=True, index=True)
    wind_speed = Column(Float, index=True)
    power = Column(Float, index=True)
    ambient_temperature = Column(Float, index=True)

class signal(Base_alvo):
    __tablename__ = 'signal'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class data_alvo(Base_alvo):
    __tablename__ = 'data'
    signal_id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, index=True)
    value = Column(Text, index=True)
