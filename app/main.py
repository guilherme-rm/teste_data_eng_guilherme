from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import timedelta
from database import get_db_fonte, get_db_alvo
import models
import schemas
from utils import process_data

app = FastAPI()  

@app.post("/transfer/")
def transfer_data(input: schemas.input, db_fonte: Session = Depends(get_db_fonte), db_alvo: Session = Depends(get_db_alvo)):

    query_time = input.timestamp
    end_time = query_time + timedelta(minutes=9)
    names = input.names
    id = db_alvo.query(func.count(models.signal.id)).scalar() + 1

    start_date = db_fonte.query(models.data_fonte.timestamp).first()[0]
    last_date = start_date + timedelta(days=9, hours=23, minutes=59)

    print(query_time)

    if end_time > last_date:
        raise HTTPException(status_code=400)

    columns = [getattr(models.data_fonte, name) for name in names if hasattr(models.data_fonte, name)]
    
    dados_fonte = db_fonte.query(*columns).filter(
        models.data_fonte.timestamp >= query_time,
        models.data_fonte.timestamp <= end_time
    ).all()
    
    if not dados_fonte:
        raise HTTPException(status_code=404, detail="Data not found")

    df = process_data(dados_fonte, names)

    print(query_time)
    print(df)

    new_signal = models.signal(
        id = id,
        name = names
    )
    new_data = models.data_alvo(
        timestamp = query_time,
        signal_id = id,
        value = df.to_json()
    )
    db_alvo.add(new_signal)
    db_alvo.add(new_data)
    db_alvo.commit()
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)