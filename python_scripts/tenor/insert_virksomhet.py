from models.tenor.Virksomhet import Virksomhet


def insert_virksomhet(virksomhet: Virksomhet):
    separator = ", "
    adresse = separator.join(
        f'"{adresse_line}"' for adresse_line in virksomhet.adresse_lines
    )
    return (
        f"INSERT INTO public.virksomhet "
        f"(orgnr, land, landkode, postnummer, poststed, kommune, kommunenummer, navn, adresse, status, oppstartsdato) "
        f"VALUES ('{virksomhet.orgnummer}', '{virksomhet.land}', '{virksomhet.landkode}', '{virksomhet.postnummer}', '{virksomhet.poststed}', '{virksomhet.kommune}', '{virksomhet.kommunenummer}', "
        f"'{virksomhet.navn}', '{{{adresse}}}', "
        f"'AKTIV', '{virksomhet.oppstartsdato}') ON CONFLICT DO NOTHING;"
    )
