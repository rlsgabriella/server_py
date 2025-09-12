from fastapi import fastapi

app = FastAPI()

@app.get("/")
def read_root():
    return {"message" : "Hello word!"}