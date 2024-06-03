import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
path = os.path.abspath("../setup/")
sys.path.append(path)
import vars
DATABASE_URL_FONTE = f"postgresql://{vars.user}:{vars.password}@{vars.host}:5432/fonte"
DATABASE_URL_ALVO = f"postgresql://{vars.user}:{vars.password}@{vars.host}:5432/alvo"

engine_fonte = create_engine(DATABASE_URL_FONTE)
engine_alvo = create_engine(DATABASE_URL_ALVO)

SessionLocalFonte = sessionmaker(autocommit=False, autoflush=False, bind=engine_fonte)
SessionLocalAlvo = sessionmaker(autocommit=False, autoflush=False, bind=engine_alvo)

def get_db_fonte():
    db = SessionLocalFonte()
    try:
        yield db
    finally:
        db.close()

def get_db_alvo():
    db = SessionLocalAlvo()
    try:
        yield db
    finally:
        db.close()
