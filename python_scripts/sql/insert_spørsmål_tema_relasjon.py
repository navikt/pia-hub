def insert_spørsmål_tema_relasjon(spørsmål_id: str, tema_id: int, tema_navn: str):
    return (
        f"-- Knytt tema til spørsmål -> '{tema_navn}'"
        + "\n"
        + "INSERT INTO ia_sak_kartlegging_tema_til_spørsmål (tema_id, sporsmal_id)"
        + "\n"
        + f"VALUES ({tema_id}, '{spørsmål_id}');"
        + "\n"
    )
