from typing import Literal

from models.spørreundersøkelse.Undertema import Undertema


class Tema:
    def __init__(
        self,
        id: int,
        navn: Literal["Partssamarbeid", "Sykefraværsarbeid", "Arbeidsmiljø"],
        undertemaer: list[Undertema],
    ):
        self.id = id
        self.navn = navn
        self.undertemaer = undertemaer
