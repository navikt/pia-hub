def insert_undertema(
    undertema_id: int,
    undertemanavn: str,
    tema_id: int,
    obligatorisk: bool,
    rekkefølge: int,
    temanavn: str = "",
) -> str:
    if undertema_id <= 0:
        raise Exception("Et undertema sin id må være et positivt tall")
    if undertemanavn == "":
        raise Exception("Et undertema må ha et navn")
    if tema_id <= 0:
        raise Exception("Et tema sin id må være et positivt tall")
    if rekkefølge <= 0:
        raise Exception("rekkefølge burde starte fra 1")
    return (
        f"-- Nytt undertema -> '{temanavn}' : '{undertemanavn}'"
        + "\n"
        + "INSERT INTO ia_sak_kartlegging_undertema (undertema_id, navn, status, rekkefolge, tema_id, obligatorisk)"
        + "\n"
        + f"VALUES ({undertema_id}, '{undertemanavn}', 'AKTIV', {rekkefølge}, {tema_id}, {str(obligatorisk).lower()});"
        + "\n"
    )
