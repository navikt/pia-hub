def insert_spørsmål(spørsmål_id: str, spørsmål_tekst: str, flervalg: bool):
    if len(spørsmål_id) != 36:
        raise Exception("et spørsmål sin id (uuid) må være 36 tegn lang")
    if spørsmål_tekst == "":
        raise Exception("Et spørsmål kan ikke være tomt")
    return (
        "INSERT INTO ia_sak_kartlegging_sporsmal (sporsmal_id, sporsmal_tekst, flervalg)"
        + "\n"
        + f"VALUES ('{spørsmål_id}','{spørsmål_tekst.strip()}',{str(flervalg).lower()});"
        + "\n"
    )
