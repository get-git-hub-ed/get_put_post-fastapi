from fastapi import FastAPI

app = FastAPI()

lst = list()

'''@app.get("/home")
def read():
    return {
        "Hello": "World"
        }'''

@app.get("/home/{username}")
def write_home(user_name: str):
    return {
        "Name": user_name,
        "Age" : 24
        }

@app.put("/username/{user_name}")
def put_data(user_name: str):
    #print(user_name)
    lst.append(user_name)
    return {
        "username": user_name
        }

@app.post("/post_data}")
def post_data(user_name: str):
    lst.append(user_name)
    return {
        "usernames": lst
        }

@app.api_route("/nothome", methods=['GET', 'POST', 'PUT'])
def homedata(user_name: str):
    return{
        "username": user_name
    }