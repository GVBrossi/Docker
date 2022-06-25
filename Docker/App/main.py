from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
async def root():
    return {"message": "Bora fica rico"}

@app.get("/api/{name}")
async def get_user(name):
    return {
        "name": name,
        "message": f"Oi, {name}, vc vai ficar rico"
    }
