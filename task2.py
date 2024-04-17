from contextlib import contextmanager

@contextmanager
def file_opener(filename, mode):
    file = None
    try:
        file = open(filename, mode)
        yield file
    finally:
        if file:
            file.close()

# Приклад використання:
with file_opener("file_task1.txt", "r") as f:
    content = f.read()
    print(content)