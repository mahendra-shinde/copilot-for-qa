# Sample E-Commerce Application in Python

This FastAPI project is designed for a GitHub Copilot testing workshop. It includes user, product, cart, and order APIs backed by SQLite and SQLAlchemy.

## Technology Stack

- Python 3.14
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- Pytest
- Swagger/OpenAPI

## Project Structure

```text
.
├── requirements.txt
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── routers/
│   ├── users.py
│   ├── products.py
│   ├── cart.py
│   └── orders.py
├── tests/
│   ├── test_users.py
│   ├── test_products.py
│   └── test_orders.py
└── sample_data.py
```

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Run the Application

```bash
uvicorn main:app --reload
```

Swagger UI is available at:

```text
http://127.0.0.1:8000/docs
```

## Run Tests

```bash
pytest
```

## API Endpoints

- `GET /` - API health message
- `POST /users/register` - Register a user
- `GET /products/` - List products
- `POST /products/` - Create product
- `POST /cart/` - Add item to cart
- `POST /orders/` - Create order

## GitHub Actions Example

```yaml
name: Python API Tests

on:
  push:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.14'

      - name: Install Dependencies
        run: |
          pip install -r requirements.txt

      - name: Run Tests
        run: |
          pytest
```
