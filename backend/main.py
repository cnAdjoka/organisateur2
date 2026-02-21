from fastapi import FastAPI
from database import create_db_and_tables
from routes.heroes import router as hero_router

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(hero_router)

