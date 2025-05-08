from typing import Union
from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select
from datetime import datetime

class Food(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    price: float
    
class Expense(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    date: datetime = Field(index=True)
    timeslot: str = Field(index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ExpenseItem(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    expense_id: int = Field(default=None, foreign_key="expense.id")
    food_id: int = Field(default=None, foreign_key="food.id")
    price: float

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
     
create_db_and_tables()
   
app = FastAPI()



@app.get("/",response_model=Food)
async def get_items():
    pass


@app.get("/items/{item_id}",response_model=Expense)
async def post_items(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}