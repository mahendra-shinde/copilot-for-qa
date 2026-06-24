from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/")
def create_order(
    order: schemas.OrderCreate,
    db: Session = Depends(get_db),
):
    return crud.create_order(db, order)
