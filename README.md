**Data pipeline - CSV to API**<br> Aim of this project is to simulate reading large chunks of CSV files, processing them, and serving as API.<br>

Below are the tools used:

Data frame processing: Dask, Pandas<br>
Data testing: Great expectations<br>
Filetypes: Parquet, Sqlite, CSV<br>
API Serving:Fast API, Uvicorn<br>
API testing: Pytest<br>

To run the project, launch sh run.sh

Further Improvements:
* Adding a data orchestrator
* Wrapping with a container

Input is book_train.parquet folder to be stored in 'data' folder downloaded from [here][https://www.kaggle.com/competitions/optiver-realized-volatility-prediction/data?select=book_train.parquet]


