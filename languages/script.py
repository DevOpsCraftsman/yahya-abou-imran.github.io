import yaml


def sort(languages):
    def _k(lang):
        date = lang.get("date")
        return 3000 if date == "..." else date
    return sorted(languages, key=_k)


def display(languages):
    for l in sort(languages):
        s = f"- `[{('*' * l['level']).ljust(5)}]` {l['name']} ({l['date']})"
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
display(extract(data, "mainstream"))


print("\n## Secondary:")
display(extract(data, "secondary"))


print("\n## Historicals:")
display(extract(data, "historical"))


print("\n## Others:")
display(data)
