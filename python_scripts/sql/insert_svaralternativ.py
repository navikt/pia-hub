def insert_svaralternativ(
    svaralternativ_tekst: str,
    spørsmål_id: str,
    svaralternativ_id: str,
):
    return (
        "INSERT INTO ia_sak_kartlegging_svaralternativer (svaralternativ_id, sporsmal_id, svaralternativ_tekst)"
        + "\n"
        + f"VALUES ('{svaralternativ_id}', '{spørsmål_id}', '{svaralternativ_tekst}');"
        + "\n"
    )
