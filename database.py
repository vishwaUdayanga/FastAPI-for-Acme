from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = "postgresql://default:3fncgklswo1K@ep-tiny-block-a42howkm-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require"

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
