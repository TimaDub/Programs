from os import getenv, mkdir
import re


class Process:
    def __init__(self):
        self.path = fr"{getenv('APPDATA')}\.pitLauncher\launcher_properties.txt"
        self.folder_path = fr"{getenv('APPDATA')}\.pitLauncher\.PitLauncher"

    def rewrite_specific_line(self, line_number: int, new_line):
        with open(self.path, 'r') as file:
            lines = file.readlines()
        lines[line_number - 1] = new_line + '\n'
        with open(self.path, 'w') as file:
            file.writelines(lines)
        file.close()

    def save(self, slicer=':', **kwargs):
        with open(self.path, 'r+', encoding="utf-8") as properties:
            lines = properties.readlines()
            x = 0
            for key, value in kwargs.items():
                exist = False
                for line in lines:
                    if key in line:
                        exist = True
                if not exist:
                    properties.write(f"{key}{slicer} {value}\n")
            else:
                for line in lines:
                    x += 1
                    param = line.split(':')
                    for key, value in kwargs.items():
                        if key == param[0].replace(' ', ''):
                            self.rewrite_specific_line(x, new_line=f"{key}{slicer} {value}")
        properties.close()

    def load(self, parameter):
        try:
            with open(self.path, 'r', encoding="utf-8") as properties:
                lines = properties.readlines()
                for line in lines:
                    if parameter in line:
                        ret = line.split(':')[1]
                        ret = ret.replace(' ', '')
                        return ret.replace('\n', '')
            properties.close()
        except FileNotFoundError:
            try:
                mkdir(self.folder_path)
            except:
                pass
            with open(self.path, 'w', encoding="utf-8"):
                pass

    @staticmethod
    def replace_from_list(list_to_clear):
        cleaned_list = [item.lower() for item in list_to_clear if
                        "pre" not in item.lower() and "r" not in item.lower() and "w" not in item.lower()
                        and "a" not in item.lower() and "b" not in item.lower() and "infinite" not in item.lower()
                        and "snapshot" not in item.lower() and "i" not in item.lower() and "c" not in item.lower()]

        def version_key(version):
            parts = re.split(r'\.|-', version)
            return tuple(int(part) if part.isdigit() else 0 for part in parts)
        cleaned_list_ = [version for version in cleaned_list if version_key(version) != (0, 0, 0)]
        sorted_versions = sorted(cleaned_list_, key=version_key, reverse=True)
        return sorted_versions

    @staticmethod
    def sort_versions_list(list_to_sort):
        def version_key(version):
            parts = re.split(r'\.|-', version)
            return tuple(int(part) if part.isdigit() else 0 for part in parts)

        cleaned_list = [version for version in list_to_sort if version_key(version) != (0, 0, 0)]
        sorted_versions = sorted(cleaned_list, key=version_key, reverse=True)
        return sorted_versions

    @staticmethod
    def forge_version_sort(versions):
        def version_key(version):
            main_version, _, _ = version.partition('-')
            parts = main_version.split('.')
            numeric_parts = [int(part) for part in parts if part.isdigit()]
            return tuple(numeric_parts)

        sorted_versions = sorted(versions, key=version_key, reverse=True)
        filtered_versions = []
        seen_main_versions = set()
        main_versions_only = []
        all_versions_sorted = []

        for version in sorted_versions:
            main_version, _, _ = version.partition('-')
            parts = main_version.split('.')
            numeric_parts = tuple(int(part) for part in parts if part.isdigit())
            if numeric_parts not in seen_main_versions:
                seen_main_versions.add(numeric_parts)
                filtered_versions.append(version)
                main_versions_only.append(main_version)
            all_versions_sorted.append(version)

        return filtered_versions, main_versions_only, sorted(all_versions_sorted, key=version_key, reverse=True)