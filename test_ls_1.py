
# Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и
# разархивирования с путями (x).

from task_1 import check_command
import pytest



 command = "ls /home/user/folder_ex"
 text = "file_1"



command = "tar -xf /home/user/folder_ex/archive.tar -C /home/user/folder_ex"
text = "file_1"

if __name__ == '__main__':
    pytest.main(['-vv'])
