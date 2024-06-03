from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import Table, func
from datetime import datetime, timedelta
from database import get_db_fonte, get_db_alvo
import models
import schemas
from utils import process_data

app = FastAPI()  

@app.post("/transfer/")
def transfer_data(input: schemas.input, db_fonte: Session = Depends(get_db_fonte), db_alvo: Session = Depends(get_db_alvo)):

    start_time = input.timestamp
    end_time = start_time + timedelta(minutes=9)
    names = input.names
    id = db_alvo.query(func.count(models.signal.id)).scalar() + 1
    print(id)

    columns = [getattr(models.data_fonte, name) for name in names if hasattr(models.data_fonte, name)]
    if not columns:
        raise HTTPException(status_code=400, detail="Nenhuma coluna válida especificada em names")

    dados_fonte = db_fonte.query(*columns).filter(
        models.data_fonte.timestamp >= start_time,
        models.data_fonte.timestamp <= end_time
    ).all()
    
    if not dados_fonte:
        raise HTTPException(status_code=404, detail="Dados não encontrados para o intervalo de tempo fornecido")

    df = process_data(dados_fonte, names)

    print(start_time)
    print(df)

    novo_signal = models.signal(
        id = id,
        name = names
    )
    novo_data = models.data_alvo(
        timestamp = start_time,
        signal_id = id,
        value = df.to_json()
    )
    db_alvo.add(novo_signal)
    db_alvo.add(novo_data)
    db_alvo.commit()
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)