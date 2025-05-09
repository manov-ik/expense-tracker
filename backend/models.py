from sqlmodel import SQLModel, Field
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
