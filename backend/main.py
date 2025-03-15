from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas
from .database import engine, get_db
from .config import Settings

settings = Settings()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure the database connection is established
try:
    models.Base.metadata.create_all(bind=engine)
except Exception as e:
    print(f"Error connecting to the database: {e}")

@app.post("/devices/", response_model=schemas.DeviceResponse, status_code=status.HTTP_201_CREATED)
def create_device(device: schemas.DeviceCreate, db: Session = Depends(get_db)):
    db_device = models.Device(**device.dict())
    db.add(db_device)
    try:
        db.commit()
        db.refresh(db_device)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return db_device

@app.get("/devices/", response_model=List[schemas.DeviceResponse])
def read_devices(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    devices = db.query(models.Device).offset(skip).limit(limit).all()
    return devices

@app.get("/devices/{id_tomb}", response_model=schemas.DeviceResponse)
def read_device(id_tomb: int, db: Session = Depends(get_db)):
    device = db.query(models.Device).filter(models.Device.id_tomb == id_tomb).first()
    if device is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Device not found")
    return device

@app.put("/devices/{id_tomb}", response_model=schemas.DeviceResponse)
def update_device(id_tomb: int, device: schemas.DeviceUpdate, db: Session = Depends(get_db)):
    db_device = db.query(models.Device).filter(models.Device.id_tomb == id_tomb).first()
    if db_device is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Device not found")
    for key, value in device.dict(exclude_unset=True).items():
        setattr(db_device, key, value)
    db.commit()
    db.refresh(db_device)
    return db_device

@app.delete("/devices/{id_tomb}", status_code=status.HTTP_204_NO_CONTENT)
def delete_device(id_tomb: int, db: Session = Depends(get_db)):
    db_device = db.query(models.Device).filter(models.Device.id_tomb == id_tomb).first()
    if db_device is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Device not found")
    db.delete(db_device)
    db.commit()
    return

@app.get("/search/{numero_tombamento}", response_model=List[schemas.DeviceResponse])
def search_devices(numero_tombamento: str, db: Session = Depends(get_db)):
    devices = db.query(models.Device).filter(models.Device.numero_tombamento == numero_tombamento).all()
    if not devices:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Devices not found")
    return devices

@app.post("/logs/", response_model=schemas.LogAtualizacaoResponse, status_code=status.HTTP_201_CREATED)
def create_log(log: schemas.LogAtualizacaoCreate, db: Session = Depends(get_db)):
    db_log = models.LogAtualizacao(**log.dict())
    db.add(db_log)
    try:
        db.commit()
        db.refresh(db_log)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return db_log

@app.get("/logs/", response_model=List[schemas.LogAtualizacaoResponse])
def read_logs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    logs = db.query(models.LogAtualizacao).offset(skip).limit(limit).all()
    return logs

@app.get("/logs/{id_log}", response_model=schemas.LogAtualizacaoResponse)
def read_log(id_log: int, db: Session = Depends(get_db)):
    log = db.query(models.LogAtualizacao).filter(models.LogAtualizacao.id_log == id_log).first()
    if log is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Log not found")
    return log