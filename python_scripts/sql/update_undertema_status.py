from typing import Literal


def update_undertema_status(
    undertema_id: int, status: Literal["AKTIV", "INAKTIV"] = "INAKTIV"
):
    return (
        "-- Gjør undertema inaktivt"
        + "\n"
        + "UPDATE ia_sak_kartlegging_undertema"
        + "\n"
        + f"SET status = '{status}'"
        + "\n"
        + f"WHERE undertema_id = {undertema_id};"
        + "\n"
    )
