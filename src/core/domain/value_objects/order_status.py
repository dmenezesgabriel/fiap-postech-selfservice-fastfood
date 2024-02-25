from enum import Enum, unique


@unique
class OrderStatus(Enum):
    RECEIVED = "Recebido"
    DOING = "Em Preparação"
    READY = "Pronto"

    def __str__(self) -> str:
        return self.value
