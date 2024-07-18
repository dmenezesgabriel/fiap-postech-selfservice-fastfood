from fastapi import APIRouter

from src.communication.controller.payment import PaymentController
from src.external.database.sqlalchemy.repositories.payment import (
    PaymentRepository,
)

payment_repository = PaymentRepository()
payment_controller = PaymentController(payment_repository)

router = APIRouter(prefix="/payments", tags=["payments"])