import pytest
from sql.insert_undertema import insert_undertema


def test_insert_undertema_success():
    result = insert_undertema(1, "Test Undertema", 1, True, 1, "Test Tema")
    expected = (
        "-- Nytt undertema -> 'Test Tema' : 'Test Undertema'\n"
        "INSERT INTO ia_sak_kartlegging_undertema (undertema_id, navn, status, rekkefolge, tema_id, obligatorisk)\n"
        "VALUES (1, 'Test Undertema', 'AKTIV', 1, 1, true);\n"
    )
    assert result == expected


def test_insert_undertema_invalid_undertema_id():
    with pytest.raises(Exception, match="Et undertema sin id må være et positivt tall"):
        insert_undertema(0, "Test Undertema", 1, True, 1)


def test_insert_undertema_empty_undertemanavn():
    with pytest.raises(Exception, match="Et undertema må ha et navn"):
        insert_undertema(1, "", 1, True, 1)


def test_insert_undertema_invalid_tema_id():
    with pytest.raises(Exception, match="Et tema sin id må være et positivt tall"):
        insert_undertema(1, "Test Undertema", 0, True, 1)


def test_insert_undertema_invalid_rekkefolge():
    with pytest.raises(Exception, match="rekkefølge burde starte fra 1"):
        insert_undertema(1, "Test Undertema", 1, True, 0)
