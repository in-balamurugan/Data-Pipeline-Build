import great_expectations as ge
import pandas as pd
from sqlalchemy import create_engine


class ColumnsMissing(Exception):
    pass


def check_columns_exists():
    """check_columns_exists checks if expected columns are present after aggregation"""
    columns = ["stock", "time_id", "bid_price_difference"]
    df = ge.read_csv("data/max_bid_prices.csv")

    for col in columns:
        if df.expect_column_to_exist(col)["success"] == False:
            return False
    return True


def write_sqlite():
    """write_sqlite writes to sqlite file"""
    df = pd.read_csv("data/max_bid_prices.csv")
    engine = create_engine("sqlite:///data/book_data.db", echo=True)
    df.to_sql("book_max_diff", con=engine, if_exists="replace")


if __name__ == "__main__":
    if check_columns_exists():
        write_sqlite()
    else:
        raise ColumnsMissing(
            "Columns in max_bid_prices.csv doesn't match the expected columns \{'stock','time_id','bid_price_difference'\} "
        )
