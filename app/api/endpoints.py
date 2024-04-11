from fastapi import APIRouter, Request
from .scheduler import *
from core.auth import verify_token
import requests
import json

from .utils import *

import os

router = APIRouter()

@router.post("/exec")
async def execute(request: Request):
    body = await request.body()
    data = json.loads(body.decode())
    
    return {'message': 'ok'}

@router.get("/get")
async def get(canal_id: int):
    url = f'http://localhost:8500/exec'
    response = requests.post(url, data=json.dumps({'data': 'example_data'})).json()
    
    return response