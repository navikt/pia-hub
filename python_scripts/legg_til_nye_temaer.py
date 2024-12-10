from typing import Literal

from models.spørreundersøkelse.Spørsmål import Spørsmål
from models.spørreundersøkelse.Tema import Tema
from models.spørreundersøkelse.Undertema import Undertema
from sql.insert_spørsmål import insert_spørsmål
from sql.insert_spørsmål_undertema_relasjon import insert_spørsmål_undertema_relasjon
from sql.insert_svaralternativ import insert_svaralternativ
from sql.insert_tema import insert_tema
from sql.insert_undertema import insert_undertema
from sql.update_tema_status import update_tema_status
from sql.update_undertema_status import update_undertema_status

#### Partssamarbeid ####


forrige_tema_id = 21
undertema_id = 32

undertema_id += 1
utvikle_partssamarbeidet = Undertema(
    id=undertema_id,
    navn="Utvikle partssamarbeidet",
    spørsmål=[
        Spørsmål(
            tekst="Hvordan opplever du at partssamarbeidet har utviklet seg i løpet av samarbeidsperioden?",
            alternativer=[
                "Svært godt",
                "Godt",
                "Dårlig",
                "Svært dårlig",
                "Vet ikke",
            ],
        ),
        Spørsmål(
            tekst="Som leder, tillitsvalgt eller verneombud har jeg fått en bedre forståelse av min rolle og mine ansvarsområder i partssamarbeidet",
        ),
        Spørsmål(
            tekst="Vi har opparbeidet oss nødvendig kompetanse for å forebygge og håndtere sykefraværet vårt",
        ),
    ],
)


undertema_id += 1
veien_videre_partssamarbeid = Undertema(
    id=undertema_id,
    navn="Veien videre",
    spørsmål=[
        Spørsmål(
            tekst="Vi har laget konkrete planer for hvordan vi i partssamarbeidet skal jobbe fremover",
        ),
        Spørsmål(
            tekst="Jeg opplever at vi er motiverte for å samarbeide videre om sykefravær og arbeidsmiljø",
        ),
    ],
    obligatorisk=True,
)

#### Sykefraværsarbeid ####
# undertemaer


undertema_id += 1
sykefraværsrutiner = Undertema(
    id=undertema_id,
    navn="Sykefraværsrutiner",
    spørsmål=[
        Spørsmål(
            tekst="Vi jobber nå mer systematisk for å forebygge sykefraværet vårt",
        ),
        Spørsmål(
            tekst="Vi har godt etablerte og lett tilgjengelige sykefraværsrutiner",
        ),
        Spørsmål(
            tekst="Ansatte kjenner til egne plikter og rettigheter når de er sykmeldt eller står i fare for å bli det",
        ),
    ],
)

undertema_id += 1

oppfølgingssamtaler = Undertema(
    id=undertema_id,
    navn="Oppfølgingssamtaler",
    spørsmål=[
        Spørsmål(
            tekst="Jeg opplever at ledere er trygge under oppfølgingsamtaler med ansatte som er sykmeldt eller står i fare for å bli det",
        ),
    ],
)

undertema_id += 1

tilretteleggings_og_medvirkningsplikt = Undertema(
    id=undertema_id,
    navn="Tilretteleggings- og medvirkningsplikt",
    spørsmål=[
        Spørsmål(
            tekst="Vi har utarbeidet og tilgjengeliggjort en oversikt over våre tilretteleggingsmuligheter",
        ),
        Spørsmål(
            tekst="Vi har etablerte rutiner og god kultur for tilrettelegging for ansatte ",
        ),
        Spørsmål(
            tekst="Ansatte medvirker under tilrettelegging av arbeidsoppgaver",
        ),
    ],
)


undertema_id += 1

sykefravær_enkeltsaker = Undertema(
    id=undertema_id,
    navn="Sykefravær - enkeltsaker",
    spørsmål=[
        Spørsmål(
            tekst="Vi har nødvendig kompetanse for å håndtere vanskelige sykefraværssaker",
        ),
    ],
)

undertema_id += 1

veien_videre_sykefraværsarbeid = Undertema(
    id=undertema_id,
    navn="Veien videre",
    spørsmål=[
        Spørsmål(
            tekst="Vi vet hvor vi finner gode verktøy i arbeidet med å redusere sykefraværet vårt",
        ),
        Spørsmål(
            tekst="Jeg tror videre forebyggende sykefraværsarbeid vil bidra til å redusere sykefraværet hos oss",
        ),
    ],
    obligatorisk=True,
)


#### Arbeidsmiljø ####

# undertemaer
undertema_id += 1

utvikle_arbeidsmiljøet = Undertema(
    id=undertema_id,
    navn="Utvikle arbeidsmiljøet",
    spørsmål=[
        Spørsmål(
            tekst="Vi har nå nødvendig kompetanse til å gjøre tiltak og forbedre arbeidsmiljøet vårt ",
        ),
        Spørsmål(
            tekst="Vi har utarbeidet konkrete planer for hvordan vi skal jobbe systematisk med arbeidsmiljøet",
        ),
        Spørsmål(
            tekst="Vi har fått god forståelse for hvilke faktorer som påvirker arbeidsmiljøet vårt ",
        ),
    ],
)

undertema_id += 1

endring_og_omstilling = Undertema(
    id=undertema_id,
    navn="Endring og omstilling",
    spørsmål=[
        Spørsmål(
            tekst="Vi har etablert rutiner for medvirkning og forebygging under endrings- og omstillingsprosesser ",
        ),
        Spørsmål(
            tekst="Vi har nødvendig kompetanse for å forebygge sykefravær under omstillingsprosesser",
        ),
    ],
)

undertema_id += 1


oppfølging_av_arbeidsmiljøundersøkelser = Undertema(
    id=undertema_id,
    navn="Oppfølging av arbeidsmiljøundersøkelser",
    spørsmål=[
        Spørsmål(
            tekst="Vi har fått tilstrekkelig støtte til å gjennomføre tiltak basert på egen arbeidsmiljøundersøkelse",
        ),
        Spørsmål(
            tekst="Vi har opparbeidet oss nødvendig kompetanse til å følge opp fremtidige arbeidsmiljøundersøkelser",
        ),
    ],
)

undertema_id += 1

livsfaseorientert_personalpolitikk = Undertema(
    id=undertema_id,
    navn="Livsfaseorientert personalpolitikk",
    spørsmål=[
        Spørsmål(
            tekst="Vi har en personalpolitikk som ivaretar ansattes behov i ulike deler av livet (f.eks. graviditet, førpensjon)",
        ),
        Spørsmål(
            tekst="Vi har utarbeidet gode rutiner for hvordan vi tilrettelegger ansattes arbeid i ulike deler av livet ",
        ),
    ],
)

undertema_id += 1

psykisk_helse = Undertema(
    id=undertema_id,
    navn="Psykisk helse",
    spørsmål=[
        Spørsmål(
            tekst="Vi får tilbakemeldinger om at ansatte med psykiske plager blir godt ivaretatt",
        ),
        Spørsmål(
            tekst="Som leder, tillitsvalgt eller verneombud har jeg opparbeidet meg ferdigheter til å møte og støtte ansatte med psykiske plager",
        ),
        Spørsmål(
            tekst="Vi jobber kontinuerlig for å redusere stigma rundt psykiske plager",
        ),
    ],
)

undertema_id += 1

helseIArbeid = Undertema(
    id=undertema_id,
    navn="HelseIArbeid",
    spørsmål=[
        Spørsmål(
            tekst="Vi har fått økt kompetanse om tilrettelegging for ansatte med muskel-, skjelett- og psykiske plager",
        ),
        Spørsmål(
            tekst="Ansatte ønsker i større grad å jobbe til tross for muskel-, skjelett- og psykiske plager",
        ),
    ],
)

undertema_id += 1

veien_videre_arbeidsmiljø = Undertema(
    id=undertema_id,
    navn="Veien videre",
    spørsmål=[
        Spørsmål(
            tekst="Vi har opparbeidet oss et godt grunnlag for å jobbe videre med arbeidsmiljøet vårt   ",
        ),
        Spørsmål(
            tekst="Vi har utarbeidet konkrete planer for hvordan vi skal videreutvikle arbeidsmiljøet vårt",
        ),
    ],
    obligatorisk=True,
)


# Temaer


forrige_tema_id += 1

partssamarbeid = Tema(
    id=forrige_tema_id,
    navn="Partssamarbeid",
    undertemaer=[utvikle_partssamarbeidet, veien_videre_partssamarbeid],
)


forrige_tema_id += 1

sykefraværsarbeid = Tema(
    id=forrige_tema_id,
    navn="Sykefraværsarbeid",
    undertemaer=[
        sykefraværsrutiner,
        oppfølgingssamtaler,
        tilretteleggings_og_medvirkningsplikt,
        sykefravær_enkeltsaker,
        veien_videre_sykefraværsarbeid,
    ],
)

forrige_tema_id += 1

arbeidsmiljø = Tema(
    id=forrige_tema_id,
    navn="Arbeidsmiljø",
    undertemaer=[
        utvikle_arbeidsmiljøet,
        endring_og_omstilling,
        oppfølging_av_arbeidsmiljøundersøkelser,
        livsfaseorientert_personalpolitikk,
        psykisk_helse,
        helseIArbeid,
        veien_videre_arbeidsmiljø,
    ],
)

if __name__ == "__main__":
    spørreundersøkelse_type: Literal["Behovsvurdering", "Evaluering"] = "Evaluering"

    sql_script = ""
    sql_script += update_tema_status(tema_id=16) + "\n"
    sql_script += update_undertema_status(tema_id=16) + "\n"
    sql_script += update_tema_status(tema_id=17) + "\n"
    sql_script += update_undertema_status(tema_id=17) + "\n"
    sql_script += update_tema_status(tema_id=18) + "\n"
    sql_script += update_undertema_status(tema_id=18) + "\n"

    for tema_nr, tema in enumerate([partssamarbeid, sykefraværsarbeid, arbeidsmiljø]):
        sql_script += (
            insert_tema(
                temanavn=tema.navn,
                tema_id=tema.id,
                spørreundersøkelse_type=spørreundersøkelse_type,
                rekkefølge=tema_nr + 1,
            )
            + "\n"
        )

        for undertema_nr, undertema in enumerate(tema.undertemaer):
            sql_script += (
                insert_undertema(
                    undertema_id=undertema.id,
                    undertemanavn=undertema.navn,
                    tema_id=tema.id,
                    obligatorisk=undertema.obligatorisk,
                    temanavn=tema.navn,
                    rekkefølge=undertema_nr + 1,
                )
                + "\n"
            )

            for spørsmål_nr, spørsmål in enumerate(undertema.spørsmål):
                sql_script += (
                    f"-- Nytt spørsmål for undertema -> '{tema.navn}' : '{undertema.navn}'"
                    + "\n"
                )

                sql_script += insert_spørsmål(
                    spørsmål_id=spørsmål.id,
                    spørsmål_tekst=spørsmål.tekst,
                    flervalg=spørsmål.flervalg,
                )
                sql_script += insert_spørsmål_undertema_relasjon(
                    undertema_navn=undertema.navn,
                    undertema_id=undertema.id,
                    spørsmål_id=spørsmål.id,
                    rekkefølge=spørsmål_nr + 1,
                )
                sql_script += "-- Svaralternativer:" + "\n"

                for svaralternativ in spørsmål.svaralternativer:
                    sql_script += insert_svaralternativ(
                        svaralternativ_tekst=svaralternativ.tekst,
                        spørsmål_id=spørsmål.id,
                        svaralternativ_id=svaralternativ.id,
                    )
                sql_script += "\n"
            sql_script += "\n"
        sql_script += "\n"

    with open(
        "python_scripts/V1__nytt_migreringsskript.sql",
        "w",
    ) as text_file:
        text_file.write(sql_script)
        print("Done")
