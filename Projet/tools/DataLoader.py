# -*- coding: utf-8 -*-

#####
# Céline ZHANG (zhac3201)
# Omar CHIDA (chim2708)
###

import csv
import numpy as np
from tools.DataSet import DataSet

class DataLoader:
    """
    Class that helps with data loading and management.
    """
    def __init__(self, filename,  class_col_name, excluded_features = set()):
        self.filename = filename
        self.features = []
        self.labels = []
        self.classes = []
        self.classes_to_index = {}
        self.class_col_name = class_col_name
        self.excluded_features = excluded_features
        self.excluded_features.add(class_col_name)
    
    def load(self):
        try:
            inputfile = open(self.filename, newline='')
        except FileNotFoundError:
            print(f"File {self.filename} not found.  Aborting")
        except OSError:
            print(f"OS error occurred trying to open {self.filename}")
        except Exception as err:
            print(f"Unexpected error opening {self.filename} is", repr(err))
        else:
            with inputfile:
                csv_data = csv.DictReader(inputfile)
                # Load the data
                for row in csv_data:
                    label = row[self.class_col_name]
                    if (label not in self.classes_to_index):
                        self.classes_to_index[label] = len(self.classes)
                        self.classes.append(label)
                    self.features.append([ v for k, v in row.items() if k not in self.excluded_features ])
                    self.labels.append(self.classes_to_index[label])
    
    def get_dataset(self):
        return DataSet(self.features, self.labels)

    def get_label_name(self, label):
        return self.classes[label]
