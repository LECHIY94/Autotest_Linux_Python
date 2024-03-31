# Дополнить проект тестами,
# проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).






import subprocess


def check_command(command, text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if result.returncode == 0 and text in out:
        return True
    else:
        return False


if __name__ == "__main__":
    check_command("cd /home/user/folder_ex; touch file_1", "")

