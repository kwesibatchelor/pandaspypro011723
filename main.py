import pandas as pd

column = ["NBS", "3C", "B&BLP", "Trust"]
titled_column = {"ticker": column}
data = pd.DataFrame(titled_column)
print(data)
