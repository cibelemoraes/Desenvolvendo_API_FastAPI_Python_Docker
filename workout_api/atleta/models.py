from datetime import datetime
from sqlalchemy import ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.categorias.models import CategoriaModel
from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.contrib.models import BaseModel


class AtletaModel(BaseModel):
    __tablename__='atletas'
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11),unique=True, nullable=False)
    idade: Mapped[str] = mapped_column(Integer, nullable=False)
    peso: Mapped[str] = mapped_column(Float, nullable=False)
    altura : Mapped[str] = mapped_column(Float, nullable=False)
    sexo : Mapped[str] = mapped_column(String(50), nullable=False)
    created_at : Mapped[DateTime] = mapped_column(DateTime,nullable=False)
    categoria: Mapped['CategoriaModel'] = relationship(back_populates='atleta')
    categoria_id : Mapped[int] = mapped_column(ForeignKey('categoria.pk_id'))
    centro_treinamento: Mapped['CentroTreinamentoModel'] = relationship(back_populates='atleta')
    centro_treinamento_id : Mapped[int] = mapped_column(ForeignKey('centro_treinamento.pk_id'))
    