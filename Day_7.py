from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()



class ProductCreate(BaseModel):
    name: str
    price: int

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[int] = None


products = []
next_id = 1


@app.post("/products")
def create_product(payload: ProductCreate):
    global next_id

    product = {
        "id": next_id,
        "name": payload.name,
        "price": payload.price
    }
    products.append(product)
    next_id += 1

    return product



@app.put("/products/{product_id}")
def put_product(product_id: int, payload: ProductCreate):
    for p in products:
        if p["id"] == product_id:
      
            p["name"] = payload.name
            p["price"] = payload.price
            return p

    raise HTTPException(status_code=404, detail="Product not found")



@app.patch("/products/{product_id}")
def patch_product(product_id: int, payload: ProductUpdate):
    for p in products:
        if p["id"] == product_id:

            if payload.name is not None:
                p["name"] = payload.name
            if payload.price is not None:
                p["price"] = payload.price
            return p

    raise HTTPException(status_code=404, detail="Product not found")



@app.get("/products")
def list_products():
    return products
