import pandas as pd


def write_csv():
    """
    write_csv reads all parquets,slices data and writes to csv
    """
    full_df = pd.DataFrame()

    for i in range(127):
        try:
            df = pd.read_parquet("data/book_parquet/stock_id=" + str(i) + "/")

            df["stock"] = i
            if i % 10 == 0:
                full_df.to_csv("data/book_csv/book_train_" + str(i) + ".csv")
                full_df = pd.DataFrame()

            full_df = pd.concat([full_df, df])
            print(full_df.shape)

        except FileNotFoundError:
            pass


if __name__ == "__main__":
    write_csv()
