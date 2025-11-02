import scipy.io
import os
import csv

def fill_diseases(path):
    diseases = {}
    with open(path, newline='') as csvfile:
        line = csv.reader(csvfile, delimiter=',')
        for row in line:
            if row[2][0].isdigit():
                diseases[row[2]] = row[1]

    return diseases

if __name__ == '__main__':
    snomed_path = "ConditionNames_SNOMED-CT.csv"
    diseases = fill_diseases(snomed_path)

    directory = r"example"

    for path, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".hea"):
                with open(os.path.join(path, filename), "r") as f:
                    data = f.read()

                mat_filename = os.path.join(path, os.path.splitext(filename)[0] + ".mat")
                if os.path.isfile(mat_filename):
                    mat = scipy.io.loadmat(mat_filename)
                    a = 3





