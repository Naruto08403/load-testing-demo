from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.routes import censusRouter, memberRouter
from fastapi.middleware.cors import CORSMiddleware
description = """
## Census API
This api tends to process **Census Data.**

This contain 2 tables, **census_records** and **family_members**.

The census_records table contains the record of the family head in that household. 
This could be Father, the Mother or any member of the family for any cases.

The census_record table has a relationship with the family_members table
for a census_record may have no or 1 or more family members.

##Functions##



"""

app = FastAPI(title="ChimichangApp",
    description=description,
    summary="Deadpool's favorite app. Nuff said.",
    version="0.0.1",
    contact={
        "name": "Load Testing Demo",
        "url": "https://github.com/Naruto08403/load-testing-demo",
        "email": "ruelawayan24@gmail.com",
    })
    
allow_origins = ['http://localhost:8080']

app.add_middleware(
    CORSMiddleware,
    allow_origins = allow_origins,
    allow_credentials=True,
    allow_methods=["GET","POST","PUT","DELETE","PATCH"],
    allow_headers=["X-Requested-With","Content-Type"]
)

@app.get('/')
async def get_homepage():
    return RedirectResponse ('/docs')

app.include_router(censusRouter)
app.include_router(memberRouter)


