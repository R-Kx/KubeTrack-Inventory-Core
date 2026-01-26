from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# ვიღებთ URL-ს გარემოდან, ან ვიყენებთ default-ს (ლოკალური ტესტირებისთვის)
# Docker-ში და K8s-ში ჩვენ ამ ცვლადს გარედან მივაწვდით
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://postgres:password@localhost:5432/inventory_db"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# DB Model (ცხრილის სტრუქტურა)
class ItemDB(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    is_offer = Column(Boolean, default=False)


# Helper function ბაზის სესიის მისაღებად
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
