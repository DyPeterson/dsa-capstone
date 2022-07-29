# Import the required Libraries
import pandas as pd
from pandas import DataFrame
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter.filedialog import askopenfile
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip

def open_file():
   file = filedialog.askopenfile(mode='r', filetypes=[('CSV File', '*.csv')])
   if file:
      global filepath
      filepath = os.path.abspath(file.name)
      # Label(win, text="The File is located at : " + str(filepath)).pack()
      file_label.config(text="The File is located at : \n" + str(filepath))

def csv_to_dataframe(filepath:str) -> None:
   """
   ### Load a csv file into a pandas dataframe.

   Returns inserted csv into 'df' variable.

   - filepath: string of filepath to csv file.
   """
   global df
   df = pd.read_csv(filepath, header=0)
   
def details(df:DataFrame):
   """
   Prints Stats of a dataframe, Returning columns, the shape and datatypes of the columns
   """
   details_text.insert('end',
   f"""
   Columns: {list(df.columns)}
   Shape: {df.shape[0]} Rows, {df.shape[1]} Columns
   Data Types: {list(df.dtypes)}
   """)
   details_text.grid(row=5,column=0,padx=5,pady=5)
   sb.grid(sticky=E)
   details_text.config(state='disabled', yscrollcommand=sb.set)

def remove_new_line_char(df:DataFrame) -> DataFrame:
   """
   Removes new lines from dataframe.
   """
   df.replace('\n','', regex=True, inplace=True)

def nullfill(df:DataFrame, fill_val) -> None:
    """
    Targets empty fields of a dataframe and sets them to the fill_val
    """    
    df.fillna(value=fill_val, axis=1, inplace=True)

def index_setter(df:DataFrame, index) -> None:
    """
    Sets the index of dataframe to a desired existing column
        - df: dataframe to have index changed
        - index: name of column that index will be set to
    """
    df.set_index(index, inplace=True)

def drop_low_data(df:DataFrame, threshold=2) -> None:
    """
    Drops dataframe row if missing more than x(threshold) values, Default is 2 
    """
    df.dropna(thresh=threshold, inplace=True)

def duplicate_drop(df:DataFrame, col_list=None) -> None:
    """
    drop duplicate rows targeting a specific column(s)
    col_list: ['column1', 'column2']
    - Enter column name as a string
    - Only 1 column required, if none set uses all columns
    - Enter multiple columns as strings seperated by commas in a list
    - eg: duplicate drop(dataframe, ['col1', 'col2'])
    """
    df.drop_duplicates(subset=[col_list], inplace=True)

def drop_extra_columns(df:DataFrame, num_cols):
    """
    Drops dataframe columns if dataframe has more than <num_cols> columns
    """
    df.drop(df.columns[num_cols:])

def save_csv(dataframe):
   """
   Save pandas dataframe as CSV file.
   """
   saving_path = filedialog.asksaveasfile(mode='w', defaultextension=".csv")
   if saving_path:
      dataframe.to_csv(saving_path)

# Create an instance of tkinter window
win = ttk.Window(themename="superhero")
win.title("CSV Pipeline")

# Set the geometry of tkinter frame
win.geometry("600x600")

# Add a Label widget
upload_label = Label(win, text="Select CSV to upload")
upload_label.grid(row=0, column=0,padx=5,pady=5)

# File browser, returns filepath
file_b = ttk.Button(
   win,
   text="Browse", 
   command=open_file, 
   bootstyle=PRIMARY
)
file_b.grid(row=1,column=0,padx=5,pady=5)
ToolTip(file_b, text= "Select CSV to load into program", bootstyle=LIGHT)


file_label = Label(win, text="The File is located at : ")
file_label.grid(row=2,column=0,padx=5,pady=5)
# Create dataframe in pandas for transformations
data_frame_b = ttk.Button(
   win,
   text="Create Dataframe",
   command=lambda: csv_to_dataframe(filepath),
   bootstyle=PRIMARY
)
data_frame_b.grid(row=3,column=0,padx=5,pady=5)
ToolTip(data_frame_b, text="Load the CSV file into a pandas dataframe", bootstyle=LIGHT)

# list details of df
details_b = ttk.Button(
   win,
   text="Display Details of Dataframe",
   command=lambda: details(df),
   bootstyle=PRIMARY
)
details_b.grid(row=4,column=0,padx=5,pady=5)
ToolTip(details_b, text="Displays stats of a dataframe, Returning columns, the shape and datatypes of the columns", bootstyle=LIGHT)

# TEXT BOX FOR DETAILS DISPLAY w/ SCROLL BAR
frame = ttk.Labelframe(win)
details_text = ttk.Text(frame, height = 5, width = 80, wrap='word')
sb = Scrollbar(frame)
sb.config(command=details_text.yview)
frame.grid(row=5,column=0,padx=5,pady=5)

# Data Cleaning label
data_clean_label = Label(win, text="Data Cleaning:", font=("Arial", 16))
data_clean_label.grid(row=0, column=2, padx=5, pady=5)

#nullfill

nullfill_entry= ttk.Entry(win, width=30)
nullfill_entry.focus_set()
nullfill_entry.grid(row=1, column=2, padx=5, pady=5)

null_b = ttk.Button(
   win,
   text="Fill Null Values",
   command=lambda: nullfill(df, nullfill_entry.get()),
   bootstyle=PRIMARY
)
null_b.grid(row=2, column=2, padx=5, pady=5)
ToolTip(null_b, text="Fill empty fields of a dataframe and sets them to the inputted value", bootstyle=LIGHT)

# Index Setter
index_entry= ttk.Entry(win, width=25)
index_entry.focus_set()
index_entry.grid(row=3, column=2, padx=5, pady=5)

index_b = ttk.Button(
   win,
   text="Set index",
   command=lambda: index_setter(df, index_entry.get()),
   bootstyle=PRIMARY
)
index_b.grid(row=4, column=2, padx=5, pady=5)
ToolTip(index_b, text="Sets the index of dataframe to inputted column name", bootstyle=LIGHT)

# Low data drop
label_low_data = Label(win, text="Enter minimum number of datapoints to keep")
label_low_data.grid(row=5, column=2, padx=5, pady=5)

low_data_entry= ttk.Entry(win, width=5)
low_data_entry.focus_set()
low_data_entry.grid(row=6, column=2, padx=5, pady=5)

low_data_b = ttk.Button(
   win,
   text="Drop Low Data",
   command=lambda: drop_low_data(df, int(low_data_entry.get())),
   bootstyle=PRIMARY
)
low_data_b.grid(row=7, column=2, padx=5, pady=5)
ToolTip(low_data_b, text="Drops a row if missing more than inputted value amount of data, Default is 2", bootstyle=LIGHT)

# drop duplicates
drop_dupes_label = Label(win, text="Drop Duplicate Entries")
drop_dupes_label.grid(row=8, column=2, padx=5, pady=5)

drop_dupes_entry = ttk.Entry(win, width=10)
drop_dupes_entry.focus_set()
drop_dupes_entry.grid(row=9, column=2, padx=5, pady=5)

drop_dupes_b = ttk.Button(
   win,
   text="Drop Duplicates",
   command=lambda: duplicate_drop(df, drop_dupes_entry.get()),
   bootstyle=PRIMARY
)
drop_dupes_b.grid(row=10, column=2, padx=5, pady=5)
ToolTip(drop_dupes_b, text="Drop duplicate values from columns. In the entry field insert list of columns to target separated by commas. Surrounded by quotes ex: 'col1', 'col2'", bootstyle=LIGHT)

# drop extra columns
drop_extra_col_label = Label(win, text="Drop extra columns")
drop_extra_col_label.grid(row=11, column=2, padx=5, pady=5)

drop_extra_col_entry = ttk.Entry(win, width=5)
drop_extra_col_entry.focus_set()
drop_extra_col_entry.grid(row=12, column=2, padx=5, pady=5)

drop_extra_col_b = ttk.Button(
   win,
   text="Set number of columns",
   command=lambda: drop_extra_columns(df, int(drop_extra_col_entry.get())),
   bootstyle=PRIMARY
)
drop_extra_col_b.grid(row=13, column=2, padx=5, pady=5)
ToolTip(drop_extra_col_b, text="Insert the number of desired columns, useful if you have extra columns from a CSV that you would like drop", bootstyle=LIGHT)

# write csv
save_file_b = ttk.Button(
   win,
   text="Save as CSV",
   command=lambda: save_csv(df),
   bootstyle=PRIMARY
)
save_file_b.grid(row=8, column=0, padx=5, pady=5)


if __name__ == "__main__":
    win.mainloop()