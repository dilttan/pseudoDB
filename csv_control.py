import pandas as pd
import os
import csv

csv_data = {}

def get_column(csv_name):
  global csv_data

  return csv_data[csv_name].columns.to_list()

def get_index(csv_name):
  global csv_data

  return csv_data[csv_name].index.to_list()

def new(csv_name, columns_list):
  global csv_data

  file_list = os.listdir('./csv_db')
  if f"{csv_name}.csv" in file_list:
    return False

  with open(f'csv_db/{csv_name}.csv', 'w') as new_csv:
    input_column = '|'.join(['index']+columns_list) + '\n'

    new_csv.write(input_column)

  csv_data[csv_name] = pd.read_csv(f"csv_db/{csv_name}.csv", index_col=0, sep='|')

  return True

def append(csv_name, idx, *input_list):
  global csv_data

  columns = csv_data[csv_name].columns
  add_column = pd.DataFrame([input_list], columns=columns, index=[idx])
  csv_data[csv_name] = csv_data[csv_name].append(add_column)
  
  csv_data[csv_name].to_csv(f"csv_db/{csv_name}.csv", sep='|')

def read_all(csv_name):
  global csv_data

  return csv_data[csv_name]

def read_one(csv_name, idx):
  global csv_data

  try:
    result = csv_data[csv_name].loc[idx]
  except:
    result = None

  return result

def read_dot(csv_name, idx, column):
  global csv_data

  try:
    result = csv_data[csv_name].loc[idx, column]
  except:
    result = None

  return result

def read_select(csv_name, column_index, value):
  global csv_data
  
  try:
    df = csv_data[csv_name]
    result = df[df[column_index] == value]
  except:
    result = None

  return result

def update(csv_name, idx, column, data):
  global csv_data

  csv_data[csv_name].loc[idx, column] = data
  csv_data[csv_name].to_csv(f"csv_db/{csv_name}.csv", sep='|')

def delete(csv_name, idx):
  global csv_data

  csv_data[csv_name] = csv_data[csv_name].drop(idx)
  csv_data[csv_name].to_csv(f"csv_db/{csv_name}.csv", sep='|') # ['']

def main():
  global csv_data

  file_list = os.listdir('./csv_db')
  for file_name in file_list:
    if file_name[-3:] == 'csv':
      csv_data[file_name[:-4]] = pd.read_csv(f"csv_db/{file_name}", index_col=0, sep='|')

  print(csv_data)

main()
