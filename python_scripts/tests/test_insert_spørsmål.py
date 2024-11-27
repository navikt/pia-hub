import pytest
from sql.insert_spørsmål import insert_spørsmål


def test_insert_spørsmål_valid_input():
    spørsmål_id = "12345678-1234-1234-1234-123456789012"
    spørsmål_tekst = "Hva er din favorittfarge?"
    flervalg = True
    expected_query = (
        "INSERT INTO ia_sak_kartlegging_sporsmal (sporsmal_id, sporsmal_tekst, flervalg)\n"
        + "VALUES ('12345678-1234-1234-1234-123456789012','Hva er din favorittfarge?',true);\n"
    )
    assert insert_spørsmål(spørsmål_id, spørsmål_tekst, flervalg) == expected_query


def test_insert_spørsmål_invalid_id_length():
    spørsmål_id = "123"
    spørsmål_tekst = "Hva er din favorittfarge?"
    flervalg = True
    with pytest.raises(Exception) as excinfo:
        insert_spørsmål(spørsmål_id, spørsmål_tekst, flervalg)
    assert str(excinfo.value) == "et spørsmål sin id (uuid) må være 36 tegn lang"


def test_insert_spørsmål_empty_text():
    spørsmål_id = "12345678-1234-1234-1234-123456789012"
    spørsmål_tekst = ""
    flervalg = True
    with pytest.raises(Exception) as excinfo:
        insert_spørsmål(spørsmål_id, spørsmål_tekst, flervalg)
    assert str(excinfo.value) == "Et spørsmål kan ikke være tomt"


def test_insert_spørsmål_flervalg_false():
    spørsmål_id = "12345678-1234-1234-1234-123456789012"
    spørsmål_tekst = "Hva er din favorittfarge?"
    flervalg = False
    expected_query = (
        "INSERT INTO ia_sak_kartlegging_sporsmal (sporsmal_id, sporsmal_tekst, flervalg)\n"
        + "VALUES ('12345678-1234-1234-1234-123456789012','Hva er din favorittfarge?',false);\n"
    )
    assert insert_spørsmål(spørsmål_id, spørsmål_tekst, flervalg) == expected_query
