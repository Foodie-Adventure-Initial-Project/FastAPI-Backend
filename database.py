import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
#As best practice we want to have a diiferent database for testing and production
#We will use the environment variable DATABASE_URL to determine which database to use
load_dotenv()
ENV = os.getenv("ENV", default="development")
if ENV == "development":
    DATABASE_URL = os.getenv("DATABASE_URL")    
else:
    DATABASE_URL = os.getenv("DATABASE_URL_TEST")

enginer = create_engine(DATABASE_URL, echo=True)
