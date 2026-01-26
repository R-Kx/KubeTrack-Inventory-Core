from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session
from src.database import Base, engine, ItemDB, get_db
import os

# ბაზის ცხრილების შექმნა გაშვებისას (Production-ში ამას Migration tool აკეთებს, მაგრამ ლაბისთვის საკმარისია)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Inventory API with DB")


# Pydantic Model (მონაცემების ვალიდაცია Request/Response-ისთვის)
class ItemSchema(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

    class Config:
        from_attributes = True


class ItemResponse(ItemSchema):
    id: int


@app.get("/")
def read_root():
    return {"status": "active", "db_type": "postgresql"}


@app.get("/items", response_model=List[ItemResponse])
def get_items(db: Session = Depends(get_db)):
    """Get all items from DB"""
    items = db.query(ItemDB).all()
    return items


@app.post("/items", response_model=ItemResponse, status_code=201)
def create_item(item: ItemSchema, db: Session = Depends(get_db)):
    """Create new item in DB"""
    # ვქმნით DB ობიექტს
    new_item = ItemDB(name=item.name, price=item.price, is_offer=item.is_offer)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


@app.get("/health")
def health_check():
    return {"status": "healthy"}
