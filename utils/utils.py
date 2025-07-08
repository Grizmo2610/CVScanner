
def reading_key(path: str):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            private_key_lines = [line.strip() for line in lines
                                    if not line.startswith('-----')]
            key = ''.join(private_key_lines)
        return key
    except FileNotFoundError:
        print(f"File '{path}' not found.")
    except Exception as e:
        print(f"Error reading file '{path}': {e}")