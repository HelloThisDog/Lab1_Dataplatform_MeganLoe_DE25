import pandas as pd

if __name__ == "__main__":

    df = pd.DataFrame(pd.read_csv("lab1_data.csv", sep=";"))

    df["id missing"] = df["id"].isna()
    df["name missing"] = df["name"].isna()
    df["price missing"] = df["price"].isna()
    df["currency missing"] = df["currency"].isna()
    df["created_at missing"] = df["created_at"].isna()

    df["name"] = df["name"].astype(str).str.strip()
    df["currency"] = df["currency"].str.strip()
    
    

    
    print(df)

    reject = (
        (df["id"] == ""),
        (df["name"] == ""),
        (df["currency"] == ""),
        (df["created_at"] == ""),
        (df["price"] == ""),
        (df["price"] <= 0)
    )

    df_reject = df[reject].copy()
    df_valid = df[~reject].copy()

    df_valid.to_csv("fixed.csv", index=False)