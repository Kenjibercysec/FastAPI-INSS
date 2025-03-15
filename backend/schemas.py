from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional, List

class DeviceBase(BaseModel):
    tipo_de_disp: str
    qnt_ram: Optional[int] = None
    qnt_armaz: Optional[int] = None
    tipo_armaz: Optional[str] = None
    marca: str
    funcionando: Optional[bool] = None
    data_de_an: Optional[date] = None
    locat_do_disp: str
    descricao: str

class DeviceCreate(DeviceBase):
    id_tomb: int

class DeviceUpdate(DeviceBase):
    id_tomb: int

class DeviceResponse(DeviceBase):
    id_tomb: int

    class Config:
        from_attributes = True

class LogAtualizacaoBase(BaseModel):
    id_tomb: int
    campo_alterado: Optional[str] = None
    valor_antigo: Optional[str] = None
    valor_novo: Optional[str] = None
    data_hora_alteracao: Optional[datetime] = None

class LogAtualizacaoCreate(LogAtualizacaoBase):
    pass

class LogAtualizacaoResponse(LogAtualizacaoBase):
    id_log: int

    class Config:
        from_attributes = True