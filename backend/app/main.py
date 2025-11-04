from fastapi import FastAPI
from .database import Base, engine
from .routes import application, payment, admin

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ApplyPay API")

# Include routes
app.include_router(application.router)
app.include_router(payment.router)
app.include_router(admin.router)

@app.get("/")
def root():
    return {"message": "ApplyPay Backend is Running"}
