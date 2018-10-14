import csv
import os
import pathlib
import shutil

i = 0
boostCol = 0
isGarbage = True

if not os.path.isdir("./Garbage"):
    pathlib.Path('./Garbage').mkdir(parents = True, exist_ok = True)

for filename in os.listdir(os.getcwd()):
    if (filename.endswith(".csv")):
        with open(filename, 'r') as f:
            reader = csv.reader(f)

            data = list(reader)
            freq = (float(data[len(data) - 1][0]) - float(data[1][0])) / (len(data) - 1)
            numRows = int(1.5 / freq)

            for num in range(0, len(data[0])):
                if ((data[0][num]) == "Boost (PSI)"):
                    boostCol = num

            for num in range(1, len(data)):
                print(float(data[num][boostCol]))
                if (float(data[num][2]) >= 50):
                    i += 1
                if (float(data[num][boostCol]) > 2.0):
                    isGarbage = False

            if (os.path.getsize(filename) < 10240):
                if (isGarbage == True): #i < numRows):
                    shutil.move(filename, "./Garbage")

            i = 0
            isGarbage = True