from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class ProductCreate(BaseModel):
    name: str
    category: str
    price: float
    quantity: int


class CartCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int


class OrderCreate(BaseModel):
    user_id: int
    total_amount: float
