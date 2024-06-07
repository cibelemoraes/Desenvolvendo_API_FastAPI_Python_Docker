from typing import Annotated
from workout_api.contrib.schemas import BaseSchema
from pydantic import Field

class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', example='CT king', max_length=10)]
    endereço: Annotated[str, Field(description='Endereço do Centro de Treinamento', example='Rua x, n 02', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietario do Centro de Treinamento', example='Marcos', max_length=30)]
