Hi, welcome to this README, this has been my first data platform assignment. 

We were given the task to ingest, manipulate and work with data from a csv file through the use of Python, I had a bit of a rough start with setting up pandas, but once that was finally sorted I got to work to sort out the data.

First I ingested the data by doing: 
    df = pd.DataFrame(pd.read_csv("lab1_data.csv", sep=";"))
with the line of code I used, I was able to set up the data frame that I needed to work with through out the task, while looking through the csv file I noticed that a few values were missing across all the columns, there were white spaces through out "name" and "currency", and the there were two string values in "prices".

so I followed it up by making all the values in "prices" numeric while coercing the errors to agree by becomign null values.
I did so by doing: 
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

we were, tasked to flag down the values ther were wrong, missing value entries, numbers under 0 and then put them in a reject pile of sorts.
So I started with creating the flags and then defining the variable that was going to determine the rows that were going into the reject pile.
These are the flags I created:
    df["id missing"] = df["id"].isna()
    df["name missing"] = df["name"].isna()
    df["price missing"] = df["price"].isna()
    df["currency missing"] = df["currency"].isna()
    df["created_at missing"] = df["created_at"].isna()

then as stated I created the variable to use to sort out all the rejected values:
        reject_df = (
        (df["id missing"] == True)|
        (df["name missing"] == True)|
        (df["currency missing"] == True)|
        (df["created_at missing"] == True)|
        (df["price missing"] == True)|
        (df["price"] <= 0)
    )
if any of the flags were triggered it'd put the row that triggered the flag into the reject pile, as well as anything under 0.
by doing these lines of code:
    bad_df = df[reject_df].copy()
    good_df = df[~reject_df].copy()
which creates two branches of results which o so coincdently lines up with the bonus task of printing out the rejected values in a csv file, there may be an extra file but it has all of the correct results.
the lines for the two csv files:
    good_df.to_csv("fixed.csv")
    bad_df.to_csv("rejected_products.csv")

The next part of the task was to create new csv file with the price data analyzed. So using the good dataframe due to the fact that it has all the correct data, I got to work on getting the median price, the average price and amount of products with a price. Through the use of a utility method within the pandas structure I could get this data out.
These are the lines of code I used to get the result through the utility method:
    good_df["median_price"] = good_df["price"].median() 
    good_df["average_price"] = good_df["price"].mean() 
    good_df["amount"] = good_df["price"].count()

then with that going I needed to limit it down to 1 row, which through a bit of digging online I found my solution using the .query function in pandas, so I put the query function in, with a tiny bit a difficulty in the sense that it wanted to be made into a seperate variable.
    money_df = good_df.query("average_price > 0").iloc[0]

And with that done I wrote the code needed to output the csv file:
    money_df.to_csv("analytics_summary.csv")

But yeah thats all there is to say about the main body of code for this project, I know I struggled a bit with this but that mainly has been due to stress of a short deadline mixed with my first time messing around with mainly pandas.
Don't bother trusting the respository I kind of did most of the work in one session with a large amount of stress of the set up not working at the start. I programmed all of this without the use of chatGPT or any other ai for that matter, only asked for help from my classmates and teacher, mostly.