def insert_spørsmål_tema_relasjon(spørsmål_id: str, tema_id: int, tema_navn: str):
    if len(spørsmål_id) != 36:
        raise Exception("et spørsmål sin id (uuid) må være 36 tegn lang")
    if tema_id <= 0:
        raise Exception("tema_id må være positiv")
    if tema_navn == "":
        raise Exception("tema_navn kan ikke være tom")
    return (
        f"-- Knytt tema til spørsmål -> '{tema_navn}'"
        + "\n"
        + "INSERT INTO ia_sak_kartlegging_tema_til_spørsmål (tema_id, sporsmal_id)"
        + "\n"
        + f"VALUES ({tema_id}, '{spørsmål_id}');"
        + "\n"
    )
