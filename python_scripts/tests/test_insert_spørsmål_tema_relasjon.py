import pytest
from sql.insert_spørsmål_tema_relasjon import insert_spørsmål_tema_relasjon


def test_insert_spørsmål_tema_relasjon_valid_input():
    result = insert_spørsmål_tema_relasjon(
        "123e4567-e89b-12d3-a456-426614174000", 1, "Test Tema"
    )
    # TODO: test med uuid regex?
    expected = (
        "-- Knytt tema til spørsmål -> 'Test Tema'\n"
        "INSERT INTO ia_sak_kartlegging_tema_til_spørsmål (tema_id, sporsmal_id)\n"
        "VALUES (1, '123e4567-e89b-12d3-a456-426614174000');\n"
    )
    assert result == expected


def test_insert_spørsmål_tema_relasjon_invalid_spørsmål_id():
    with pytest.raises(Exception) as excinfo:
        insert_spørsmål_tema_relasjon("invalid-uuid", 1, "Test Tema")
    assert str(excinfo.value) == "et spørsmål sin id (uuid) må være 36 tegn lang"


def test_insert_spørsmål_tema_relasjon_invalid_tema_id():
    with pytest.raises(Exception) as excinfo:
        insert_spørsmål_tema_relasjon(
            "123e4567-e89b-12d3-a456-426614174000", -1, "Test Tema"
        )
    assert str(excinfo.value) == "tema_id må være positiv"


def test_insert_spørsmål_tema_relasjon_empty_tema_navn():
    with pytest.raises(Exception) as excinfo:
        insert_spørsmål_tema_relasjon("123e4567-e89b-12d3-a456-426614174000", 1, "")
    assert str(excinfo.value) == "tema_navn kan ikke være tom"
