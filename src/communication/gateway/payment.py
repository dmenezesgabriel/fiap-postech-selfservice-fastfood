from typing import List

from src.common.dto.payment_dto import CreatePaymentDTO
from src.common.interfaces.payment_gateway import PaymentGatewayInterface
from src.common.interfaces.payment_repository import PaymentRepositoryInterface
from src.core.domain.entities.payment import PaymentEntity
import json
import httpx


class PaymentGateway(PaymentGatewayInterface):
    def __init__(self, payment_repository: PaymentRepositoryInterface) -> None:
        self.payment_repository = payment_repository

    def get_many_by_user_id(self, user_id: int) -> List[PaymentEntity]:
        return self.payment_repository.get_many_by_user_id(user_id=user_id)

    def get_by_id(self, payment_id: int) -> PaymentEntity:
        return self.payment_repository.get_by_id(payment_id=payment_id)

    def get_by_order_id(self, order_id: int) -> PaymentEntity:
        return self.payment_repository.get_by_order_id(order_id=order_id)

    def create(self, create_payment_dto: CreatePaymentDTO) -> bool:
        try:
            url = 'http://23.23.36.50:8000/'
            payment_json = json.loads(create_payment_dto.model_dump_json())
            payment_response = httpx.post('http://23.23.36.50:8000/', json=payment_json).json()
            print(payment_response)
            return True
        except Exception as error:
            print(error)
            return False

    def update(self, payment: PaymentEntity) -> PaymentEntity:
        return self.payment_repository.update(payment=payment)

    def delete(self, payment_id: int) -> None:
        return self.payment_repository.delete(payment_id=payment_id)
