from pydantic import BaseModel

class UserCreateInput(BaseModel): 
    name: str 
    played_games: str 
    favorites_games: str 

    class Config:
        orm_mode = True

class Get_user_input(BaseModel):
    id: int 
    name: str 
    played_games: str
    favorites_games: str 

    class Config:
        orm_mode =True

class Update_user_input(BaseModel):
    name: str 
    played_games: str 
    favorites_games: str 

    class Config:
        orm_mode = True

