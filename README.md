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
which creates two branches of results which o so coincdently lines up wit ha bonus taks of printing out the rejected values in a csv file, there may be an extra file but it has all of the correct results.
the lines for the two csv files:
    good_df.to_csv("fixed.csv")
    bad_df.to_csv("rejected_products.csv")

The next part of the task was to create new csv files with the sorted data, here is where I may have changed things around a tiny bit. the file that we were required to make first was a file called "analytics_summary.csv", and in this file we need the median price, the average price and the amount of products with and without values. I put all the lines of code that related to this file above the flags or else it'd be a bit full with a lot of columns that weren't needed, which was all the flags.

So this is the code I used to get out the results needed in the csv file:
    df["median_price"] = df["price"].median() 
    df["average_price"] = df["price"].mean() 
    df["amount"] = df["price"].count()

It keeps repeating the results onto every row, but upon futher discussion with others, (my family who know a bit about programming), we came to the conclusion that it is supposed to do that as it is counting all the rows that have proper values, which is 50 rows out of 55. 
So with that result I wrote the code needed to output the csv file:
    df.to_csv("analytics_summary.csv")
And as I have stated about I've put this before the flags so that all the values are in.

But yeah thats all there is to say about the main body of code for this project, I know I struggled a bit with this but that mainly has been due to stress of a short deadline mixed with my first time messing around with mainly pandas. I'm pretty sure I missed the mark on this and need to redo this task, which just means it won't get done at all due to being put on the backburner. 
Don't bother trusting the respository I kind of did most of the work in one session with a large amount of stress of the set up not working at the start. I programmed all of this without the use of chatGPT or any other ai for that matter, only asked for help from my classmates and teacher, mostly.