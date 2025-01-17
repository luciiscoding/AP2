import pandas as pd
from pandas_profiling import ProfileReport
df = pd.read_csv('tourism_dataset.csv')
profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
profile.to_file("tourism_dataset_report.html")

import pandas as pd
from pandas_profiling import ProfileReport


file_path = '/TemaPractica2/tourism_dataset.csv'

try:
    df = pd.read_csv(file_path)
    print("Setul de date a fost încărcat cu succes!")
except FileNotFoundError:
    print(f"Fișierul nu a fost găsit la locația: {file_path}")
    exit()

print("Primele rânduri din setul de date:")
print(df.head())
print("\nInformații despre date:")
print(df.info())


print("Generăm raportul Pandas Profiling...")
profile = ProfileReport(df, title="Tourism Dataset Profiling Report", explorative=True)


output_file = "tourism_dataset_report.html"
profile.to_file(output_file)
print(f"Raportul a fost generat și salvat ca {output_file}.")

