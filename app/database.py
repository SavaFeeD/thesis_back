from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import dotenv_values


config = {**dotenv_values(".env")}

SQLALCHEMY_DATABASE_URL = f'postgresql://{config["DB_USERNAME"]}:{config["DB_PASSWORD"]}@{config["DB_HOST"]}/{config["DB_DATABASE"]}'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
