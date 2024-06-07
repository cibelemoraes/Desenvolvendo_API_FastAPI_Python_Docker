from pydantic import BaseModel

class Atleta(BaseModel):
    nome: Annotated[str, Field(description='Nome do Atleta', examples='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta ', examples='123456789', max_length=11)]
    idade: Annotated[str, Field(description='Idade do Atleta', examples=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do Atleta', examples=75.5)]
    altura : Annotated[PositiveFloat, Field(description='Altura do Atleta', examples=1.70)]
    sexo : Annotated[str, Field(description='Sexo do Atleta', examples='1234594440', max_lenhth=11)]