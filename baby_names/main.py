import os

from baby_names.errors import check_folder_exists
from baby_names.files import get_list_of_files, read_data_from_file
from baby_names.normalizers import filter_files_names


def make_names_data_structure(files_filtered: list[str], folder: str):
    names_structure = {
        'girls': [],
        'boys': [],
    }
    for file in files_filtered:
        path = os.path.join(folder, file)
        names = read_data_from_file(path)
        print(names)


def main(folder: str) -> None:
    if not check_folder_exists(folder):
        print(f'Incorrect folder: {folder}')
        return None

    files = get_list_of_files(folder)
    files_filtered = filter_files_names(files)
    make_names_data_structure(files_filtered, folder)


if __name__ == '__main__':
    folder1 = 'data'
    main(folder1)