from sqlalchemy.orm import Session

import models
import schemas


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        name=user.name,
        email=user.email,
        password=user.password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_products(db: Session):
    return db.query(models.Product).all()


def add_to_cart(db: Session, cart_item: schemas.CartCreate):
    item = models.CartItem(**cart_item.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(
        user_id=order.user_id,
        total_amount=order.total_amount,
        status="CREATED",
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
