from .activity import *


class LegymActivities:
    """Manager of Legym activities."""

    def __init__(self, activities: list[dict]) -> None:
        """Parse each activity."""
        self.__activities = [LegymActivity(activity) for activity in activities]

    def __str__(self) -> str:
        return "\n".join([str(activity) for activity in self.__activities])

    def __repr__(self) -> str:
        return "\n".join([str(activity) for activity in self.__activities])

    def search(
        self,
        id: str = "",
        code: str = "",
        name: str = "",
        state: ActivityState = ActivityState.unknown,
    ) -> list[LegymActivity]:
        """Get activity by specified rule.

        Args:
            id: Activity ID, default to "".
            code: Activity code, default to "".
            name: Activity name, default to "".
            state: Activity state, default to `ActivityState.unknown`.

        Returns:
            List of Legym activities under specified rules.
        """
        results = self.__activities.copy()

        if id != "":
            results = list(filter(lambda act: act.id == id, results))
        if code != "":
            results = list(filter(lambda act: act.code == code, results))
        if name != "":
            results = list(filter(lambda act: act.name.find(name) != -1, results))
        if state != ActivityState.unknown:
            results = list(filter(lambda act: act.state == state, results))

        return results
