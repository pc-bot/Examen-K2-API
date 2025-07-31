from fastapi import FastAPI
from email.policy import HTTP
from fastapi import FastAPI, Request, HTTPException, Response
from typing import Optional , List
from pydantic import BaseModel
import uvicorn
from starlette.templating import Jinja2Templates
from starlette.responses import JSONResponse

list_posts = []

class postLists(BaseModel):
    author : str
    title : str
    content : str

app = FastAPI()

@app.get("/ping/")
async def found_pong():
    return Response("pong", status_code=200)

@app.post("/posts/")
async def add_post(posts : postLists):
    list_posts.append(posts)
    return JSONResponse("il a été ajoute", status_code=201)

@app.get("/posts/")
async def post_lists():
    return list_posts

@app.put("/posts/{title_post}")
async def update_lists(title_post : str, posts : postLists):
    if title_post != posts.title:
        list_posts.append(posts)
        return JSONResponse({"message" : "new post added "},status_code=201)
    list_posts[title_post] = posts
    return list_posts

class Basic_Authentication(BaseModel):
    username : str
    password : str


@app.get("/ping/auth")
async def found_pong( authentification : Basic_Authentication ):
    if authentification.username == "admin" and authentification.password :
        return Response("pong", status_code=200)
    return JSONResponse({"message ":"you must be indentified"},status_code=401)

        



    













