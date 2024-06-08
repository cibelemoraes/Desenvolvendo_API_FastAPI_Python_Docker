from fastapi import APIRouter
from workout_api.contrib.dependencies import DatabaseDepency
router = APIRouter()

@router.post('/', 
             summary='Criar novo Atleta'
             status_code=status.HTTP_201_CREATED
             )

async def post(db_session: DatabaseDependancy):
    pass