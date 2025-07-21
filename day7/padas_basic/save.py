import pandas as pd 

person = {
    "name":["ram","syam","ghansyam"],
    "age":[20,22,12],
    "city":["ayodhya","vrundavan","chapaya"]
}


df = pd.DataFrame(person)

df.to_csv("output.csv", index=False)
print(df)