from datetime import datetime
from sqlalchemy import Integer, String, DateTime, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel


class AtletaModel(BaseModel):
    __tablename__='atletas'
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), nullable=False)
    idade: Mapped[str] = mapped_column(Integer, nullable=False)
    peso: Mapped[str] = mapped_column(Float, nullable=False)
    altura : Mapped[str] = mapped_column(String(1), nullable=False)
    sexo : Mapped[str] = mapped_column(String(50), nullable=False)
    created_at : Mapped[DateTime] = mapped_column(DateTime,nullable=False)
    categoria: Mapped['CategriaModel'] = relationship(back_populates='atleta')
    categoria_id = Mapped[int] = mapped_column(ForeignKey('categoria.ph_id'))