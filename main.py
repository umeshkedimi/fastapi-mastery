from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

@app.get("/")
def root():
    return {"message": "FastAPI Mastery Repo is Working!"}

@app.get("/posts")
def posts():
    return {"data": "This is Post1"}

@app.post("/createpost")
def create_posts(new_post:Post):
    print(new_post)
    return {"new_post": "New post created", "info": f"Title-{new_post.title}. Content-{new_post.content}"}