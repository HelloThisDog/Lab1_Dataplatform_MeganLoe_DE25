import pandas as pd

if __name__ == "__main__":

    df = pd.DataFrame(pd.read_csv("lab1_data.csv", sep=";"))

    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    df["name"] = df["name"].astype(str).str.strip()
    df["currency"] = df["currency"].str.strip()
    
    df["id missing"] = df["id"].isna()
    df["name missing"] = df["name"].isna()
    df["price missing"] = df["price"].isna()
    df["currency missing"] = df["currency"].isna()
    df["created_at missing"] = df["created_at"].isna()

    
    print(df)

    reject_df = (
        (df["id missing"] == True)|
        (df["name missing"] == True)|
        (df["currency missing"] == True)|
        (df["created_at missing"] == True)|
        (df["price missing"] == True)|
        (df["price"] <= 0)
    )

    
    bad_df = df[reject_df].copy()
    good_df = df[~reject_df].copy()

    good_df.to_csv("fixed.csv")

    bad_df.to_csv("rejected_values.csv")

