
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

import model.calidad_del_aire as cal


#Base model
class Enviroment(BaseModel):
    AM: float
    BM: float
    CM: float
    DM: float
    EM: float

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
        data_predic = pd.DataFrame({'A': [enviroment.AM], 'B': [enviroment.BM], 'C': [enviroment.CM], 'D': [enviroment.DM], 'E': [enviroment.EM]})
        cal.prediction_asd(data_predic)
        return 'recived'