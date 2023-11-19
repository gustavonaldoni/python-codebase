import re

FILE_PATH = "./seguranca.html"

def get_all_modules(file_path: str) -> list[str]:
    with open(file_path, 'rb') as file:
        buffer = file.read().decode("utf-8")

        regex = r"""<div
  class="item-group-condensed context_module
    
    
    "
    aria-label=".*"
    data-workflow-state="active"
    data-module-url=".*"
    data-module-id=".*"
    id="context_module_.*"
    style=""
>"""

        result = re.findall(regex, buffer)
        result = [re.search(r'aria-label=".*"', r).group() for r in result]
        result = [r[11:].replace('"', '') for r in result]

        return result

def parse_html(file_path: str):
    modules = get_all_modules(file_path)

    print(modules)

def main():
    parse_html(FILE_PATH)

if __name__ == '__main__':
    main()