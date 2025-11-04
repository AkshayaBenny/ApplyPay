from fastapi import APIRouter,Depends
from app.models import Application, Base
from app.schemas import ApplicationCreate
from sqlalchemy.orm import Session
from app.database import get_db
from datetime import datetime

router = APIRouter()

@router.post("/create")
def create_application(application: ApplicationCreate, db: Session =  Depends(get_db)):
    # Convert DOB from DD-MM-YYYY to datetime
    dob_obj = datetime.strptime(application.dob, "%d-%m-%Y")

    is_email_exist = db.query(Application).filter(Application.email == application.email).first()
    if is_email_exist:
        return {"Email Already Exist"}

    new_app = Application(
        name=application.name,
        email=application.email,
        phone=application.phone,
        gender=application.gender,
        dob=dob_obj,
        bio=application.bio,
        resume_path=application.resume_path,
        payment_id=application.payment_id,
        payment_status=application.payment_status
    )
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    return True

