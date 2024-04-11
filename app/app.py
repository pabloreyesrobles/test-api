from fastapi import FastAPI
import uvicorn
from api.endpoints import router as ep_router
from api.scheduler import start_scheduler, stop_scheduler
import os

app = FastAPI()

@app.get('/')
def home():
    print('Holaa')
    return ({'message': 'Holaa'})

# Rutas de endpoints
app.include_router(ep_router)

# Scheduler que ejecuta funciones periódicas y subprocesos en segundo plano
# start_scheduler()

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8500)

