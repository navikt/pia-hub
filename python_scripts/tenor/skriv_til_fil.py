import csv

from models.tenor.Virksomhet import Virksomhet
from tenor.insert_virksomhet import insert_virksomhet
from tenor.insert_virksomhet_naringsundergrupper import (
    insert_virksomhet_naringsundergrupper,
)


def ansatteTilEnum(antall_ansatte):
    if antall_ansatte <= 25:
        return "LITEN"
    elif antall_ansatte <= 100:
        return "MEDIUM"
    elif antall_ansatte <= 10000:
        return "STOR"
    else:
        return "ENORM"


def skriv_til_fil(
    output_filename_SQL: str,
    output_filename_fiktive_orgnr_liste_csv: str,
    nye_virksomheter: list[Virksomhet],
):
    with (
        open(output_filename_SQL, "w") as sql_file,
        open(output_filename_fiktive_orgnr_liste_csv, "w") as csv_file,
    ):
        csv_builder = csv.writer(csv_file)
        csv_builder.writerow(["orgnr", "sektor", "primærnæring", "størrelse"])

        for indeks, ny_virksomhet in enumerate(nye_virksomheter):
            sektor = (indeks % 3) + 1
            størrelse = ansatteTilEnum(ny_virksomhet.antall_ansatte)

            csv_builder.writerow(
                [
                    ny_virksomhet.orgnummer,
                    sektor,
                    ny_virksomhet.næringskode,
                    størrelse,
                ]
            )

            sql_file.write(insert_virksomhet(ny_virksomhet))
            sql_file.write("\n")
            sql_file.write(
                insert_virksomhet_naringsundergrupper(
                    ny_virksomhet.orgnummer, ny_virksomhet.næringskode
                )
            )
            sql_file.write("\n")

    return len(nye_virksomheter)
