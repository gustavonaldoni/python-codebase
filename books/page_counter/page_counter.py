import re

def count_pages(file_path: str) -> int:
    with open(file_path, 'r') as file:
        buffer = file.read()
        pages = re.findall(r'{[0-9]+}', buffer)

        pages = [page[1:-1] for page in pages]
        pages = [int(page) for page in pages]

        return sum(pages)

def main():
    pages = count_pages('./year2023.txt')
    print(f'Total pages read in 2023: {pages}')

if __name__ == "__main__":
    main()
