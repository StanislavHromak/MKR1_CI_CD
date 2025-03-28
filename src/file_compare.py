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


def find_different_lines(file1_path, file2_path):
    """Знаходить рядки, присутні лише в одному з файлів."""
    lines1 = read_file(file1_path)
    lines2 = read_file(file2_path)
    return lines1.symmetric_difference(lines2)


def write_to_file(lines, output_path):
    """Записує рядки у вихідний файл."""
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(sorted(lines)))


def compare_files(file1_path, file2_path, same_output='same.txt', diff_output='diff.txt'):
    """Основна функція для порівняння двох файлів і запису результатів."""
    common = find_common_lines(file1_path, file2_path)
    different = find_different_lines(file1_path, file2_path)

    write_to_file(common, same_output)
    write_to_file(different, diff_output)


if __name__ == "__main__":
    compare_files('file1.txt', 'file2.txt')