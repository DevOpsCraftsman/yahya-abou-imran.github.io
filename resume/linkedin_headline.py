company = "Easy Way Web"
# post = "Software Engineer & Architect"
# title = "Software Engineer"
title = "DevOps Craftsman"

methodologies = {
    "DevOps": {
        "name": "DevOps",
        "headline": False,
    },
    "Craft": {
        "name": "Software Craftsmanship",
        "headline": False,
    },
    "Lean": {
        "name": "Lean Software Development",
        "headline": False,
    },
    "Agile": {
        "name": "Agile",
        "headline": False,
    },
    "XP": {
        "name": "Extreme Programming",
    },
    "Kanban": {
        "name": "Kanban",
    },
    "BDD": {
        "name": "Behavior Driven Development",
    },
    "DDD": {
        "name": "Domain Driven Design",
    },
    "CI/CD": {
        "name": "Continuous Delivery",
        "level": "Medium",
    },
    "IaC": {
        "name": "Infrastructure as Code",
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
    "TDD": {
        "name": "Test Driven Development",
        "level": "low",
    },
}

max_len = 220
pc_cut_len = 65
phone_cut_len = 40
sep = ", "
at = "At "
opening = ": "
nbsp = True
short = True


def headline(*, short=short, sep=sep, nbsp=nbsp, **kwargs):

    s = ""
    # s += f"{post} "
    # s += f"{at}{company}{opening}"
    # s += "Stack: "
    s += (
        "Meaningful Software Delivery"
        # " advocate"
        # " at"
        " – "
        f"{company}"
        " | "
        f"{title}"
        " | "
        # "Empowering software delivery actors "
        # "to surmount troubles and experience fulfillment "
        # "with successful products | "
    )

    res = s
    for name, meth in methodologies.items():
        if not meth.get("headline", True):
            continue
        if short:
            _s = name
        else:
            _s = meth["name"]
        if nbsp:
            _s = _s.replace(" ", " ", 1)
        s += _s
        if len(s) >= max_len:
            print(f"Stripped at: {_s}")
            break
        res = s = s + sep

    res = res.removesuffix(sep)
    return res


def description(tmpl="• {name}\n"):

    res = ""
    for shortname, meth in methodologies.items():
        name = meth["name"]
        s = tmpl.format(name=name)
        res += s

    return res


def display(res):
    print()
    print(res)
    print()
    print(res[:pc_cut_len] + "…")
    print(res[:phone_cut_len] + "…")
    print()

def valitade(res):
    assert "DevOps" in res[:pc_cut_len]
    assert "Craft" in res[:pc_cut_len]
    assert company in res[:pc_cut_len]
    # assert "DevOps" in res[:phone_cut_len]
    # assert "Craft" in res[:phone_cut_len]
    # assert company in res[:phone_cut_len]
    print(f"length: {len(res)} (≤ {max_len})")
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
    res = headline(**vars(args))
    display(res)
    valitade(res)
    print(description())
    print(description(tmpl="{name} "))
    print()

