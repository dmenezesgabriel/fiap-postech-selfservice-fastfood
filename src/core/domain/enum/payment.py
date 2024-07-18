import enum


class PaymentStatusEnum(enum.Enum):
    CAPTURED = "CAPTURED"
    DECLINED = "DECLINED"
    PENDING = "PENDING"
