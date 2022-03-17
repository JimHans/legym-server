from .user import LegymUser


def login(username: str, password: str) -> LegymUser:
    """Log in Legym account.

    Args:
        username: Legym username.
        password: Legym password.

    Returns:
        LegymUser object representing a user.
    """
    return LegymUser(username, password)
