import pandas as pd

if __name__ == "__main__":

    df = pd.DataFrame(pd.read_csv("lab1_data.csv", sep=";")) #read file
    
    df["price"] = pd.to_numeric(df["price"], errors="coerce") #force all values to be numbers

    #cleans the white space
    df["name"] = df["name"].astype(str).str.strip()
    df["currency"] = df["currency"].str.strip()

    #counts up the avarage and median, as well as valid entries
    df["median_price"] = df["price"].median() 
    df["average_price"] = df["price"].mean() 
    df["amount"] = df["price"].count() #counts the correct amount 50 out of 55 rows
    
    df.to_csv("analytics_summary.csv") #putting this here so becuase all values have been asked to be shown

    #flags for null values
    df["id missing"] = df["id"].isna()
    df["name missing"] = df["name"].isna()
    df["price missing"] = df["price"].isna()
    df["currency missing"] = df["currency"].isna()
    df["created_at missing"] = df["created_at"].isna()
    
    #the net to catch all of the null values and anything under zero
    reject_df = (
        (df["id missing"] == True)|
        (df["name missing"] == True)|
        (df["currency missing"] == True)|
        (df["created_at missing"] == True)|
        (df["price missing"] == True)|
        (df["price"] <= 0)
    )


    #creates the csvs, based on the results from the net
    bad_df = df[reject_df].copy()
    good_df = df[~reject_df].copy()
    
    #puts out the diffrent csvs
    good_df.to_csv("fixed.csv") #everything with the correct value

    bad_df.to_csv("rejected_products.csv") #everything with the wrong values

    






