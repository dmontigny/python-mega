
import time
import os
import pandas as pd

path = "files/temps_today.csv"
while True:
    if os.path.exists(path):
        df = pd.read_csv(path)
        print(df.mean())
    else:
        print("File does not exist")
    time.sleep(2)

