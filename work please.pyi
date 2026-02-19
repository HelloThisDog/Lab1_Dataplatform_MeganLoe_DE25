import pandas as pd

if __name__ == "__main__":

    df = pd.DataFrame(pd.read_csv("lab1_data.csv", sep=";"))

    df["id missing"] = df["id"].isna()
    df["name missing"] = df["name"].isna()
    df["price missing"] = df["price"].isna()
    df["currency missing"] = df["currency"].isna()
    df["created_at missing"] = df["created_at"].isna()

    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    df["name"] = df["name"].astype(str).str.strip()
    df["currency"] = df["currency"].str.strip()
    
    

    
    print(df)

    reject_df = (
        (df["id missing"] == "true"),
        (df["name missing"] == "true"),
        (df["currency missing"] == "true"),
        (df["created_at missing"] == "true"),
        (df["price missing"] == "true"))

    #bad_df = df[reject_df].copy()
    #good_df = df[~reject_df].copy()

    #good_df.to_csv("fixed.csv")