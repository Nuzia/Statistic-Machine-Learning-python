import pandas as pd

df = pd.DataFrame({
    'NAMA': ["A", "B", "C", "D", "E"],
    'MTK': [7,6,8,9,8],
    'IPS': [5,4,5,6,7],
    'IPA': [8,4,5,6,7],
    'PKn': [8,9,7,9,9],
    'PJOK': [8,4,5,6,7]
})

print(df.std(numeric_only=True))
# print(df.quantile(numeric_only=True))
# print(df.median(numeric_only=True))