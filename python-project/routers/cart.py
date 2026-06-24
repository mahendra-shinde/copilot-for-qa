from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db

router = APIRouter(prefix="/cart", tags=["Cart"])


@router.post("/")
def add_cart_item(
    cart_item: schemas.CartCreate,
    db: Session = Depends(get_db),
):
    return crud.add_to_cart(db, cart_item)
