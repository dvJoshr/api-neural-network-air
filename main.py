from fastapi import FastAPI
from pydantic import BaseModel

#Base model

class Enviroment(BaseModel):
    CO: str
    NO2: str
    PM_2: str
    PM10: str
    OZONE: str

app = FastAPI()

posts = []

enviroments = []

@app.get('/')
def read_root():
    return {'Welcome': 'Welcome to my API server'}

@app.get('/posts')
def get_posts():
    return enviroments 

@app.post('/post')
def save_enviroments(enviroment: Enviroment):
        enviroments.append(enviroment.dict())
        return 'recived'

