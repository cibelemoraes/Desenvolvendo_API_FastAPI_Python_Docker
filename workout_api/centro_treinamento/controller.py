from uuid import uuid4
from fastapi import APIRouter, Body, status, HTTPException
from pydantic import UUID4
from sqlalchemy import select
from workout_api.categorias.models import CategoriaModel
from workout_api.centro_treinamento import CentroTreinamentoaModel
from workout_api.centro_treinamento.schemas import CentroTreinamentoIn, CentroTreinamentoOut
from workout_api.contrib.dependencies import DatabaseDepency

router = APIRouter()

@router.post('/', 
             
    summary='Criar uma novo Centro de TREINAMENTO'
    status_code=status.HTTP_201_CREATED
    response_model=CentroTreinamento,
     )

async def post(
    db_session: DatabaseDepency, 
    centro_treinamento: CentroTreinamentoIn  = Body(...)
    ) -> CentroTreinamentoOut:
     centro_treinamento_out = CentroTreinamentoOut(id=uuid4(), ** centro_treinamento.model_dump())
     centro_treinamento_model = CategoriaModel( ** centro_treinamento_out.model_dump())
    
    
   
@router.get('/', 
             summary='Consultar todas os centrotreinamento'
             status_code=status.HTTP_201_OK,
             response_model=LIST[CategoriaOut],
             )

async def query(
    db_session: DatabaseDepency, ) -> list[centro_treinamentoOut]:
    ccentro_treinamento:list[centro_treinamentoOut] = (await db_session.execute(select(centro_treinamentoModel))).scalars().all()
    
    return centro_treinamento

@router.get('/{id}', 
             summary='Consultar uma centro treinamento pelo id'
             status_code=status.HTTP_201_OK,
             response_model=LIST[CentroTreinamentoOut],
             )

async def query( id: UUID4, db_session: DatabaseDepency, ) -> CentroTreinamentoOut:
    CentroTreinamento: CentroTreinamento = (await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id))
    ).scalars().first()
    
    if not CentroTreinamento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'centro treinamento não encontrada no id: {id}'
        )
    
    return cCentroTreinamento
    