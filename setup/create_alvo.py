from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import Table, Column, Integer, String, DateTime, Float, Text, MetaData
from sqlalchemy.orm import declarative_base
import vars
db = "alvo"
url = f"postgresql://{vars.user}:{vars.password}@{vars.host}/{db}"
engine = create_engine(url)
base = declarative_base()

if not database_exists(engine.url):
    create_database(engine.url)

metadata = MetaData()

signal = Table(
    'signal', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False)
)

data = Table(
    'data', metadata,
    Column('signal_id', Integer, primary_key=True, nullable=False),
    Column('timestamp', DateTime, nullable=False),
    Column('value', Text, nullable=False)
)

metadata.create_all(engine)