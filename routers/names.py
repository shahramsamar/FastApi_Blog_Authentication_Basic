from fastapi import APIRouter
from fastapi import status, HTTPException, Query, Path, Form,Body,File,UploadFile,Depends
from fastapi.responses import JSONResponse
from typing import Optional,List
import random
from datetime import datetime
from sqlalchemy.orm import Session
from core.config.database import get_db, StudentModel
from schemas.names import NamesSchema, ResponseNamesSchema




router = APIRouter(prefix="/api/v1",tags=["NAME"])


@router.get("/names",response_model=List[ResponseNamesSchema],status_code=status.HTTP_200_OK)
async def names_list(search: Optional[str] = Query(None, description="searching names"),db:Session =Depends(get_db)):
    return db.query(StudentModel).all()


@router.post("/names",response_model=ResponseNamesSchema,status_code=status.HTTP_201_CREATED)
async def names_create(request:NamesSchema,db:Session =Depends(get_db)):
    student_obj = StudentModel(name=request.name)
    db.add(student_obj)
    db.commit()
    db.refresh(student_obj)
    return student_obj


@router.get("/names/{item_id}",response_model=ResponseNamesSchema,status_code=status.HTTP_200_OK)
async def names_detail(item_id: int = Path(description="something cool"),db:Session =Depends(get_db)):
    student_obj = db.query(StudentModel).filter(StudentModel.id == item_id).one_or_none()
    
    if not student_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="item not found")
    return student_obj



@router.put("/names/{item_id}",response_model=ResponseNamesSchema,status_code=status.HTTP_200_OK)
async def names_update(item_id: int, request:NamesSchema,db:Session =Depends(get_db)):
    student_obj = db.query(StudentModel).filter(StudentModel.id == item_id).one_or_none()
    
    if not student_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="item not found")
    student_obj.name = request.name
    db.commit()
    db.refresh(student_obj)
    return student_obj


@router.delete("/names/{item_id}")
async def names_delete(item_id: int,db:Session =Depends(get_db)):
    student_obj = db.query(StudentModel).filter(StudentModel.id == item_id).one_or_none()
    
    if not student_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="item not found")
    db.delete(student_obj)
    db.commit()
    return JSONResponse({"detail": "item removed successfully"}, status_code=status.HTTP_200_OK)


