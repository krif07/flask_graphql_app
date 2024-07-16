import strawberry
from typing import List
from sqlalchemy.orm import Session
from models import CartItem
from database import SessionLocal


@strawberry.type
class CartItemType:
    id: int
    name: str
    price: float
    quantity: int
    created_at: str
    updated_at: str


@strawberry.type
class Query:
    @strawberry.field
    def cart_items(self, info) -> List[CartItemType]:
        session: Session = SessionLocal()
        cart_items = session.query(CartItem).all()
        return cart_items


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_cart_item(self, name: str, price: float, quantity: int) -> CartItemType:
        session: Session = SessionLocal()
        new_item = CartItem(name=name, price=price, quantity=quantity)
        session.add(new_item)
        session.commit()
        session.refresh(new_item)
        return new_item

    @strawberry.mutation
    def update_cart_item(self, id: int, name: str, price: float, quantity: int) -> CartItemType:
        session: Session = SessionLocal()
        item = session.query(CartItem).filter(CartItem.id == id).first()
        if item:
            item.name = name
            item.price = price
            item.quantity = quantity
            session.commit()
            session.refresh(item)
        return item

    @strawberry.mutation
    def delete_cart_item(self, id: int) -> bool:
        session: Session = SessionLocal()
        item = session.query(CartItem).filter(CartItem.id == id).first()
        if item:
            session.delete(item)
            session.commit()
            return True
        return False


schema = strawberry.Schema(query=Query, mutation=Mutation)
