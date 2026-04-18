import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#accede a la info del .env
load_dotenv()

DATABASE_URL = os.getenv("DB_URL")
print(DATABASE_URL)

engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Base = declarative_base()

print("Connected to DB OK")

from db import models  # 👈 esto hace que cargue User

Base.metadata.create_all(bind=engine)