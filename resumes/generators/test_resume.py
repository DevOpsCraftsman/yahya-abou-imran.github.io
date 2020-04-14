import json
from operator import eq, contains
import pytest
from resume import ResumeGenerator


def test_resume():
    with open("./generators/fr.json", "r") as f:
        fr = json.load(f)
    rg = ResumeGenerator(sections=fr, format="md")
    md = rg()
    assert "### COMPÉTENCES" in md


@pytest.mark.parametrize("cmp", [contains, eq])
def test_full_compat(cmp):
    with open("./generators/fr.json", "r") as f:
        fr_sections = json.load(f)
    with open("./CV-Alexandre-Poitevin-fr.md", "r") as f:
        fr_resume = f.read()
    resume = ResumeGenerator(fr_sections)()
    assert cmp(fr_resume, resume)
