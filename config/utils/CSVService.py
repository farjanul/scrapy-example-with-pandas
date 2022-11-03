import csv
import os
from typing import Any


class CSVService:
    """
    This is the service class for CSV file.
    """

    def __init__(self, filename, fieldnames):
        """
        @param filename: name of the CSV file
        @param fieldnames: column names of the CSV file
        """
        self.check_directory()
        self.filename = filename
        self.fp = open(self.filename, 'w', newline='')
        self.writer = csv.DictWriter(self.fp, fieldnames=fieldnames)
        self.writer.writeheader()

    def close(self):
        """Close the CSV file"""
        self.fp.close()

    def write(self, elems):
        """Write the given data to the CSV file"""
        self.writer.writerow(elems)

    def size(self) -> int:
        """Get the size of the CSV file"""
        return os.path.getsize(self.filename)

    @staticmethod
    def check_directory():
        """Check the directory, if exist otherwise create a directory."""
        if not os.path.exists('output'):
            os.makedirs('output')

    def delete(self):
        """Delete a CSV file"""
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def filename(self) -> str:
        """Get the CSV file name"""
        return self.filename
