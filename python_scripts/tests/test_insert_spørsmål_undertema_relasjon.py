import pytest
from sql.insert_spørsmål_undertema_relasjon import insert_spørsmål_undertema_relasjon


def test_valid_input():
    result = insert_spørsmål_undertema_relasjon(
        "Test Undertema", 1, "12345678-1234-1234-1234-123456789012", 1
    )
    # TODO: test med uuid regex?
    expected = (
        "-- Knytt spørsmål til undertema -> 'Test Undertema'\n"
        "INSERT INTO ia_sak_kartlegging_sporsmal_til_undertema (undertema_id, sporsmal_id,rekkefolge)\n"
        "VALUES (1, '12345678-1234-1234-1234-123456789012', 1);\n"
    )
    assert result == expected


def test_invalid_spørsmål_id_length():
    with pytest.raises(Exception) as excinfo:
        insert_spørsmål_undertema_relasjon("Test Undertema", 1, "short-id", 1)
    assert str(excinfo.value) == "et spørsmål sin id (uuid) må være 36 tegn lang"


def test_negative_undertema_id():
    with pytest.raises(Exception) as excinfo:
        insert_spørsmål_undertema_relasjon(
            "Test Undertema", -1, "12345678-1234-1234-1234-123456789012", 1
        )
    assert str(excinfo.value) == "undertema_id må være positiv"


def test_empty_undertema_navn():
    with pytest.raises(Exception) as excinfo:
        insert_spørsmål_undertema_relasjon(
            "", 1, "12345678-1234-1234-1234-123456789012", 1
        )
    assert str(excinfo.value) == "undertema_navn kan ikke være tom"


def test_invalid_rekkefølge():
    with pytest.raises(Exception) as excinfo:
        insert_spørsmål_undertema_relasjon(
            "Test Undertema", 1, "12345678-1234-1234-1234-123456789012", 0
        )
    assert str(excinfo.value) == "rekkefølge burde starte fra 1"
