from enum import Enum, unique


@unique
class OrderStatus(Enum):
    RECEIVED = "Recebido"
    DOING = "Em Preparação"
    READY = "Pronto"
    DONE = "Finalizado"

    def __str__(self) -> str:
        return self.value
