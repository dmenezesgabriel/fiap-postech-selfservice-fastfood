import pytest
from src.core.domain.entities.user import User


class TestUser:
    @pytest.mark.parametrize(
        "email, password",
        [
            ("test@example.com", "password123"),
        ],
    )
    def test_user_creation_success(self, email, password):
        user = User(email=email, password=password)
        assert user.email == email
        assert user.password == password

    @pytest.mark.parametrize(
        "email, password",
        [
            (123, "password123"),
            ("test@example.com", 123),
            (123, 123),
        ],
    )
    def test_user_creation_fail(self, email, password):
        with pytest.raises(ValueError):
            User(email=email, password=password)
