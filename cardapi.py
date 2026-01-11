from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()
class Details(BaseModel):
    name: str
    age: int
    aadhar: str
    legacy_id: int
    card_type: str
    status: str
records = [
    Details(name="Rahul", age=25, aadhar="1234-5678-9012", legacy_id=101, card_type="Silver", status="Active"),
    Details(name="Priya", age=30, aadhar="4567-8901-2345", legacy_id=102, card_type="Gold", status="Inactive"),
    Details(name="Amit", age=28, aadhar="7890-1234-5678", legacy_id=103, card_type="Platinum", status="Active")
]
@app.get("/")
def welcome():
    return {"message": "Welcome to Card Management System!"}
@app.get("/details")
def get_details():
    return records
class Details(BaseModel):
    legacy_id: int
    name: str
    age: int
    aadhar: str
    card_type: str
    status: str

@app.post("/details")
def create(detail: Details):
    records.append(detail.dict())
    return {"message": "Record added"}

@app.put("/details/{legacy_id}")
def update(legacy_id: int, detail: Details):
    for i, rec in enumerate(records):
        if rec.legacy_id == legacy_id:
            records[i] = detail
            return {"message": "Updated", "data": detail}
    raise HTTPException(status_code=404, detail="Record not found")    
    raise HTTPException(status_code=404, detail="Record not found")
@app.delete("/details/{legacy_id}")
def delete_details(legacy_id: int):
    for index, rec in enumerate(records):
        if rec.legacy_id == legacy_id:
            removed = records.pop(index)
            return {"msg": "Record deleted successfully", "data": removed}
    
    raise HTTPException(status_code=404, detail="Record not found")
