from dataclasses import dataclass
import re

HTML_PATH = "./seguranca.html"
FILE_PATH = "./ferramentasPericiaForenseComputacional.txt"

@dataclass
class Item:
    title: str
    link: str
    
def get_all_items(html_path: str) -> list[Item]:
    with open(html_path, 'rb') as file:
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
        
        search_result = re.findall(regex, buffer)

        titles = [re.search(r'title=".*"', r).group() for r in search_result]
        titles = [t.replace('title=', '').replace('"', '') for t in titles]

        links = [re.search(r'href=".*"', r).group() for r in search_result]
        links = [l.replace('href=', '').replace('"', '') for l in links]

        result = [Item(title, link) for title, link in zip(titles, links)]

        return result

def parse_html_to_file(html_path: str, file_path: str):
    items = get_all_items(html_path)

    with open(file_path, 'wb') as file:
        for item in items:
            text = f'{item.title}:\n'
            text += f'{item.link}\n\n'

            text = text.encode()

            file.write(text)

def main():
    parse_html_to_file(HTML_PATH, FILE_PATH)

if __name__ == '__main__':
    main()