import razorpay
from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from ..database import SessionLocal
from app.database import get_db
from ..models import Application

router = APIRouter(prefix="/api", tags=["Payment"])

# Razorpay test keys (replace with your test account keys)
RAZORPAY_KEY_ID = "rzp_test_1234567890"
RAZORPAY_KEY_SECRET = "your_secret_key"

client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))


@router.post("/create_order")
def create_order(amount: int = Form(...)):
    order = client.order.create({
        "amount": amount * 100,  
        "currency": "INR",
        "payment_capture": 1
    })
    return {"order_id": order["id"], "amount": order["amount"], "currency": order["currency"]}


@router.post("/verify_payment")
def verify_payment(
    payment_id: str = Form(...),
    application_id: int = Form(...),
    db: Session = Depends(get_db)
):
    app = db.query(Application).filter(Application.id == application_id).first()

    if not app:
        return {"error": "Application not found"}

    app.payment_id = payment_id
    app.payment_status = 1
    db.commit()

    return {"message": "Payment verified successfully"}

