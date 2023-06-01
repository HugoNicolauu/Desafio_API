from fastapi import FastAPI
from core.configs import setting
from api.v1.api import api_router

app = FastAPI(title='Desafio_API')
app.include_router(api_router,prefix=setting.API_V1_STR)

if __name__=='__main__':
    import uvicorn 
    uvicorn.run("main:app",host="0.0.0.0",
                 port=8000,log_level='info',reload=True)