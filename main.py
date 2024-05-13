from fastapi import FastAPI
from fastapi import status
from fastapi import Body

from typing import Annotated

from models.item import Item

app = FastAPI()

# Response Status Code
"""
@app.post("/items", response_model = Item, status_code = status.HTTP_201_CREATED)
async def create_item(item: Annotated[Item, Body()]):
  return item
"""

# Tags
@app.post("/items",
  response_model = Item,
  status_code = status.HTTP_201_CREATED,
  tags = ["Items"])
async def create_item(item: Annotated[Item, Body()]):
  return item
