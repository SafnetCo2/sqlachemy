from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine =create_engine('sqlite:///sqlalchemy.db')
Base=declarative_base()

class Album(Base):
    __tablename__="albums"
    
    id=Column(Integer, primary_key=True)
    email=Column(String)
    artist=Column(String)
Base.metadata.create_all(engine)

#add records
#import sessionmaker,
Session=sessionmaker(bind=engine)
session=Session()

album1=Album(title="Thriller",artist="Mj")
session.add(album1)
session.commit()