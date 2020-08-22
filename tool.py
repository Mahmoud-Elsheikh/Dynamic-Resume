import json
import subprocess
from jinja2 import Environment, FileSystemLoader
if __name__ == "__main__":
    with open('projects.json', 'r') as file:
        data=file.read()
    projects= json.loads(data)
    env = Environment(
        loader=FileSystemLoader('templates'),
    )
    latex= env.get_template('Resume.xtx')
    latex.stream(Projects=projects).dump("./output/output.xtx")
    subprocess.run(["xelatex.exe","output.xtx"], cwd="./output")

