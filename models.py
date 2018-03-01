from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

import config

Base = declarative_base()
url_config = {
    'drivername': config.DB_DRIVER,
    'host': config.DB_HOST,
    'port': config.DB_PORT,
    'username': config.DB_USER,
    'password': config.DB_PASSWORD,
    'database': config.DB_NAME
}
connection_string = str(URL(**url_config))
engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)
session = Session()


class ValueList(Base):
    __tablename__ = 'value_list'
    id = Column(Integer, primary_key=True)
    value = Column(String(255))


if __name__ == '__main__':
    Base.metadata.create_all(engine)
