import csv
import os


class CSVService:

    def __init__(self, filename, fieldnames):
        self.check_directory()
        self.filename = filename
        self.fp = open(self.filename, 'w', newline='')
        self.writer = csv.DictWriter(self.fp, fieldnames=fieldnames)
        self.writer.writeheader()

    def close(self):
        self.fp.close()

    def write(self, elems):
        self.writer.writerow(elems)

    def size(self):
        return os.path.getsize(self.filename)

    def to_dict(self):
        lst = [*csv.DictReader(open(self.filename, 'r'))]
        return lst

    @staticmethod
    def check_directory():
        if not os.path.exists('output'):
            os.makedirs('output')

    def delete(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def filename(self):
        return self.filename
