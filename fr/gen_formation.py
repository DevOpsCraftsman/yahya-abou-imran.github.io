def get_txt_formation():

    with open("formation.md") as f:
        s = f.read()

    i1 = s.index("## List")
    i2 = s.index("#### Contact")

    details = "Détail de la formation :\n\n"
    details += "https://yahya-abou-imran.github.io/fr/formation.html\n\n\n"""

    s = s[:i1] + details + s[i2:]
    # import pdb; pdb.set_trace()

    s = s.replace("# ", "")
    s = s.replace("#", "")
    s = s.replace("- ", "• ")

    return s


if __name__ == "__main__":
    with open("formation.txt", "w") as f:
        f.write(get_txt_formation())
