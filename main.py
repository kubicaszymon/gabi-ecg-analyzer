import re
import scipy.io
import os
import csv
import matplotlib.pyplot as plt
from collections import Counter

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

    # preprocess results as pairs of 0 - disease, 1 - ecg data
    results = []

    for path, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".hea"):
                with open(os.path.join(path, filename), "r") as f:
                    data = f.read()
                    match = re.search(r"#Dx:\s*([0-9,]+)", data)
                    if match:
                        dx_codes = match.group(1).split(',')

                mat_filename = os.path.join(path, os.path.splitext(filename)[0] + ".mat")
                if os.path.isfile(mat_filename):
                    mat = scipy.io.loadmat(mat_filename)
                    results.append((dx_codes, mat))

    all_diseases = []
    for diseases, data in results:
        all_diseases.extend(diseases)

    diseases_counts = Counter(all_diseases)
    plt.bar(diseases_counts.keys(), diseases_counts.values(), color='skyblue', edgecolor='black')
    plt.show()
    a = 3



