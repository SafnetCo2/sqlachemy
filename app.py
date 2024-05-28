from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create engine and base
engine = create_engine('sqlite:///sqlalchemy.db')
Base = declarative_base()

# Define Album class
class Album(Base):
    __tablename__ = "albums"
    
    id = Column(Integer, primary_key=True)
    title = Column(String)  # Define title column
    artist = Column(String)

# Create tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add records
album1 = Album(title="Thriller", artist="Mj")


# Add and commit records to the session
session.add(album1)
#session.add_all([album2, album3, album4])
session.commit()
