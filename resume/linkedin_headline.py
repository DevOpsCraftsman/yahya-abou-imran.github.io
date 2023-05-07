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
    "CI/CD": {
        "name": "Continuous Delivery",
        "level": "Medium",
    },
    "Clean Code": {
        "name": "Clean Code",
    },
    "Clean Architecure": {
        "name": "Clean Architecture",
    },
    "DDD": {
        "name": "Domain Driven Design",
    },
    "BDD": {
        "name": "Behavior Driven Development",
    },
    # "SOLID": {
    #     "name": "SOLID principles",
    #     "level": "Medium",
    # },
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


def compute(*, sep=sep, nbsp=nbsp):

    s = ""
    # s += f"{post} "
    s += f"@{company} = "
    # s += "Stack: "

    res = s
    for name, meth in methodologies.items():
        # _s = name
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
    import sys
    if len(sys.argv) >= 2:
        sep = sys.argv[1]
    if len(sys.argv) >= 3:
        nbsp = False
        print("Not using NBSP")
    res = compute(sep=sep, nbsp=nbsp)
    display(res)
    valitade(res)
