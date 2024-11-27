import pytest
from sql.insert_tema import insert_tema


def test_insert_tema_success():
    result = insert_tema("Test Tema", 1, "Behovsvurdering", 1)
    expected = (
        "-- Nytt tema -> 'Test Tema'\n"
        "INSERT INTO ia_sak_kartlegging_tema (tema_id, navn, status, rekkefolge, type)\n"
        "VALUES (1, 'Test Tema', 'AKTIV', 1, 'Behovsvurdering');\n"
    )
    assert result == expected


def test_insert_tema_empty_name():
    with pytest.raises(Exception) as excinfo:
        insert_tema("", 1, "Behovsvurdering", 1)
    assert str(excinfo.value) == "Et tema må ha et navn"


def test_insert_tema_invalid_tema_id():
    with pytest.raises(Exception) as excinfo:
        insert_tema("Test Tema", 0, "Behovsvurdering", 1)
    assert str(excinfo.value) == "Et tema sin id må være et positivt tall"


def test_insert_tema_invalid_rekkefolge():
    with pytest.raises(Exception) as excinfo:
        insert_tema("Test Tema", 1, "Behovsvurdering", 0)
    assert str(excinfo.value) == "rekkefølge burde starte fra 1"


def test_insert_tema_invalid_sporreundersokelse_type():
    with pytest.raises(Exception) as excinfo:
        insert_tema("Test Tema", 1, "InvalidType", 1)
    assert str(excinfo.value) == "Ugyldig type for spørreundersøkelse"
