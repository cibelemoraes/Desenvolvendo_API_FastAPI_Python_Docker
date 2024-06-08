from typing import Annotated
from pydantic import Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema, OutMixin

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Atleta', example='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta ', example='123456789', max_length=11)]
    idade: Annotated[str, Field(description='Idade do Atleta', example=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do Atleta', example=75.5)]
    altura : Annotated[PositiveFloat, Field(description='Altura do Atleta', example=1.70)]
    sexo : Annotated[str, Field(description='Sexo do Atleta', example='M', max_lenhth=1)]
    
class AtletaIn(Atleta):
    pass

class AtletaOut(AtletaIn, OutMixin)
    pass