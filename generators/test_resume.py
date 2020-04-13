from resume import ResumeGenerator
import json


def test_resume():
    with open("./generators/fr.json", "r") as f:
        fr = json.load(f)
    rg = ResumeGenerator(sections=fr, format="md")
    md = rg()
    assert "### Compétences" in md
    assert "- Python" in md
