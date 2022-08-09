from fastapi import APIRouter, HTTPException
from sqlalchemy import delete
from sqlalchemy.future import select
from database.models import User
from database.connection import SessionLocal
from fastapi.encoders import jsonable_encoder

session = SessionLocal()

class UserService:
    def create_user(name, played_games, favorites_games):
        session.add(User(name=name, played_games=played_games, 
        favorites_games=favorites_games))
        
        session.commit()  

    
    def get_user(id:int):
        result = session.execute(select(User).where(User.id == id))
        
        return result.scalar()

    def delete_user(id:int):
        session.execute(select(User).where(User.id == id))

        session.commit()
    

