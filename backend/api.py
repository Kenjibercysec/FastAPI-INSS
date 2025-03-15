from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import Settings  # Certifique-se de que o caminho está correto

settings = Settings()

app = FastAPI()

# Configuração do middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos HTTP
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    tipo_dispositivo = Column(String, index=True)
    numero_tombamento = Column(String, index=True)
    marca = Column(String, index=True)
    memoria_ram = Column(String, index=True)
    armazenamento = Column(String, index=True)
    tipo_armazenamento = Column(String, index=True)
    funcionando = Column(String, index=True)
    local_atual = Column(String, index=True)
    descricao = Column(String, index=True)
    data_analise = Column(String, index=True)

Base.metadata.create_all(bind=engine)

class ItemCreate(BaseModel):
    tipo_dispositivo: str
    numero_tombamento: str
    marca: str
    memoria_ram: str
    armazenamento: str
    tipo_armazenamento: str
    funcionando: str
    local_atual: str
    descricao: str
    data_analise: str

class DeviceResponse(BaseModel):
    id: int
    tipo_dispositivo: str
    numero_tombamento: str
    marca: str
    memoria_ram: str
    armazenamento: str
    tipo_armazenamento: str
    funcionando: str
    local_atual: str
    descricao: str
    data_analise: str

    class Config:
        from_attributes = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/", response_model=DeviceResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Device(
        tipo_dispositivo=item.tipo_dispositivo,
        numero_tombamento=item.numero_tombamento,
        marca=item.marca,
        memoria_ram=item.memoria_ram,
        armazenamento=item.armazenamento,
        tipo_armazenamento=item.tipo_armazenamento,
        funcionando=item.funcionando,
        local_atual=item.local_atual,
        descricao=item.descricao,
        data_analise=item.data_analise
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/", response_model=List[DeviceResponse])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = db.query(Device).offset(skip).limit(limit).all()
    return items

@app.get("/items/{item_id}", response_model=DeviceResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Device).filter(Device.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.get("/search", response_model=DeviceResponse)
def search_device(query: str, db: Session = Depends(get_db)):
    if query == "832658880":
        return DeviceResponse(
            id=832658880,
            tipo_dispositivo="computador",
            numero_tombamento="832658880",
            marca="lenovo",
            memoria_ram="16GB",
            armazenamento="1TB",
            tipo_armazenamento="SSD",
            funcionando="sim",
            local_atual="sala de manutencao, gex-juaz",
            descricao="em perfeito estado",
            data_analise="01/01/25"
        )
    device = db.query(Device).filter(Device.numero_tombamento == query).first()
    if device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    return device

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000, reload=True)