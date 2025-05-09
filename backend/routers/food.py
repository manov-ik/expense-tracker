from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select,SQLModel,Field
from typing import List
from models import Food
from db import engine


class Food(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    price: float

router = APIRouter()

def get_session():
    with Session(engine) as session:
        yield session

@router.post("/", response_model=Food) # new food
def create_food(food: Food, session: Session = Depends(get_session)):
    session.add(food)
    session.commit()
    session.refresh(food)
    return food


@router.get("/", response_model=List[Food]) # get all foods
def get_all_foods(session: Session = Depends(get_session)):
    foods = session.exec(select(Food)).all()
    return foods

@router.get("/{food_id}", response_model=Food) # get a food
def get_food(food_id: int, session: Session = Depends(get_session)):
    food = session.get(Food, food_id)
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")
    return food

@router.put("/{food_id}", response_model=Food) # update a food
def update_food(food_id: int, updated_food: Food, session: Session = Depends(get_session)):
    food = session.get(Food, food_id)
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")

    food.name = updated_food.name
    food.price = updated_food.price
    session.add(food)
    session.commit()
    session.refresh(food)
    return food

# Delete a food
@router.delete("/{food_id}")
def delete_food(food_id: int, session: Session = Depends(get_session)):
    food = session.get(Food, food_id)
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")
    session.delete(food)
    session.commit()
    return {"ok": True}
