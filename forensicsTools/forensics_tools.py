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
    
def get_all_items(file_path: str) -> list[tuple[str, str]]:
    with open(file_path, 'rb') as file:
        buffer = file.read().decode("utf-8")

        regex = r"""<span class="item_name">
            <a
              title=".*"
              class="title external_url_link"
              target="_blank"
              href=".*"
              data-item-href=".*"
            >
              .*
            </a>"""
        
        result = re.findall(regex, buffer)

        titles = [re.search(r'title=".*"', r).group() for r in result]
        titles = [t.replace('title=', '').replace('"', '') for t in titles]

        links = [re.search(r'href=".*"', r).group() for r in result]
        links = [l.replace('href=', '').replace('"', '') for l in links]

        return list(zip(titles, links))

def parse_html(file_path: str):
    modules = get_all_modules(file_path)
    items = get_all_items(file_path)

    for module in modules:
        print(module)

    print()

    for item in items:
        title = item[0]
        link = item[1]

        print(title)
        print(link)

        print()

def main():
    parse_html(FILE_PATH)

if __name__ == '__main__':
    main()