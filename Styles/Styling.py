
def load_stylesheet(filename):
    with open(filename, "r") as file:
        return file.read()

css_style = load_stylesheet("./Styles/style.css")