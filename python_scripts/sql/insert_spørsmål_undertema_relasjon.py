def insert_spørsmål_undertema_relasjon(
    undertema_navn: str, undertema_id: int, spørsmål_id: str, rekkefølge: int
):
    if len(spørsmål_id) != 36:
        raise Exception("et spørsmål sin id (uuid) må være 36 tegn lang")
    if undertema_id <= 0:
        raise Exception("undertema_id må være positiv")
    if undertema_navn == "":
        raise Exception("undertema_navn kan ikke være tom")
    if rekkefølge <= 0:
        raise Exception("rekkefølge burde starte fra 1")
    return (
        f"-- Knytt spørsmål til undertema -> '{undertema_navn}'"
        + "\n"
        + "INSERT INTO ia_sak_kartlegging_sporsmal_til_undertema (undertema_id, sporsmal_id,rekkefolge)"
        + "\n"
        + f"VALUES ({undertema_id}, '{spørsmål_id}', {rekkefølge});"
        + "\n"
    )
