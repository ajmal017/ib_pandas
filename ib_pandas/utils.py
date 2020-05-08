"""Helpers for data manipulation"""
import csv

# import os


def load_file(filename):
    """Reads a CSV file and returns a list"""
    filepath = filename
    data = []
    with open(filepath) as file_stream:
        reader = csv.DictReader(file_stream)
        for line in reader:
            data.append(line)
        return data
