def read_file(file_path):
    """Читання вмісту з текстового файлу та повернення набору рядків."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return set(line.strip() for line in file if line.strip())
    except FileNotFoundError:
        return set()


def find_common_lines(file1_path, file2_path):
    """Знаходить рядки в обох файлах."""
    lines1 = read_file(file1_path)
    lines2 = read_file(file2_path)
    return lines1.intersection(lines2)
