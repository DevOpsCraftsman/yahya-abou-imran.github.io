class ResumeGenerator:

    def __init__(self, sections, format="md"):
        self.sections = sections
        self.format = format

    def __call__(self):
        s = ""
        skills = self.sections["skills"]
        s += f"### {skills['name']}\n"
        for item in skills['content']:
            s += f"\t- {item}"
        return s
