import yaml


def sort(languages):
     return sorted(languages, key=lambda lang: lang["date"])


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


print("\n## Interinting for prod:")
display(extract(data, "prod"))


print("\n## Historicals:")
display(extract(data, "historical"))


print("\n## Others:")
display(data)
