class FileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()


with FileOpener("file_task1.txt", "r") as f:
    content = f.read()
    print(content)