from jinja2 import Environment, FileSystemLoader
if __name__ == "__main__":
    env = Environment(
        loader=FileSystemLoader('templates'),
    )
    template = env.get_template('test.txt')
    template.stream(name="Blank", day="Friday").dump("./output/output.txt")


