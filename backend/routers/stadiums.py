from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Stadium
from schemas import StadiumOut

router = APIRouter(prefix="/stadiums", tags=["stadiums"])


@router.get("", response_model=list[StadiumOut])
def list_stadiums(db: Session = Depends(get_db)):
    return db.query(Stadium).order_by(Stadium.name).all()
