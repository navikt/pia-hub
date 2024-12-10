from models.spørreundersøkelse.Svaralternativ import Svaralternativ
from util.generer_uuider import generer_uuid_med_delay


def lagSvaralternativer(alternativer: list[str]) -> list[Svaralternativ]:
    return [Svaralternativ(tekst=alternativ) for alternativ in alternativer]


class Spørsmål:
    def __init__(
        self,
        tekst: str,
        flervalg: bool = False,
        alternativer=[
            "Enig",
            "Litt enig",
            "Litt uenig",
            "Uenig",
            "Vet ikke",
        ],
    ):
        self.id = generer_uuid_med_delay()
        self.tekst = tekst
        self.flervalg = flervalg
        self.svaralternativer = lagSvaralternativer(alternativer=alternativer)
