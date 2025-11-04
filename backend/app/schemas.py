from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ApplicationBase(BaseModel):
    name: str
    email: str
    phone: int
    gender: str
    dob: str  # we accept string from frontend, convert later
    bio: str
    resume_path: str
    payment_id: Optional[int] = None
    payment_status: Optional[int] = 0

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationResponse(ApplicationBase):
    id: int
    dob: datetime  # datetime in response

    class Config:
        orm_mode = True

