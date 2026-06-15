from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routers import teams, groups, matches, stats, stadiums
from seed import seed


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    seed()
    yield


app = FastAPI(title="World Cup 2026 API", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(teams.router)
app.include_router(groups.router)
app.include_router(matches.router)
app.include_router(stats.router)
app.include_router(stadiums.router)


@app.get("/")
def root():
    return {"name": "World Cup 2026 API", "version": "1.0.0", "endpoints": "/docs"}
