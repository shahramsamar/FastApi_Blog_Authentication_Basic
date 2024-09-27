from fastapi import FastAPI, status, HTTPException, Query, Path, Form,Body,File,UploadFile,Depends
from fastapi.responses import JSONResponse
from typing import Optional,List
import random
from datetime import datetime
from pydantic import BaseModel

from sqlalchemy.orm import Session
from core.database import get_db, initiate_database, StudentModel

app = FastAPI()

names_db = [
    {
        "id": 1,
        "name": "ali"
    },
    {
        "id": 2,
        "name": "maryam"
    },
    {
        "id": 3,
        "name": "arousha"
    },
    {
        "id": 4,
        "name": "alireza"
    },
    {
        "id": 5,
        "name": "alimi"
    },
]


@app.on_event("startup")
async def startup_event():
    initiate_database()

# search: Optional[str] = None

class NamesSchema(BaseModel):
    name : str 
    
class ResponseNamesSchema(NamesSchema):
    id: int



@app.get("/names",response_model=List[ResponseNamesSchema],status_code=status.HTTP_200_OK)
async def names_list(search: Optional[str] = Query(None, description="searching names"),db:Session =Depends(get_db)):
    return db.query(StudentModel).all()
    # result = names_db
    # if search:
    #     result = [item for item in names_db if search.lower()
    #               in item["name"].lower()]
    # return result


@app.post("/names",response_model=ResponseNamesSchema,status_code=status.HTTP_201_CREATED)
async def names_create(request:NamesSchema,db:Session =Depends(get_db)):
    student_obj = StudentModel(name=request.name)
    db.add(student_obj)
    db.commit()
    db.refresh(student_obj)
    return student_obj
    # new_name = {"id": random.randint(100, 1000), "name": request.name}
    # names_db.append(new_name)
    
    # # return JSONResponse(new_name, status_code=status.HTTP_201_CREATED)
    # return new_name


@app.get("/names/{item_id}",response_model=ResponseNamesSchema,status_code=status.HTTP_200_OK)
async def names_detail(item_id: int = Path(description="something cool"),db:Session =Depends(get_db)):
    student_obj = db.query(StudentModel).filter(StudentModel.id == item_id).one_or_none()
    
    if not student_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="item not found")
    return student_obj
    
    # for name in names_db:
    #     if name["id"] == item_id:
    #         # return name
    #         return name

 


@app.put("/names/{item_id}",response_model=ResponseNamesSchema,status_code=status.HTTP_200_OK)
async def names_update(item_id: int, request:NamesSchema,db:Session =Depends(get_db)):
    student_obj = db.query(StudentModel).filter(StudentModel.id == item_id).one_or_none()
    
    if not student_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="item not found")
    student_obj.name = request.name
    db.commit()
    db.refresh(student_obj)
    return student_obj
    
    # for item in names_db:
    #     if item["id"] == item_id:
    #         item["name"] = request.name
    #         return item

    # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                     detail="item not found")


@app.delete("/names/{item_id}")
async def names_delete(item_id: int,db:Session =Depends(get_db)):
    student_obj = db.query(StudentModel).filter(StudentModel.id == item_id).one_or_none()
    
    if not student_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="item not found")
    db.delete(student_obj)
    db.commit()
    return JSONResponse({"detail": "item removed successfully"}, status_code=status.HTTP_200_OK)
    # for index, item in enumerate(names_db):
    #     if item["id"] == item_id:
    #         del names_db[index]
    #         return JSONResponse({"detail": "item removed successfully"}, status_code=status.HTTP_200_OK)

    # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                     detail="item not found")

# GET  /names List
# GET /names/<id> Detail
# POST /names Create
# PUT/PATCH  /names/<id> Update
# DELETE /names/<id> DELETE

# /names  GET POST
# /names/<id> GET PUT/PATCH DELETE