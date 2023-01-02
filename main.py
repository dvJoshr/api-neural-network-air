import os

import pandas as pd
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
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

app.mount("/static", StaticFiles(directory="static"), name="static")
parent_dir_path = os.path.dirname(os.path.realpath(__file__))
posts = []

enviroments = []

@app.get('/')
def read_root():
    return {'Welcome': 'Welcome to my API server'}

@app.get('/favicon.ico')
async def favicon():
    file_name = "favicon.ico"
    print(parent_dir_path)
    return FileResponse(path=parent_dir_path + "/static/" + file_name)

@app.get('/posts')
def get_posts():
    return enviroments 

@app.post('/post')
def save_enviroments(enviroment: Enviroment):
        data_predic = pd.DataFrame({'A': [enviroment.AM], 'B': [enviroment.BM], 'C': [enviroment.CM], 'D': [enviroment.DM], 'E': [enviroment.EM]})
        cal.prediction_asd(data_predic)
        return 'recived'