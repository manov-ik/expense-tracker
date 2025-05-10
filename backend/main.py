from typing import Union
from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select
from datetime import datetime
from routers import food, expenses

app = FastAPI()


app.include_router(food.router, prefix="/food", tags=["food"])
app.include_router(expenses.router, prefix="/expenses", tags=["expenses"])



# @app.get("/",response_model=Food)
# async def get_items():
#     pass


# @app.get("/items/{item_id}",response_model=Expense)
# async def post_items(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}