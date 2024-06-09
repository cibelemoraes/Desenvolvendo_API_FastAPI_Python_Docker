from fastapi import APIRouter, Body, status
from workout_api.categorias.schemas import CategoriaIn, CategoriaOut
from workout_api.contrib.dependencies import DatabaseDepency
router = APIRouter()

@router.post('/', 
             summary='Criar novo Atleta'
             status_code=status.HTTP_201_CREATED
             response_model=CategoriaOut,
             )

async def post(
    db_session: DatabaseDepency, 
    categoria_in:CategoriaIn  = Body(...)
    ) -> CategoriaOut:
    
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel( **categoria_out.model_dump())
    
    db_session.add(categoria_model)
    await db_session.commit()
    
    return categoria_out

    breakpoint()
   