from typing import List

from src.common.dto.order_dto import KitchenResponseDTO, CreateOrderDTO
from src.common.interfaces.order_gateway import OrderGatewayInterface
from src.common.interfaces.order_repository import OrderRepositoryInterface
from src.core.domain.entities.order import OrderDetailEntity
import httpx
import json


class OrderGateway(OrderGatewayInterface):
    def __init__(self, order_repository: OrderRepositoryInterface):
        self.order_repository = order_repository

    def create(self, createOrderDTO: CreateOrderDTO) -> KitchenResponseDTO:
        create_order_json = createOrderDTO.model_dump_json()
        ## TODO: remover url estática
        kitchen_response_json = httpx.post('http://localhost:8081/kitchen/v1/orders/', json=json.loads(create_order_json)).json()

        return KitchenResponseDTO(**kitchen_response_json)

    def list_all(self) -> List[OrderDetailEntity]:
        return self.order_repository.list_all()

    def update_order_status(self, order_id: int, order_status: str):
        return self.order_repository.update_order_status(order_id, order_status)
