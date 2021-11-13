from typing import NamedTuple


class UsernameAndPassword(NamedTuple):
    username: str
    password: str


class UserCredentials(NamedTuple):
    name: str
    email: str