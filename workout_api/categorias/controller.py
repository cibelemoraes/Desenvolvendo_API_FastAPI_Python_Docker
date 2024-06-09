from uuid import uuid4
from fastapi import APIRouter, Body, status
from pydantic import UUID4
from sqlalchemy import select
from workout_api.categorias.models import CategoriaModel
from workout_api.categorias.schemas import CategoriaIn, CategoriaOut
from workout_api.contrib.dependencies import DatabaseDepency

router = APIRouter()

@router.post('/', 
             summary='Criar uma nova Categoria'
             status_code=status.HTTP_201_CREATED
             response_model=CategoriaOut,
             )

async def post(
    db_session: DatabaseDependency, 
    categoria_in:CategoriaIn  = Body(...)
    ) -> CategoriaOut:
    
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel( **categoria_out.model_dump())
    
    db_session.add(categoria_model)
    await db_session.commit()
    
    return categoria_out

@router.get('/', 
             summary='Consultar todas as Categorias'
             status_code=status.HTTP_201_OK,
             response_model=LIST[CategoriaOut],
             )

async def query(
    db_session: DatabaseDepency, ) -> list[CategoriaOut]:
    categorias:list[CategoriaOut] = (await db_session.execute(select(CategoriaModel))).scalars().all()
    
    return categorias

@router.get('/{id}', 
             summary='Consultar uma Categoria pelo id'
             status_code=status.HTTP_201_OK,
             response_model=LIST[CategoriaOut],
             )

async def query( id: UUID4, db_session: DatabaseDepency, ) -> CategoriaOut:
    categorias:CategoriaOut = (await db_session.execute(select(CategoriaModel).filter_by(id=id))
    ).scalars().first()
    
    if not categorias:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Categoria não encontrada no id: {id}'
        )
    
    return categorias
    