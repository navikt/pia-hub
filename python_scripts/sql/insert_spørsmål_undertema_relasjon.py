def insert_spørsmål_undertema_relasjon(
    undertema_navn: str, undertema_id: int, spørsmål_id: str, rekkefølge: int
):
    return (
        f"-- Knytt spørsmål til undertema -> '{undertema_navn}'"
        + "\n"
        + "INSERT INTO ia_sak_kartlegging_sporsmal_til_undertema (undertema_id, sporsmal_id,rekkefolge)"
        + "\n"
        + f"VALUES ({undertema_id}, '{spørsmål_id}', {rekkefølge});"
        + "\n"
    )
