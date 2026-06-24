from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/")
def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db),
):
    return crud.create_product(db, product)


@router.get("/")
def get_all_products(db: Session = Depends(get_db)):
    return crud.get_products(db)
