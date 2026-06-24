from database import SessionLocal
import models


db = SessionLocal()

products = [
    models.Product(
        name="Laptop",
        category="Electronics",
        price=65000,
        quantity=10,
    ),
    models.Product(
        name="Phone",
        category="Electronics",
        price=30000,
        quantity=15,
    ),
    models.Product(
        name="Shoes",
        category="Fashion",
        price=2500,
        quantity=50,
    ),
]

for product in products:
    db.add(product)

db.commit()
db.close()
print("Sample data inserted")
