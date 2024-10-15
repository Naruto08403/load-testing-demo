from pydantic import BaseModel


class MembersBase(BaseModel):
    name:str 
    age:int 
    civil_status:str 

class MemberResponse(BaseModel):
    id:int 
    name:str 
    civil_status:str 
    age:int 

    class Config:
        from_attributes = True


class RecordBase(BaseModel):
    family_head:str 
    age:int
    civil_status:str 
    address:str
    members: list[MembersBase] 

class RecordResponse(BaseModel):
    id:int 
    family_head:str 
    civil_status:str 
    age:int 
    members: list[MemberResponse] = []
    class Config:
        from_attributes = True
