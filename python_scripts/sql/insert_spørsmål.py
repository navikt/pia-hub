def insert_spørsmål(spørsmål_id: str, spørsmål_tekst: str, flervalg: bool):
    return (
        "INSERT INTO ia_sak_kartlegging_sporsmal (sporsmal_id, sporsmal_tekst, flervalg)"
        + "\n"
        + f"VALUES ('{spørsmål_id}','{spørsmål_tekst.strip()}',{str(flervalg).lower()});"
        + "\n"
    )
