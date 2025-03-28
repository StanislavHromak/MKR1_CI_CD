def read_file(file_path):
    """Читання вмісту з текстового файлу та повернення набору рядків."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return set(line.strip() for line in file if line.strip())
    except FileNotFoundError:
        return set()