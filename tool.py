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
    print(uae)
    #print("Enter the Desired Format\n 1: Resume \n 2: CV")
    #format_num = input_validator(1,3)
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
    latex.stream(uae=uae,Projects=filtered_projects).dump("./output/output.xtx")
    subprocess.run(["xelatex.exe","output.xtx"], cwd="./output")

