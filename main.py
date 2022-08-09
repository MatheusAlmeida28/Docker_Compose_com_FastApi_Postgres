from fastapi import FastAPI, APIRouter
from routes.views import user_router


app = FastAPI()
router = APIRouter()

@router.get('/')
def home():
    return 'Tudo ok'


app.include_router(prefix='/home', router=router)
app.include_router(user_router)