from typing import Literal


def update_tema_status(
    tema_id: int,
    status: Literal["AKTIV", "INAKTIV"] = "INAKTIV",
):
    return (
        "-- Gjør tema inaktivt"
        + "\n"
        + "UPDATE ia_sak_kartlegging_tema"
        + "\n"
        + f"SET status = '{status}'"
        + "\n"
        + f"WHERE tema_id = {tema_id};"
        + "\n"
    )
