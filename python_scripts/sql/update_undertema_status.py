from typing import Literal


def update_undertema_status(
    undertema_id: int, status: Literal["AKTIV", "INAKTIV"] = "INAKTIV"
):
    if undertema_id <= 0:
        raise Exception("Et undertema sin id må være et positivt tall")
    if status not in ["AKTIV", "INAKTIV"]:
        raise ValueError("status must be either 'AKTIV' or 'INAKTIV'")
    return (
        f"-- Gjør undertema {status.lower()}t"
        + "\n"
        + "UPDATE ia_sak_kartlegging_undertema"
        + "\n"
        + f"SET status = '{status}'"
        + "\n"
        + f"WHERE undertema_id = {undertema_id};"
        + "\n"
    )
