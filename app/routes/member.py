from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from app.models import session,Records,FamilyMembers
from app.schemas import MemberResponse,MembersBase,RecordBase,RecordResponse

memberRouter = APIRouter(prefix='/api/members',tags=['Members Endpoints'])

@memberRouter.get('/<record_id>',response_model=list[MemberResponse])
async def get_members_of_a_records(record_id:int):
    db = session() 
    record = db.query(Records).where(Records.id==record_id).first()
    if not record:
        raise HTTPException(status_code=404,detail="Record not Found")
    db = session() 
    
    db.close()
    return record.members

@memberRouter.get('/<member_id>',response_model=list[MemberResponse])
async def get_specific_members_of_a_record(member_id:int):
    db = session()
    record = db.query(FamilyMembers).where(FamilyMembers.id==member_id).first()
    if not record:
        raise HTTPException(status_code=404,detail="Record not Found")
    db = session() 
    db.close()
    return record


@memberRouter.post('/',response_model=MemberResponse)
def add_member_record(data:MembersBase):
    db = session()
    new_record = FamilyMembers(name=data.name,age=data.age,civil_status=data.civil_status)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    db.close()
    return new_record



@memberRouter.delete('/<id>',response_model=list[MemberResponse])
async def delete_a_member(id:int):
    db = session()
    record = db.query(FamilyMembers).where(FamilyMembers.id==id).first()
    if not record:
        raise HTTPException(status_code=404,detail="Record not Found")
    
    db.delete(record)
    db.commit()
    db.close()
    return {"message":"Successfully deleted"}

@memberRouter.put('/',response_model=MemberResponse)
def update_member_record(id:int,data:MembersBase):
    db = session()
    record = db.query(FamilyMembers).where(FamilyMembers.id==id).first()
    if not record:
        raise HTTPException(status_code=404,detail="Record not Found")
    new_record = Records(name=data.name,age=data.age,civil_status=data.civil_status)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    db.close()
    return new_record
    
