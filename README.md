## Using News to Predict Company Stock Movements

### Description

An end-to-end data collection to preprocessing to model training and evaluation with GloVe-CNN-LSTM and BERT-MLP to predict company stock movements using news articles and news sentiment polarity.

Driver notebooks at `/notebooks`.

For complete report & slide, navigate to `/reports`

### Flowchart

![Flowchart](https://github.com/Joeyipp/predict-stock-trends-news/blob/master/images/flowchart_design.png)

### System Architecture

![Flowchart](https://github.com/Joeyipp/predict-stock-trends-news/blob/master/images/model_design.png)

### Repository Structure

> `data`

- `/data` contains the news data. Due to the size of the datasets, it currently only has TSLA (Tesla) news data from 10/7/20 to 11/7/20 for the `/notebooks`. For the other datasets (AAPL and BA) as documented in `/reports`, please submit a pull request. Alternatively, you can self-collect using the `/notebooks/collect_data.py`.
- `/data/daily_TSLA.csv` contains the historical financial prices.
- `/data/news_TSLA.json` is the aggregated daily news data (for downstream experiments).

> `images`

- `/images` contains the images for the design flowchart and system architecture above.

> `notebooks`

- `/notebooks/collect_data.py` is the script to download news data from NewsAPI.org. Replace the `KEY` with your own API keys and modify the dates, query, sources, and ticker symbol to collect company news data.
- `/notebooks/CNN_LSTM_stock_trends_news.ipynb` is the notebook to run the GloVe-CNN-LSTM models.
- `/notebooks/BERT_stock_trends_news.ipynb` is the notebook to run the BERT models.

> `reports`

- `/reports/Final_Project_Report_YIP.pdf` is the written report for this project.
- `/reports/Final_Project_Presentation_Slide_YIP.pdf` is the presentation slide for this project.
