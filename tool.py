import json
import subprocess
from jinja2 import Environment, FileSystemLoader

def input_validator(lower, upper):
    while True:
        try:
            inp= int(input("Format: "))
        except ValueError:
            print("Please enter a number.")
            continue
        if lower <= inp <= upper:
            return inp
        else:
            print("Incorrect Input")

def binary_validator():
    while True:
        data=input("Y/N? ")
        if data.lower() not in ("y", "n"):
            print("Incorrect Input")
        else:
            if data.lower()=="y":
                return True
            else:
                return False

if __name__ == "__main__":
    with open('projects.json', 'r') as file:
        data=file.read()
    projects= json.loads(data)
    env = Environment(
        loader=FileSystemLoader('templates'),
    )

    print("Dynamic CV")
    #Commented Out Until CV Template Release
    print("For the UAE? Y/N")
    uae = binary_validator()
    print("Two Pages? Y/N")
    pagecount = binary_validator()
    print("PhD? Y/N")
    phd = binary_validator()

    latex= env.get_template('Resume.xtx')

    print("Choose projects to add:")
    for idx, project in enumerate(projects):
        print(f"{idx+1}. {project['Title']}")
    project_input = [x for x in input("Enter values separated by a space: ").split()]
    temp = []
    for x in project_input:
        try:
            temp.append(int(x))
        except ValueError:
            pass
    filtered_input = [x for x in temp if 1 <= x <= len(projects) ]
    filtered_projects = [projects[x-1] for x in filtered_input]
    latex.stream(pagecount=pagecount,uae=uae, phd= phd, Projects=filtered_projects).dump("./output/output.xtx")
    subprocess.run(["xelatex","output.xtx"], cwd="./output")
    subprocess.run(["bibtex","output.aux"], cwd="./output")
    subprocess.run(["xelatex","output.xtx"], cwd="./output")

