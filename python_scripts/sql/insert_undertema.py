def insert_undertema(
    undertema_id: int,
    undertemanavn: str,
    tema_id: int,
    obligatorisk: bool,
    temanavn: str,
    rekkefølge: int,
) -> str:
    return (
        f"-- Nytt undertema -> '{temanavn}' : '{undertemanavn}'"
        + "\n"
        + "INSERT INTO ia_sak_kartlegging_undertema (undertema_id, navn, status, rekkefolge, tema_id, obligatorisk)"
        + "\n"
        + f"VALUES ({undertema_id}, '{undertemanavn}', 'AKTIV', {rekkefølge}, {tema_id}, {str(obligatorisk).lower()});"
        + "\n"
    )
