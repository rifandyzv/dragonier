from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# DATABASE_URL = 'postgresql://postgres:123@localhost:5432/dragonier'

DATABASE_URL = 'postgresql://xpjfchbo:urdE0vW2Q8Q9iVYuX6-DGmundndpKKBc@rosie.db.elephantsql.com/xpjfchbo'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try :
        yield db
    except :
        db.close()                          