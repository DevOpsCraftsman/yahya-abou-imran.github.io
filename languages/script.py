import yaml


def sort(languages, *fields):
    if not fields:
        fields = ("date",)
    def _k(lang):
        return tuple(lang.get(f) for f in fields)
    return sorted(languages, key=_k)


def display(languages, *fields):
    for l in sort(languages, *fields):
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
display(extract(data, "mainstream"), "level", "date")

jvm_languages = extract(data, "jvm")

print("\n## Secondary:")
display(extract(data, "secondary"), "level", "date")

print("\n## JVM:")
display(jvm_languages, "level", "date")


print("\n## Historicals:")
display(extract(data, "historical"), "level", "date")


print("\n## Others:")
display(data, "level", "date")
