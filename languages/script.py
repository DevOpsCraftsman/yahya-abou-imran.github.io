import yaml


def sort(languages):
     return sorted(languages, key=lambda lang: lang["date"])


with open("./data.yaml") as file:
    data = yaml.safe_load(file)

mainstreams: list = []

lang: dict
for lang in data.copy():
    if lang.get("mainstream"):
        mainstreams.append(lang)
        data.remove(lang)

print("## Mainstreams:")
for lang in sort(mainstreams):
    print(f"- `[{('*' * lang['level']).ljust(5)}]` {lang['name']} ({lang['date']})")


for_prod = []
for lang in data.copy():
    if lang.get("prod"):
        for_prod.append(lang)
        data.remove(lang)

print("\n## Interinting for prod:")
for lang in sort(for_prod):
    print(f"- `[{('*' * lang['level']).ljust(5)}]` {lang['name']} ({lang['date']})")

print("\n## Others:")
for lang in sort(data):
    print(f"- `[{('*' * lang['level']).ljust(5)}]` {lang['name']} ({lang['date']})")
