
from typing import Annotated
from uuid import UUID
from Datetime import DateTime # type: ignore
from pydantic import BaseModel, UUID4, Field

    
    
class BaseSchema(BaseModel):
    class Config:
        extra= 'forbid'
        from_atributes = True
        
class OutMixin(BaseModel):
    id: Annotated[UUID4, Field(description='Identificador')]
    created_at: Annotated[DateTime, Field(description='Data de criação')]