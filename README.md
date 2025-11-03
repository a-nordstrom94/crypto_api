# Crypto API Data Analysis
TLDR: Crypto data analysis project - fetches cryptocurrency data via API, transforms and analyzes it with Pandas, logs operations, and is fully Dockerized for easy setup and reproducibility.

OVERVIEW 

Crypto API Data Analysis is a python project that fetches cryptocurrency market data from  <a href="https://www.coingecko.com/en/api">CoinGecko API</a>  and performs data transformation and analysis using Pandas. The project is fully Dockerized for easy setup and includes a logging system to track operations and provide insights into the project flow, and for potential errors.

The goal is to provide a simple, reproducible pipeline to:
* Fetch cryptocurrency data
* Analyze top performers, losers, and volatility
* Compute market cap statistics
* Save results to CSV files
* Log process steps for transparency and debugging

PROJECT STRUCTURE
```
Crypto_project/
├─ Data/
│  ├─ Raw/           <-- Raw JSON data from API
│  └─ Processed/     <-- Processed CSV and TXT output
├─ Docker/
│  ├─ Dockerfile     <-- Docker setup
│  └─ requirements.txt  <-- For pip install
├─ Src/
│  ├─ main.py
│  └─ Crypto_functions/
│     ├─ __init__.py
│     ├─ crypto_api.py
│     ├─ crypto_transform.py
│     └─ logging_config.py
└─ Logs/             <-- Logs of processing
```

GETTING STARTED
Prerequisites
* Docker installed (recommended)
OR
* Python 3.11+ and pip (Not recommended)

Running with Docker (recommended)
1. docker build -t crypto_project -f Docker/dockerfile .
2. docker run --rm -v $(pwd)/Data:/app/Data -v $(pwd)/Logs:/app/Logs crypto_project
* CSV data will be saved to Data/Processed folder
* Logs will appear in Logs/ and some output in the console

Running with Python (optional)
1. Navigate to root
2. pip install -r Docker/requirements.txt
3. python -m Src.main

OUTPUTS
* CSV files: Processed inisghts are saved in Data/Processed/
* Log files: Detailed logs of all operations saved in Logs/
* Console output provides real-time progress update

FURTHER IMPROVEMENTS
* Allow user to specify target currency (currently USD fixed)
* Add more advanced Pandas analysis
* Schedule automated data fetching and analysis
