from dotenv import dotenv_values

from fastapi import HTTPException, status
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

config = dotenv_values(".env")
SQLALCHEMY_DATABASE_URL = config.get('DATABASE_URL')
engine = create_engine(SQLALCHEMY_DATABASE_URL)
DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = DBSession()
    try:
        yield db
    except SQLAlchemyError as err_sql:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err_sql))
    finally:
        db.close()


