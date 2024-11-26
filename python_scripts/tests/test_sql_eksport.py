from sql.update_tema_status import update_tema_status
from sql.update_undertema_status import update_undertema_status


def test_gjør_tema_inaktivt():
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


def test_gjør_undertema_inaktivt():
    assert (
        update_undertema_status(2)
        == "-- Gjør undertema inaktivt"
        + "\n"
        + "UPDATE ia_sak_kartlegging_undertema"
        + "\n"
        + "SET status = 'INAKTIV'"
        + "\n"
        + "WHERE undertema_id = 2;"
        + "\n"
    )
