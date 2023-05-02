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
    "Agile": {
        "name": "Agile",
    },
    "XP": {
        "name": "Extreme Programming",
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
    "CI/CD": {
        "name": "Continuous Delivery",
    },
    "SOLID": {
        "name": "SOLID principles",
    },
    "TDD": {
        "name": "Test Driven Development",
    },
}

max_len = 220
pc_cut_len = 69
phone_cut_len = 50

sep = " & "

s = ""
s += f"{post} "
s += f"@{company}; "
# s += "Stack: "
res = s
for meth in methodologies.values():
    s += meth["name"]
    if len(s) >= max_len:
        break
    res = s = s + sep

res = res.removesuffix(sep)

print()
print(res)
print()
print(res[:pc_cut_len] + "…")
print(res[:phone_cut_len] + "…")
print()

assert company in res[:phone_cut_len]
assert methodologies["Craft"]["name"] in res[:phone_cut_len]

assert len(res) <= max_len

