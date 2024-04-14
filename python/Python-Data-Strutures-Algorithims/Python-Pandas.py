import pandas as pd

df  = pd.read_csv('pokeman.csv')

print(df.head(6))

print(df.columns)

# print(df.to_dict())
# print(df.rpow(5))

# print(pd.options.display.max_rows)