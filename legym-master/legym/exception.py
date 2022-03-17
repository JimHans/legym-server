class LegymException(Exception):
    """Self-defined exception under Legym field."""

    def __init__(self, message: str) -> None:
        """Specify error message.

        Args:
            message: Brief description of exception.
        """
        super().__init__()
        self.__message = message

    def __str__(self) -> str:
        return self.__message

    def __repr__(self) -> str:
        return self.__message

    @property
    def message(self) -> str:
        """Set message as read-only."""
        return self.__message
