from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    dbid = Column(Integer, primary_key=True)
    name = Column(String(50))
    surname = Column(String(50))
    age = Column(Integer)


if __name__ == "__main__":
    engine = create_engine("mysql+pymysql://u12:u12@localhost/u12", echo=True)
    Base.metadata.create_all(engine)

