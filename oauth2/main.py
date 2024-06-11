from typing import Annotated
# from fastapi import Depends, FastAPI
# from fastapi.security import OAuth2PasswordRequestForm


from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from  jose import jwt 

# app=FastAPI()
# @app.get("/")
# async def get():
#     return {"message":"hello world"}


app=FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@app.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):

 if form_data.username!= "afsheen": 
         raise HTTPException(status_code=400, detail="Incorrect username ")
 if form_data.password!= "afs": 
         raise HTTPException(status_code=400, detail="Incorrect password ")
 token = jwt.encode({'username': 'form_data.username'},
                     'abc', algorithm='HS256') # type: ignore

 return {"access_token": token}

@app.get("/user/username/")
async def user_route(token: Annotated[str, Depends(oauth2_scheme)]):
    user=jwt.decode(token, 'abc', algorithms=['HS256'])
    return {"user": user}

@app.get("/user/msg/")
async def user_msg(token: Annotated[str, Depends(oauth2_scheme)]):
    
    return {"user": "hello world"}
