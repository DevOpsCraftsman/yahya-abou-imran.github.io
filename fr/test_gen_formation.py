from gen_formation import get_txt_formation


def test_gen_formation():
    ftxt = get_txt_formation()
    assert "• Des" in ftxt
    assert "Détail de la formation :" in ftxt
    assert "## Liste des séries" not in ftxt
    assert "Contact :\n  • Tél" in ftxt
    assert "formation.html" in ftxt
    assert "yahya-abou-imran" in ftxt
    assert "https://yahya-abou-imran.github.io/fr/formation.html" in ftxt
    assert "+213798786428" in ftxt
    assert "yahya-abou-imran@protonmail.com" in ftxt
