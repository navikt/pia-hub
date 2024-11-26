from typing import Literal


def insert_tema(
    temanavn: str,
    tema_id: int,
    spørreundersøkelse_type: Literal["Behovsvurdering", "Evaluering"],
    rekkefølge: int,
) -> str:
    return (
        f"-- Nytt tema -> '{temanavn}'"
        + "\n"
        + "INSERT INTO ia_sak_kartlegging_tema (tema_id, navn, status, rekkefolge, type)"
        + "\n"
        + f"VALUES ({tema_id}, '{temanavn}', 'AKTIV', {rekkefølge}, '{spørreundersøkelse_type}');"
        + "\n"
    )
