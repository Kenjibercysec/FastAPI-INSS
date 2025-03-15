from sqlalchemy import Column, Integer, String, Date, Boolean, TIMESTAMP, ForeignKey, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base

class Device(Base):
    __tablename__ = "dispositivos"

    id_tomb = Column(Integer, primary_key=True, unique=True, nullable=False)
    tipo_de_disp = Column(String(50), nullable=False)
    qnt_ram = Column(Integer)
    qnt_armaz = Column(Integer)
    tipo_armaz = Column(String(3))
    marca = Column(String(50), nullable=False)
    funcionando = Column(Boolean)
    data_de_an = Column(Date)
    locat_do_disp = Column(String(40), nullable=False)
    descricao = Column(Text, nullable=False)

    logs = relationship("LogAtualizacao", back_populates="device")

class LogAtualizacao(Base):
    __tablename__ = "log_atualizacoes"

    id_log = Column(Integer, primary_key=True, autoincrement=True)
    id_tomb = Column(Integer, ForeignKey("dispositivos.id_tomb"), nullable=False)
    campo_alterado = Column(String(50))
    valor_antigo = Column(Text)
    valor_novo = Column(Text)
    data_hora_alteracao = Column(TIMESTAMP, default=func.now())

    device = relationship("Device", back_populates="logs")