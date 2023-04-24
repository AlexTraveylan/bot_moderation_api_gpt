from src.app.core.twitch.avertissements import Compteur


def test_add_avertissement():
    c = Compteur()
    c.add("avertissement1")
    assert c.avertissementList == {"avertissement1": 1}


def test_add_existing_avertissement():
    c = Compteur({"avertissement1": 2})
    c.add("avertissement1")
    assert c.avertissementList == {"avertissement1": 3}


def test_add_multiple_avertissements():
    c = Compteur()
    c.add("avertissement1")
    c.add("avertissement2")
    c.add("avertissement1")
    assert c.avertissementList == {"avertissement1": 2, "avertissement2": 1}
