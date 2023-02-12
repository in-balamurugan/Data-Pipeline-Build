import dask.dataframe as dd


def dask_pipeline():
    """dask_pipeline reads csv, finds the max value and writes back to csv"""
    df = dd.read_csv("data/book_csv/*.csv")
    df["bid_price_difference"] = df["bid_price1"] - df["bid_price2"]
    df_max = (
        df.groupby(["stock", "time_id"])["bid_price_difference"].max().reset_index()
    )
    df_max.to_csv("data/max_bid_prices.csv", single_file=True, index=False)
    return


if __name__ == "__main__":
    dask_pipeline()
