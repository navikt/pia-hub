import pytest
from sql.update_tema_status import update_tema_status


def test_update_tema_status_inaktiv():
    assert (
        update_tema_status(1)
        == "-- Gjør tema inaktivt"
        + "\n"
        + "UPDATE ia_sak_kartlegging_tema"
        + "\n"
        + "SET status = 'INAKTIV'"
        + "\n"
        + "WHERE tema_id = 1;"
        + "\n"
    )


def test_update_tema_status_aktiv():
    assert (
        update_tema_status(2, "AKTIV")
        == "-- Gjør tema aktivt"
        + "\n"
        + "UPDATE ia_sak_kartlegging_tema"
        + "\n"
        + "SET status = 'AKTIV'"
        + "\n"
        + "WHERE tema_id = 2;"
        + "\n"
    )


def test_update_tema_status_invalid_id():
    with pytest.raises(Exception, match="Et tema sin id må være et positivt tall"):
        update_tema_status(0)


def test_update_tema_status_invalid_status():
    with pytest.raises(ValueError, match="status must be either 'AKTIV' or 'INAKTIV'"):
        update_tema_status(1, "INVALID")
