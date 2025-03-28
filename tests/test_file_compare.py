import pytest
import os
from src.file_compare import read_file, find_common_lines, find_different_lines, write_to_file

@pytest.fixture
def temp_files(tmp_path):
    file1 = tmp_path / "test_file1.txt"
    file2 = tmp_path / "test_file2.txt"
    file1.write_text("a\nb\nc\n")
    file2.write_text("b\nc\nd\n")
    return str(file1), str(file2)

@pytest.mark.parametrize("content,expected", [
    ("a\nb\nc\n", {"a", "b", "c"}),
    ("", set()),
    ("\n\n", set())
])

def test_read_file(tmp_path, content, expected):
    """Тест функції, що читає вміст з текстового файлу та повертає набір рядків."""
    test_file = tmp_path / "test.txt"
    test_file.write_text(content)
    assert read_file(str(test_file)) == expected


def test_write_to_file(tmp_path):
    """Тест для функції, що записує рядки у вихідний файл."""
    output = tmp_path / "output.txt"
    lines = {"a", "b"}
    write_to_file(lines, str(output))
    assert output.read_text() == "a\nb"