from typing import Literal


def insert_tema(
    temanavn: str,
    tema_id: int,
    spørreundersøkelse_type: Literal["Behovsvurdering", "Evaluering"],
    rekkefølge: int,
) -> str:
    if temanavn == "":
        raise Exception("Et tema må ha et navn")
    if spørreundersøkelse_type not in ["Behovsvurdering", "Evaluering"]:
        raise Exception("Ugyldig type for spørreundersøkelse")
    if tema_id <= 0:
        raise Exception("Et tema sin id må være et positivt tall")
    if rekkefølge <= 0:
        raise Exception("rekkefølge burde starte fra 1")
    return (
        f"-- Nytt tema -> '{temanavn}'"
        + "\n"
        + "INSERT INTO ia_sak_kartlegging_tema (tema_id, navn, status, rekkefolge, type)"
        + "\n"
        + f"VALUES ({tema_id}, '{temanavn}', 'AKTIV', {rekkefølge}, '{spørreundersøkelse_type}');"
        + "\n"
    )
