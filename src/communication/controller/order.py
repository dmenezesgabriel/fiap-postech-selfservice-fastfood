from src.common.dto.order_dto import CreateOrderDTO
from src.common.interfaces.order_repository import OrderRepositoryInterface
from src.common.interfaces.product_repository import ProductRepositoryInterface
from src.communication.gateway.order import OrderGateway
from src.communication.gateway.product import ProductGateway
from src.core.use_cases.order import OrderUseCase


class OrderController:
    def __init__(
        self,
        order_repository: OrderRepositoryInterface,
        product_repository: ProductRepositoryInterface,
    ):
        self.order_repository = order_repository
        self.product_repository = product_repository

    def create_order(self, order: CreateOrderDTO):
        order_gateway = OrderGateway(self.order_repository)
        product_gateway = ProductGateway(self.product_repository)
        return OrderUseCase.create(
            order=order,
            order_gateway=order_gateway,
            product_gateway=product_gateway,
        )

    def list_orders(self):
        order_gateway = OrderGateway(self.order_repository)
        return OrderUseCase.list_all(order_gateway=order_gateway)
