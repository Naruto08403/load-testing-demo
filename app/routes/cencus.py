from fastapi import APIRouter,HTTPException
from fastapi.responses import RedirectResponse
from app.models import session,Records,FamilyMembers
from app.schemas import MemberResponse,MembersBase,RecordBase,RecordResponse

censusRouter = APIRouter(prefix='/api/records',tags=['Census Endpoints'])

@censusRouter.get('/',response_model=list[RecordResponse])
async def get_records():
    db = session() 
    records = db.query(Records)
    db.close()
    return records

@censusRouter.get('/<id>',response_model=RecordResponse)
async def get_members_of_a_record(id:int):
    db = session()
    record = db.query(Records).where(Records.id==id).first()
    if not record:
        raise HTTPException(status_code=404,detail="Record not Found")
    db = session() 
    
    db.close()
    return record


@censusRouter.post('/',response_model=RecordResponse)
async def add_record(data):
    print(data)
    db = session()
    new_record = Records(family_head=data.family_head,age=data.age,civil_status=data.civil_status,address=data.address)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    db.close()
    db = session()
    if data.members:
        for member in data.members:
            new_member = FamilyMembers(record_id=new_record.id,name=member.name,age=member.age,civil_status=member.civil_status)
            db.add(new_member)
    
    db.commit()
    db.close()
    return new_record



@censusRouter.delete('/<id>',response_model=list[MemberResponse])
async def delete_a_record(id:int):
    db = session()
    record = db.query(Records).where(Records.id==id).first()
    if not record:
        raise HTTPException(status_code=404,detail="Record not Found")
    # delete all members of that record 
    for member in record.members:
        db.delete(member)
    db.delete(record)
    db.commit()

    
    db.close()
    return {"message":"Successfully deleted"}

@censusRouter.put('/',response_model=RecordResponse)
def update_record(id:int,data:RecordBase):
    db = session()
    record = db.query(Records).where(Records.id==id).first()
    if not record:
        raise HTTPException(status_code=404,detail="Record not Found")
    new_record = Records(family_head=data.family_head,age=data.age,civil_status=data.civil_status,address=data.address)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    db.close()
    db = session()
    if data.members:
        for member in data.members:
            new_member = FamilyMembers(record_id=new_record.id,name=member.name,age=member.age,civil_status=member.civil_status)
            db.add(new_member)
    
    db.commit()
    db.close()
    return new_record
    
