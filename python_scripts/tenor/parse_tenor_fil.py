import json

from models.tenor.Virksomhet import Virksomhet


def parse_tenor_fil(
    import_filename: str,
) -> list[Virksomhet]:
    nye_virksomheter = []

    with open(import_filename, "r") as tenorTestDataFil:
        json_decode = json.load(tenorTestDataFil)
        for virksomhet in json_decode["dokumentListe"]:
            nye_virksomheter.append(
                Virksomhet(
                    orgnummer=virksomhet.get("organisasjonsnummer"),
                    navn=virksomhet.get("navn"),
                    næringskode=virksomhet.get("naeringKode")[0],
                    kommune=virksomhet.get("forretningsadresse").get("kommune"),
                    postnummer=virksomhet.get("forretningsadresse").get("postnummer"),
                    adresse_lines=[
                        adresse.replace("'", "")
                        for adresse in virksomhet.get("forretningsadresse").get(
                            "adresse"
                        )
                    ],
                    kommunenummer=virksomhet.get("forretningsadresse").get(
                        "kommunenummer"
                    ),
                    poststed=virksomhet.get("forretningsadresse").get("poststed"),
                    landkode=virksomhet.get("forretningsadresse").get("landkode"),
                    land=virksomhet.get("forretningsadresse").get("land"),
                    oppstartsdato=virksomhet.get("registreringsdatoEnhetsregisteret"),
                    antall_ansatte=virksomhet.get("antallAnsatte"),
                )
            )
    return nye_virksomheter
