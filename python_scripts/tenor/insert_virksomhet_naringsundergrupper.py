def insert_virksomhet_naringsundergrupper(orgnr: str, naringskode: str) -> str:
    return (
        f"INSERT INTO public.virksomhet_naringsundergrupper "
        f" (virksomhet, naringsundergruppe1) "
        f"select id, '{naringskode}' as kode from virksomhet where orgnr='{orgnr}' ON CONFLICT DO NOTHING; "
    )
