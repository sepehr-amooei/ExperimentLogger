import csv
import pickle
from openpyxl import Workbook
import pandas as pd

def export_csv(data, filepath):
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def export_excel(data, filepath):
    wb = Workbook()
    ws = wb.active
    for row in data:
        ws.append(row)
    wb.save(filepath)

def load_pickle(filepath):
    with open(filepath, 'rb') as file:
        return pickle.load(file)

def save_pickle(obj, filepath):
    with open(filepath, 'wb') as file:
        pickle.dump(obj, file)

def load_csv_as_df(filepath):
    return pd.read_csv(filepath)