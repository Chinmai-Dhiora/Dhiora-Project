from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Std(BaseModel):
    name: str
    age: int

stds = {
    1: {"name": "Sita", "age": 20},
    2: {"name": "Gita", "age": 22}
}

@app.get("/std/{std_id}")
def get_std(std_id: int):
    if std_id not in stds:
        raise HTTPException(status_code=404, detail="Student not found")
    return stds[std_id]

@app.post("/std/{std_id}")
def create_std(std_id: int, std: Std):
    if std_id in stds:
        raise HTTPException(status_code=400, detail="Student already exists")
    stds[std_id] = std.dict()
    return {"message": "Student added", "std": stds[std_id]}

@app.put("/std/{std_id}")
def update_std(std_id: int, std: Std):
    if std_id not in stds:
        raise HTTPException(status_code=404, detail="Student not found")
    stds[std_id] = std.dict()
    return {"message": "Student updated", "std": stds[std_id]}

@app.delete("/std/{std_id}")
def delete_std(std_id: int):
    if std_id not in stds:
        raise HTTPException(status_code=404, detail="Student not found")
    del stds[std_id]
    return {"message": "Student deleted"}
