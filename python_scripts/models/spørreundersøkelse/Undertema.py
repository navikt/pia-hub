from models.spørreundersøkelse.Spørsmål import Spørsmål


class Undertema:
    def __init__(
        self, id: int, navn: str, spørsmål: list[Spørsmål], obligatorisk: bool = False
    ):
        self.id = id
        self.navn = navn
        self.spørsmål = spørsmål
        self.obligatorisk = obligatorisk
