from pydantic import BaseModel


class FullName(BaseModel):
    first_name: str
    last_name: str

    def __init__(self, first_name: str, last_name: str):
        super().__init__(
            first_name=first_name.lower(),
            last_name=last_name.lower()
        )

    @property
    def capitalized_first_name(self):
        return self.first_name.capitalize()

    @property
    def capitalized_last_name(self):
        return self.last_name.capitalize()

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
