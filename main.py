from fastapi import FastAPI
from fastapi import status
from fastapi import Body

from typing import Annotated
from enum import Enum

from models.item import Item

app = FastAPI()

# Response Status Code
"""
@app.post("/items", response_model = Item, status_code = status.HTTP_201_CREATED)
async def create_item(item: Annotated[Item, Body()]):
  return item
"""

# Tags
"""
@app.post("/items",
  response_model = Item,
  status_code = status.HTTP_201_CREATED,
  tags = ["Items"])
async def create_item(item: Annotated[Item, Body()]):
  return item
"""

# Tags with Enums
class Tags(Enum):
  items = "Items"

"""
@app.post("/items",
  response_model = Item,
  status_code = status.HTTP_201_CREATED,
  tags = [Tags.items])
async def create_item(item: Annotated[Item, Body()]):
  return item
"""

# Summary and description
"""
@app.post("/items",
  response_model = Item,
  status_code = status.HTTP_201_CREATED,
  tags = [Tags.items],
  summary = "Create an item",
  description = "Create an item with all the information, name, description, price, tax and a set of unique tags")
async def create_item(item: Annotated[Item, Body()]):
  return item
"""

# Description from docstring
"""
@app.post("/items",
  response_model = Item,
  status_code = status.HTTP_201_CREATED,
  tags = [Tags.items],
  summary = "Create an item")
async def create_item(item: Annotated[Item, Body()]):
  return item
"""

# Response description
@app.post("/items",
  response_model = Item,
  status_code = status.HTTP_201_CREATED,
  tags = [Tags.items],
  summary = "Create an item",
  response_description="The created item"
)
async def create_item(item: Annotated[Item, Body()]):
  """
  Create an item with all the information:

  - **name**: each item must have a name
  - **description**: a long description
  - **price**: required
  - **tax**: if the item doesn't have tax, you can omit this
  - **tags**: a set of unique tag strings for this item
  """
  return item

# Deprecate a path operation
@app.get("/items", tags = [Tags.items], deprecated=True)
async def read_items():
  return []
