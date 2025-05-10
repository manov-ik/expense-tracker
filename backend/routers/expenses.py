from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models import Expense, ExpenseItem, Food
from db import get_session
from typing import List
from datetime import datetime

router = APIRouter()

@router.post("/expense/", response_model=Expense)  # Create a new expense session (morning/afternoon/night/fullday)
def create_expense(timeslot: str, session: Session = Depends(get_session)):
    expense = Expense(date=datetime.utcnow(), timeslot=timeslot) 
    session.add(expense)
    session.commit()
    session.refresh(expense)
    return expense

@router.post("/expense/{expense_id}/item/") # Add items (foods) to a specific expense session
def add_expense_item(expense_id: int, food_id: int, price: float | None = None, session: Session = Depends(get_session)):
    # Optional: check that the food exists
    food = session.get(Food, food_id)
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")

    expense_item = ExpenseItem(
        expense_id=expense_id,
        food_id=food_id,
        price=price if price is not None else food.price
    )
    session.add(expense_item)
    session.commit()
    session.refresh(expense_item)
    return expense_item

@router.get("/expense/", response_model=List[Expense]) # Get all expense sessions with their items
def get_all_expenses(session: Session = Depends(get_session)):
    expenses = session.exec(select(Expense)).all()
    return expenses

@router.get("/expense/{expense_id}/items/") # Get items for a specific expense
def get_expense_items(expense_id: int, session: Session = Depends(get_session)):
    statement = select(ExpenseItem).where(ExpenseItem.expense_id == expense_id)
    items = session.exec(statement).all()
    return items

@router.get("/get-all-items/")
def get_all_items(session: Session = Depends(get_session)):
    items = session.exec(select(ExpenseItem)).all()
    return items

@router.delete("/delete-all/")
def delete_all_items(session: Session = Depends(get_session)):
    session.query(ExpenseItem).delete()
    session.commit()
    return {"message": "All items deleted"}