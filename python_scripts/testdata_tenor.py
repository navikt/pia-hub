import os

from tenor.parse_tenor_fil import parse_tenor_fil
from tenor.skriv_til_fil import skriv_til_fil

if __name__ == "__main__":
    input_folder = "python_scripts/data/tenor"
    output_folder = "python_scripts/db/tenor"

    alle_virksomheter = []
    innleste_orgnr = set()
    duplikater_fjernet = 0

    lag_individuelle_mapper_og_filer = True

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    for fylke in os.listdir(input_folder):
        if fylke == ".DS_Store":
            continue

        if (
            not os.path.exists(f"{output_folder}/{fylke}")
            and lag_individuelle_mapper_og_filer
        ):
            os.mkdir(f"{output_folder}/{fylke}")

        print(f"Antall virksomheter for {fylke}:")
        count = 0

        for næring in os.listdir(f"{input_folder}/{fylke}"):
            if næring == ".DS_Store":
                continue

            if (
                not os.path.exists(f"{output_folder}/{fylke}/{næring}")
                and lag_individuelle_mapper_og_filer
            ):
                os.mkdir(f"{output_folder}/{fylke}/{næring}")

            for filename in os.listdir(f"{input_folder}/{fylke}/{næring}"):
                if filename == ".DS_Store":
                    continue

                import_file = f"{input_folder}/{fylke}/{næring}/{filename}"

                nye_virksomheter = parse_tenor_fil(
                    import_file,
                )
                antall_nye_virksomheter = len(nye_virksomheter)
                print(f" {næring}: {len(nye_virksomheter)}")

                nye_virksomheter = [
                    virksomhet
                    for virksomhet in nye_virksomheter
                    if virksomhet.orgnummer not in innleste_orgnr
                ]

                innleste_orgnr.update(
                    [virksomhet.orgnummer for virksomhet in nye_virksomheter]
                )

                duplikater_fjernet += antall_nye_virksomheter - len(nye_virksomheter)

                count += len(nye_virksomheter)

                if lag_individuelle_mapper_og_filer:
                    skriv_til_fil(
                        f"{output_folder}/{fylke}/{næring}/insert_testvirksomheter.sql",
                        f"{output_folder}/{fylke}/{næring}/testvirksomheter.csv",
                        nye_virksomheter,
                    )

                alle_virksomheter.extend(nye_virksomheter)

        print(f" Totalt: {count}")
        print("---------------")

    if duplikater_fjernet > 0:
        print(f"Duplikater droppet: {duplikater_fjernet}")
