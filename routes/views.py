from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from database.connection import SessionLocal
from schemas import UserCreateInput, Get_user_input,Update_user_input
from services import UserService
from database.connection import SessionLocal
from database.models import User

user_router = APIRouter(prefix='/user')

session = SessionLocal()

@user_router.post('/create')
def user_create(user_input: UserCreateInput): 

    UserService.create_user(name=user_input.name, played_games = user_input.played_games,
    favorites_games = user_input.favorites_games)


    return 'Enviado com Sucesso'
    
    
@user_router.get('/get', response_model= Get_user_input)
def get_user(user_input: int):
        user = UserService.get_user(user_input)

        if user is None:
            raise HTTPException(status_code=400, detail='Não existe dados referente')
        
        return jsonable_encoder(user)

@user_router.delete('/delete/{user_id}')
def delete_user(user_input: int):
    try:
        user = UserService.delete_user(id=user_input)

        
        return 'Dados apagados com sucesso!'

    except Exception as error:
        raise HTTPException(400, detail=str(error))

@user_router.put('/put', response_model=Update_user_input)
def update_user(id : int , user_input: Update_user_input):
    user = session.query(User).filter(User.id == id).first()

    try:
        if user_input.name:
            user.name = user_input.name
    except:
        pass
    try:
        if user_input.played_games:
            user.played_games = user_input.played_games
    except:
        pass
    try:
        if user_input.favorites_games:
            user.favorites_games = user_input.favorites_games
    except:
        pass

    session.commit()  

    raise HTTPException(status_code=201, detail = 'Dados atualizados com sucesso!')



    


