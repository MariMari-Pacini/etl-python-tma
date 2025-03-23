from pydantic import BaseModel, Field, field_validator, constr
from typing import Optional, Literal
from datetime import datetime


class PlanilhaAtendimento(BaseModel):
    ID_Atendimento: int = Field(..., ge=127503, le=127678, description="Identificador único do atendimento")
    
    Tempo_Medio_Atendimento: datetime = Field(..., description="Tempo médio do atendimento em formato datetime (HH:MM:SS)")

    Assunto_Atendimento: Literal[
        "Transferencia", "C&R", "LCD", "Manutencao", "Queda Atendimento"
    ] = Field(..., description="Categoria do atendimento")

    Chamado: Literal["Sim", "Nao"] = Field(..., description="Indica se houve abertura de chamado")

    Improcedente: Optional[float] = Field(None, description="Indica improcedência (quando aplicável)", nullable=True)

    Mais_de_um_protocolo: Literal["Sim", "Nao"] = Field(..., description="Indica se o atendimento teve múltiplos protocolos")

    Acionou_suporte_focal: Literal["Sim", "Nao"] = Field(..., description="Indica se o suporte focal foi acionado")

    # Parse datetime que vem como HH:MM:SS
    @field_validator("Tempo_Medio_Atendimento", mode="before")
    def parse_time_as_datetime(cls, value):
        if isinstance(value, datetime):
            return value
        try:
            return datetime.strptime(value, "%H:%M:%S")
        except ValueError:
            raise ValueError("Tempo_Medio_Atendimento deve estar no formato HH:MM:SS")

    class Config:
        validate_default = True
