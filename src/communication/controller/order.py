from typing import List

from src.common.dto.order_dto import CreateOrderDTO, OrderResponseDTO
from src.common.interfaces.order_repository import OrderRepositoryInterface
from src.common.interfaces.product_repository import ProductRepositoryInterface
from src.communication.gateway.order import OrderGateway
from src.communication.gateway.product import ProductGateway
from src.core.domain.entities.order import OrderDetailEntity
from src.core.domain.exceptions import NotFoundError
from src.core.domain.value_objects.order_status import check_order_status
from src.core.use_cases.order import OrderUseCase
from src.external.database.sqlalchemy.mappers.order_mapper import OrderMapper


class OrderController:
    def __init__(
            self,
            order_repository: OrderRepositoryInterface,
            product_repository: ProductRepositoryInterface,
    ) -> None:
        self.order_repository = order_repository
        self.product_repository = product_repository

    def create_order(self, order: CreateOrderDTO) -> OrderResponseDTO:
        order_gateway = OrderGateway(self.order_repository)
        product_gateway = ProductGateway(self.product_repository)
        return OrderUseCase.create(
            order_dto=order,
            order_gateway=order_gateway,
            product_gateway=product_gateway,
        )

    def list_orders(self) -> List[OrderResponseDTO]:
        order_gateway = OrderGateway(self.order_repository)
        orders = OrderUseCase.list_all(order_gateway=order_gateway)
        return [OrderMapper.entity_to_order_response_dto(order) for order in orders]

    def update_order_status(self, order_id: int, order_status: str) -> OrderDetailEntity:
        order_gateway = OrderGateway(self.order_repository)

        if not check_order_status(order_status):
            raise NotFoundError("Order status invalid")

        return OrderUseCase.order_status_update(
            order_gateway=order_gateway,
            order_id=order_id,
            order_status=order_status
        )
