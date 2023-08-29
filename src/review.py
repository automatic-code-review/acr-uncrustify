import hashlib
import os
import re
import subprocess


def __check_regex_ignore(regexs, name):
    for regex in regexs:
        if re.search(regex, name):
            return True

    return False


def review(config):
    path_source = config['path_source']
    regex_file = config['regexFile']
    arquivo_config = config['config']
    regex_ignore = config['regexIgnore']

    comments = []

    for root, dirs, files in os.walk(path_source):
        for file in files:
            file_path = os.path.join(root, file)

            if re.search(regex_file, file_path) and not __check_regex_ignore(regex_ignore, file):
                if not __verificar_indentacao_arquivo(file_path, arquivo_config):
                    path_relative = file_path.replace(path_source, "")[1:]
                    comments.append({
                        "id": __generate_md5(file_path),
                        "comment": f"Indentação incorreta no arquivo {path_relative}",
                        "position": {
                            "language": "c++",
                            "path": path_relative,
                            "startInLine": 1,
                            "endInLine": 1,
                            "snipset": False
                        }
                    })

    return comments


def __verificar_indentacao_arquivo(arquivo, arquivo_config):
    comando = ['uncrustify', '-c', arquivo_config, '--check', arquivo]
    resultado = subprocess.run(comando, capture_output=True, text=True)

    return resultado.returncode == 0


def __generate_md5(string):
    md5_hash = hashlib.md5()
    md5_hash.update(string.encode('utf-8'))

    return md5_hash.hexdigest()
