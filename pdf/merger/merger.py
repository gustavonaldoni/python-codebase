import fitz
import os

class PDFMerger:
    def merge(self, result_file_path: str, file_paths: list):
        result = fitz.open()

        for file_path in file_paths:
            with fitz.open(file_path) as file:
                result.insert_pdf(file)

        result.save(result_file_path)

    def merge_dir(self, result_file_path: str, directory_path: str):
        """
        Merges all PDF files of a given directory.
        """
        file_paths = []

        for file_path in os.listdir(directory_path):
            full_file_path = os.path.join(directory_path, file_path)

            if os.path.isfile(os.path.join(full_file_path)) and full_file_path.endswith('.pdf'):
                file_paths.append(full_file_path)

        file_paths.sort()

        self.merge(result_file_path, file_paths)
