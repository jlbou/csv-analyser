# CSV Analyzer

A small [Streamlit](https://streamlit.io/) app that takes any CSV file and produces an instant statistical summary and a set of charts, without writing a single line of code. Built as a portfolio piece to demonstrate data analysis, data visualization, and app development with Python.

## Screenshots

> _Add your screenshots here. Suggested shots: overview with metrics, the statistics table, one of the charts, and the "Try it yourself" tab with an uploaded file._

![Overview](docs/screenshots/overview.png)
![Charts](docs/screenshots/charts.png)
![Try it yourself](docs/screenshots/try-it-yourself.png)

## Features

- **Demo tab**: preloaded sample dataset (`data/clients_purchases.csv`) with a full analysis ready to explore.
- **Try it yourself tab**: upload your own CSV and get the same analysis instantly.
- **Automatic summary**: row/column counts, duplicate count, missing values per column, and descriptive statistics.
- **Column inspector**: pick any column and see its data type, unique values, most frequent values, mean, median, and mode.
- **Charts**: sales by category, sales by region, sales over time, and age distribution (rendered only when the required columns are present).
- **Graceful error handling**: missing files, unreadable CSVs, or missing columns show a clear message instead of crashing the app.

## Project structure

```
CSV Analyzer/
├── app.py                  # Streamlit entry point (tabs, file upload, error handling)
├── ui.py                   # Shared rendering logic for both tabs
├── utils/
│   ├── loader.py            # CSV loading with error handling
│   ├── analysis.py          # Summary statistics and column inspection
│   └── charts.py             # Matplotlib/Seaborn chart generation
├── data/
│   └── clients_purchases.csv # Sample dataset used in the demo tab
└── requirements.txt
```

## Requirements

- Python 3.9+
- Dependencies listed in `requirements.txt`: `pandas`, `streamlit`, `matplotlib`, `seaborn`

## Installation

```bash
git clone <repo-url>
cd "CSV Analyzer"
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

This opens the app in your browser (by default at `http://localhost:8501`).

- Go to **Demonstration** to explore the analysis on the sample dataset right away.
- Go to **Try it yourself** to upload your own CSV.

To get the full set of charts when uploading your own file, it should include these columns: `age`, `category`, `region`, `total_purchase`, `purchase_date`, `quantity`. If a column is missing, the app skips that specific chart and shows a warning instead of failing.

## Known limitations

This is a portfolio/demo project, not a production tool. A few trade-offs worth mentioning:

- Column validation checks that required columns **exist**, but not that they contain the expected data type (e.g. a text column named `age` won't raise an error, it will just produce a meaningless chart).
- Chart sizing is fixed (`width=750`) rather than fully responsive to screen size.

## License

This project is available for portfolio/demonstration purposes.
