"""Assertion concern module.

Note: most of validation is done by pydantic, so this may not be needed unless
you want to add custom validation or remove pydantic.

Usage example:

from src.core.domain.base.assertion_concern import AssertionConcern

class FullName(AssertionConcern):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name=first_name, last_name=last_name)

    def __eq__(self, other):
        if isinstance(other, FullName):
            return (
                self.first_name == other.first_name and
                self.last_name == other.last_name
            )
        return False

    def __repr__(self):
        return (
            f"FullName(first_name={self.first_name}, " +
            "last_name={self.last_name})"
        )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def _validate_invariants(self):
        self._assert_argument_length(
            self.first_name,
            2,
            255,
            "First name must be between 2 and 255 characters."
        )
        self._assert_argument_length(
            self.last_name,
            2,
            255,
            "Last name must be between 2 and 255 characters."
        )

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def initials(self):
        return f"{self.first_name[0]}{self.last_name[0]}"

    @property
    def last_initial(self):
        return self.last_name[0]

"""

from pydantic import BaseModel, ConfigDict, ValidationError, validator


class AssertionConcern(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        validate_assignment=True,
        validate_all=True,
        validate_assignment=True,
        validate_all=True,
    )

    @validator("*", pre=True)
    def validate(cls, value, field):
        """Validate all fields."""
        if value is None:
            raise ValidationError("value cannot be None")
        return value

    def __init__(self, *args, **kwargs):
        """Initialize instance."""
        super().__init__(*args, **kwargs)
        self._validate_invariants()

    def _validate_invariants(self):
        """Validate invariants."""
        pass

    def _assert_argument_not_none(self, value, message):
        """Assert argument not none."""
        if value is None:
            raise ValueError(message)

    def _assert_argument_is_true(self, value, message):
        """Assert argument is true."""
        if not value:
            raise ValueError(message)

    def _assert_argument_is_false(self, value, message):
        """Assert argument is false."""
        if value:
            raise ValueError(message)

    def _assert_state_not_none(self, value, message):
        """Assert state not none."""
        if value is None:
            raise ValueError(message)

    def _assert_argument_length(self, value, min_length, max_length, message):
        """Assert argument length."""
        if value is None:
            raise ValueError(message)
        if len(value) < min_length or len(value) > max_length:
            raise ValueError(message)

    def _assert_argument_greater_than(self, value, min_value, message):
        """Assert argument greater than."""
        if value is None or value <= min_value:
            raise ValueError(message)

    def _assert_argument_greater_or_equal_than(
            self, value, min_value, message):
        """Assert argument greater or equal than."""
        if value is None or value < min_value:
            raise ValueError(message)

    def _assert_argument_less_than(self, value, max_value, message):
        """Assert argument less than."""
        if value is None or value >= max_value:
            raise ValueError(message)
