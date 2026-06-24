from fastapi import FastAPI

from database import Base, engine
from routers import cart, orders, products, users

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-Commerce API",
    version="1.0.0",
)

app.include_router(users.router)
app.include_router(products.router)
app.include_router(cart.router)
app.include_router(orders.router)


@app.get("/")
def home():
    return {"message": "E-Commerce API Running"}
