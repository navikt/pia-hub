import pytest
from sql.update_undertema_status import update_undertema_status


def test_update_undertema_status_inaktiv():
    assert (
        update_undertema_status(2)
        == "-- Gjør undertemaer til temaet 2 inaktivt"
        + "\n"
        + "UPDATE ia_sak_kartlegging_undertema"
        + "\n"
        + "SET status = 'INAKTIV'"
        + "\n"
        + "WHERE tema_id = 2;"
        + "\n"
    )


def test_update_undertema_status():
    assert (
        update_undertema_status(2, "INAKTIV")
        == "-- Gjør undertemaer til temaet 2 inaktivt"
        + "\n"
        + "UPDATE ia_sak_kartlegging_undertema"
        + "\n"
        + "SET status = 'INAKTIV'"
        + "\n"
        + "WHERE tema_id = 2;"
        + "\n"
    )


def test_update_undertema_status_aktiv():
    assert (
        update_undertema_status(2, "AKTIV")
        == "-- Gjør undertemaer til temaet 2 aktivt"
        + "\n"
        + "UPDATE ia_sak_kartlegging_undertema"
        + "\n"
        + "SET status = 'AKTIV'"
        + "\n"
        + "WHERE tema_id = 2;"
        + "\n"
    )


def test_update_undertema_status_invalid_id():
    with pytest.raises(Exception, match="Et undertema sin id må være et positivt tall"):
        update_undertema_status(0)


def test_update_undertema_status_invalid_status():
    with pytest.raises(ValueError, match="status must be either 'AKTIV' or 'INAKTIV'"):
        update_undertema_status(1, "INVALID")
