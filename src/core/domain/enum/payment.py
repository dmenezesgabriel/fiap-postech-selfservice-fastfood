import enum


class PaymentStatusEnum(enum.Enum):
    captured = "CAPTURED"
    declined = "DECLINED"
    pending = "PENDING"
