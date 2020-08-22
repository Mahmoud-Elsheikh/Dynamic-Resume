import json
from jinja2 import Environment, FileSystemLoader
if __name__ == "__main__":
    with open('projects.json', 'r') as file:
        data=file.read()
    projects= json.loads(data)
    env = Environment(
        loader=FileSystemLoader('templates'),
    )
    #template.stream(name="Blank", day="Friday").dump("./output/output.txt")
    latex= env.get_template('latex.txt')
    print(latex.render(Projects=projects))


