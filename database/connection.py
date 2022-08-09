from os import getenv

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine(getenv('DATABASE_URL_SYNC'))

SessionLocal = sessionmaker(bind=engine)

