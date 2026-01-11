from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Pydantic model
class Details(BaseModel):
    name: str
    age: int
    aadhar: str
    legacy_id: int
    card_type: str
    status: str

# In-memory database with 3 sample records
records = [
    Details(name="Rahul", age=25, aadhar="1234-5678-9012", legacy_id=101, card_type="Silver", status="Active"),
    Details(name="Priya", age=30, aadhar="4567-8901-2345", legacy_id=102, card_type="Gold", status="Inactive"),
    Details(name="Amit", age=28, aadhar="7890-1234-5678", legacy_id=103, card_type="Platinum", status="Active")
]


# GET / : Welcome route
@app.get("/")
def welcome():
    return {"message": "Welcome to Card Management System!"}


# GET /details : List all records
@app.get("/details")
def get_details():
    return records


# POST /details : Add a new record
@app.post("/details")
def add_details(detail: Details):
    records.append(detail)
    return {"msg": "Record added successfully", "data": detail}


# PUT /details/{legacy_id} : Update record by legacy_id
@app.put("/details/{legacy_id}")
def update_details(legacy_id: int, updated_data: Details):
    for index, rec in enumerate(records):
        if rec.legacy_id == legacy_id:
            records[index] = updated_data
            return {"msg": "Record updated successfully", "data": updated_data}
    
    raise HTTPException(status_code=404, detail="Record not found")


# DELETE /details/{legacy_id} : Delete record by legacy_id
@app.delete("/details/{legacy_id}")
def delete_details(legacy_id: int):
    for index, rec in enumerate(records):
        if rec.legacy_id == legacy_id:
            removed = records.pop(index)
            return {"msg": "Record deleted successfully", "data": removed}
    
    raise HTTPException(status_code=404, detail="Record not found")
