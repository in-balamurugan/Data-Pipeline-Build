from sqlalchemy import create_engine
from fastapi import FastAPI, Response
import pandas as pd
import uvicorn

engine = create_engine("sqlite:///book_data.db")
app = FastAPI()


@app.get("/")
async def get_data(stock, time_id):
    """
    Return the max diff value given the stock id and time id    
    """
    query = f"SELECT * FROM book_max_diff WHERE stock={stock} AND time_id={time_id}"
    df = pd.read_sql_query(query, engine)
    return df.to_dict()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
