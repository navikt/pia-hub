from typing import Literal


def update_tema_status(
    tema_id: int,
    status: Literal["AKTIV", "INAKTIV"] = "INAKTIV",
):
    if tema_id <= 0:
        raise Exception("Et tema sin id må være et positivt tall")
    if status not in ["AKTIV", "INAKTIV"]:
        raise ValueError("status must be either 'AKTIV' or 'INAKTIV'")
    return (
        f"-- Gjør tema {status.lower()}t"
        + "\n"
        + "UPDATE ia_sak_kartlegging_tema"
        + "\n"
        + f"SET status = '{status}'"
        + "\n"
        + f"WHERE tema_id = {tema_id};"
        + "\n"
    )
