import pytest
from sql.insert_svaralternativ import insert_svaralternativ


def test_insert_svaralternativ_valid_input():
    spørsmål_id = "12345678-1234-1234-1234-123456789012"
    svaralternativ_id = "87654321-4321-4321-4321-210987654321"
    svaralternativ_tekst = "Helt enig"
    expected_query = (
        "INSERT INTO ia_sak_kartlegging_svaralternativer (svaralternativ_id, sporsmal_id, svaralternativ_tekst)\n"
        + f"VALUES ('{svaralternativ_id}', '{spørsmål_id}', '{svaralternativ_tekst}');\n"
    )
    assert (
        insert_svaralternativ(spørsmål_id, svaralternativ_id, svaralternativ_tekst)
        == expected_query
    )


def test_insert_svaralternativ_invalid_spørsmål_id_length():
    with pytest.raises(Exception) as excinfo:
        insert_svaralternativ(
            "feil-id", "87654321-4321-4321-4321-210987654321", "Helt enig"
        )
    assert "et spørsmål sin id (uuid) må være 36 tegn lang" in str(excinfo.value)


def test_insert_svaralternativ_invalid_svaralternativ_id_length():
    with pytest.raises(Exception) as excinfo:
        insert_svaralternativ(
            "12345678-1234-1234-1234-123456789012", "feil-id", "Helt uenig"
        )
    assert "et svaralternativ sin id (uuid) må være 36 tegn lang" in str(excinfo.value)


def test_insert_svaralternativ_empty_svaralternativ_tekst():
    with pytest.raises(Exception) as excinfo:
        insert_svaralternativ(
            "12345678-1234-1234-1234-123456789012",
            "87654321-4321-4321-4321-210987654321",
            "",
        )
    assert "Et svaralternativ må ha noe tekst" in str(excinfo.value)
