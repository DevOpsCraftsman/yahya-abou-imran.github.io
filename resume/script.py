company = "EasyWayWeb"
post = "Software Engineer & Architect"

methodologies = [
    {
        "name": "Agile",
    },
    {
        "name": "Software Craftsmanship",
        "shortname": "Craft",
    },
    {
        "name": "DevOps",
    },
    {
        "name": "Extreme Programming",
        "shortname": "XP",
    },
    {
        "name": "Domain Driven Design",
        "shortname": "DDD",
    },
    {
        "name": "Behavior Driven Development",
        "shortname": "DDD",
    },
    {
        "name": "Continuous Delivery",
        "shortname": "CI/CD",
    },
    {
        "name": "Clean Architecture",
    },
    {
        "name": "Clean Code",
    },
]

s = ""
s += f"@{company}: "
s += f"{post}. "
s += "Stack: "
s += ", ".join(meth["name"] for meth in methodologies)

assert len(s) <= 220

print(s)
