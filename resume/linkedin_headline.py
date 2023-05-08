company = "EasyWayWeb"
# post = "Software Engineer & Architect"
post = "Software Engineer"

methodologies = {
    "Craft": {
        "name": "Software Craftsmanship",
    },
    "DevOps": {
        "name": "DevOps",
    },
    "Lean": {
        "name": "Lean",
    },
    "Agile": {
        "name": "Agile",
    },
    "XP": {
        "name": "Extreme Programming",
    },
    "TDD/BDD": {
        "name": "Behavior Driven Development",
    },
    "CI/CD": {
        "name": "Continuous Delivery",
        "level": "Medium",
    },
    "DDD": {
        "name": "Domain Driven Design",
    },
    "Clean Arch": {
        "name": "Clean Architecture",
    },
    "Clean Code": {
        "name": "Clean Code",
    },
    "SOLID": {
        "name": "SOLID principles",
        "level": "Medium",
    },
    # "TDD": {
    #     "name": "Test Driven Development",
    #     "level": "low",
    # },
}

max_len = 220
pc_cut_len = 69
phone_cut_len = 50
sep = " & "
nbsp = True
short = True


def compute(*, short=short, sep=sep, nbsp=nbsp, **kwargs):

    s = ""
    # s += f"{post} "
    s += f"@{company} = "
    # s += "Stack: "

    res = s
    for name, meth in methodologies.items():
        if short:
            _s = name
        else:
            _s = meth["name"]
        if nbsp:
            _s = _s.replace(" ", " ", 1)
        s += _s
        if len(s) >= max_len:
            break
        res = s = s + sep

    res = res.removesuffix(sep)
    return res


def display(res):
    print()
    print(res)
    print()
    print(res[:pc_cut_len] + "…")
    print(res[:phone_cut_len] + "…")
    print()

def valitade(res):
    assert company in res[:phone_cut_len]
    assert "Craft" in res[:phone_cut_len]
    assert len(res) <= max_len


if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('--short', action="store_true", default=short)
    parser.add_argument('--space', action="store_false", dest="nbsp", default=nbsp)
    parser.add_argument('--sep', default=sep)
    args = parser.parse_args()
    if not args.nbsp:
        print("Not using NBSP")
    res = compute(**vars(args))
    display(res)
    valitade(res)
