import yaml


def sort(languages, *fields):
    if not fields:
        fields = ("date",)
    def _k(lang):
        return tuple(lang.get(f) for f in fields)
    return sorted(languages, key=_k)


def display(languages, *fields):
    for l in sort(languages, *fields):
        s = f"- `[{('*' * l.get('level')).ljust(5)}]` {l['name']} ({l['date']})"
        print(s)


def extract(languages, field):
    extracted = []
    for lang in languages.copy():
        if lang.get(field):
            extracted.append(lang)
            languages.remove(lang)
    return extracted


with open("./data.yaml") as file:
    data = yaml.safe_load(file)


print("## Mainstreams:")
display(extract(data, "mainstream"), "date")


print("\n## Secondary:")
display(extract(data, "secondary"), "date")


print("\n## Functional:")
display(extract(data, "functional"), "date")


print("\n## Historicals:")
display(extract(data, "historical"), "date")


print("\n## Others:")
display(data, "date")

print("")

