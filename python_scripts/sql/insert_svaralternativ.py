def insert_svaralternativ(
    spørsmål_id: str,
    svaralternativ_id: str,
    svaralternativ_tekst: str,
):
    if len(spørsmål_id) != 36:
        raise Exception("et spørsmål sin id (uuid) må være 36 tegn lang")
    if len(svaralternativ_id) != 36:
        raise Exception("et svaralternativ sin id (uuid) må være 36 tegn lang")
    if svaralternativ_tekst == "":
        raise Exception("Et svaralternativ må ha noe tekst")
    return (
        "INSERT INTO ia_sak_kartlegging_svaralternativer (svaralternativ_id, sporsmal_id, svaralternativ_tekst)"
        + "\n"
        + f"VALUES ('{svaralternativ_id}', '{spørsmål_id}', '{svaralternativ_tekst}');"
        + "\n"
    )
