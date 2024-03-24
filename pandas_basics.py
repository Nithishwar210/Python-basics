import pandas as pd

fruits = {
    'apple': [0, 1, 1, 2],
    'orange': [2, 3, 1, 1],
}

df = pd.DataFrame(fruits)

print(df)

df = pd.read_csv("weather_data.csv")
