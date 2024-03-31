# • Установить пакет для расчёта crc32
# sudo apt install libarchive-zip-perl
# • Доработать проект, добавив тест команды расчёта хеша (h).
# Проверить, что хеш совпадает с рассчитанным командой crc32.

from task_1 import check_command
import hashlib
import pytest

if __name__ == "__main__":
    filename = "/home/user/folder_ex/file_1"
    command = f"crc32 {filename}"
    expected_hash = hashlib.crc32(open(filename, 'rb').read()) & 0xffffffff


if __name__ == '__main__':
    pytest.main(['-vv'])