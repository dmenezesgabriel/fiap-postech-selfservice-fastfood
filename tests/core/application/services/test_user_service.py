from unittest.mock import Mock

import pytest
from src.core.application.ports.user_repository import UserRepositoryInterface
from src.core.application.services.user import UserService
from src.core.domain.entities.user import User


class TestUserService:
    @pytest.fixture
    def user_service(self):
        user_repository = Mock(spec=UserRepositoryInterface)
        return UserService(user_repository)

    def test_get_by_id_success(self, user_service):
        user_id = 1
        user_data = {
            "id": user_id,
            "email": "test@example.com",
            "password": "123",
        }
        expected_user = User(**user_data)
        user_service.user_repository.get_by_id.return_value = expected_user

        result = user_service.get_by_id(user_id)
        assert result == expected_user

    def test_get_all_success(self, user_service):
        user_data = [
            {"id": 1, "email": "test@example.com", "password": "123"},
            {"id": 2, "email": "test2@example.com", "password": "123"},
        ]
        expected_users = [User(**data) for data in user_data]
        user_service.user_repository.get_all.return_value = expected_users

        result = user_service.get_all()
        assert result == expected_users

    def test_create_success(self, user_service):
        user_data = {"id": 1, "email": "test@example.com", "password": "123"}
        user_to_create = User(**user_data)
        user_service.user_repository.create.return_value = user_to_create

        result = user_service.create(user_to_create)
        assert result == user_to_create

    def test_update_success(self, user_service):
        user_data = {"id": 1, "email": "test@example.com", "password": "123"}
        user_to_update = User(**user_data)
        user_service.user_repository.update.return_value = user_to_update

        result = user_service.update(user_to_update)
        assert result == user_to_update

    def test_delete_success(self, user_service):
        user_id = 1
        user_service.user_repository.delete.return_value = True

        result = user_service.delete(user_id)
        assert result is True

    def test_get_by_id_failure(self, user_service):
        user_id = 1
        user_service.user_repository.get_by_id.side_effect = Exception(
            "User not found"
        )

        with pytest.raises(Exception) as exc_info:
            user_service.get_by_id(user_id)

        assert str(exc_info.value) == "User not found"

    def test_delete_failure(self, user_service):
        user_id = 1
        user_service.user_repository.delete.side_effect = Exception(
            "Deletion failed"
        )

        with pytest.raises(Exception) as exc_info:
            user_service.delete(user_id)

        assert str(exc_info.value) == "Deletion failed"
