from typing import List

from fastapi import APIRouter, HTTPException

from src.common.dto.payment_dto import (
    CreatePaymentDTO,
    PaymentDTO,
    UpdatePaymentDTO,
)
from src.communication.controller.payment import PaymentController
from src.external.database.sqlalchemy.repositories.payment import (
    PaymentRepository,
)

payment_repository = PaymentRepository()
payment_controller = PaymentController(payment_repository)

router = APIRouter(prefix="/payments", tags=["payments"])


@router.get("/user/{user_id}", response_model=List[PaymentDTO])
async def get_many_payments_by_user_id(user_id: int):
    payments = payment_controller.get_many_by_user_id(user_id=user_id)
    return [
        PaymentDTO(
            id=payment.id,
            user_id=payment.user_id,
            order_id=payment.order_id,
            amount=payment.amount,
            provider=payment.provider,
            status=payment.status,
        )
        for payment in payments
    ]


@router.get("/{payment_id}", response_model=PaymentDTO)
async def get_payment_by_id(payment_id: int):
    payment = payment_controller.get_by_id(payment_id=payment_id)
    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return PaymentDTO(
        id=payment.id,
        user_id=payment.user_id,
        order_id=payment.order_id,
        amount=payment.amount,
        provider=payment.provider,
        status=payment.status,
    )


@router.get("/order/{order_id}", response_model=PaymentDTO)
async def get_payment_by_order_id(order_id: int):
    payment = payment_controller.get_by_order_id(order_id=order_id)
    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return PaymentDTO(
        id=payment.id,
        user_id=payment.user_id,
        order_id=payment.order_id,
        amount=payment.amount,
        provider=payment.provider,
        status=payment.status,
    )


@router.post("/", response_model=PaymentDTO)
async def create_payment(payment: CreatePaymentDTO):
    new_payment = payment_controller.create(payment=payment)
    return PaymentDTO(
        id=new_payment.id,
        order_id=new_payment.order_id,
        user_id=new_payment.user_id,
        amount=new_payment.amount,
        provider=new_payment.provider,
        status=new_payment.status,
    )


@router.put("/{payment_id}", response_model=PaymentDTO)
async def update_payment(payment_id: int, payment: UpdatePaymentDTO):
    return payment_controller.update(
        payment_id=payment_id, updated_payment=payment
    )


@router.delete("/{payment_id}")
async def delete_payment(payment_id: int):
    if payment_controller.get_by_id(payment_id) is False:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment_controller.delete(payment_id=payment_id)


@router.post("/webhook")
async def webhook(payment: PaymentDTO):
    pass
