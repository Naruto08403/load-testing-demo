from sqlalchemy import Column,String,Integer,create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base 

DATABASE_URL = 'sqlite:///./test.db'

engine = create_engine(DATABASE_URL)

session = sessionmaker(autoflush=False,bind=engine)
Base = declarative_base()

class Records(Base):
    __tablename__ = 'census_records'

    id = Column(Integer,primary_key=True, index=True)
    family_head = Column(String(100),nullable=False)
    age = Column(Integer,nullable =False)
    address = Column(String(100),nullable=False)
    civil_status = Column(String(100),nullable = False)

    members = relationship("FamilyMembers",back_populates="member",lazy="joined")

class FamilyMembers(Base):
    __tablename__ = 'family_members'

    id = Column(Integer,primary_key=True,index=True)
    name  = Column(String(100),nullable=False)
    age = Column(Integer,nullable =False)
    civil_status = Column(String(100),nullable = False)

    record_id = Column(Integer,ForeignKey("census_records.id"))
    member = relationship("Records",back_populates="members")

Base.metadata.create_all(bind=engine)

