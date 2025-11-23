import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

def fetch_data():
    """
    Fetches 30 days of OHLC data for Bitcoin from CoinGecko.
    Returns a list of lists: [timestamp, open, high, low, close]
    """
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/ohlc"
    params = {
        "vs_currency": "usd",
        "days": "30"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        print(f"Successfully fetched {len(data)} data points.")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def process_data(data):
    """
    Converts raw data to a DataFrame, formats timestamps, and calculates volatility.
    """
    if not data:
        return None
    
    df = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close"])
    
    # Convert timestamp to datetime
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
    
    # Calculate Daily Volatility
    df["volatility"] = df["high"] - df["low"]
    
    return df

def visualize_data(df):
    """
    Plots Closing Price and Volatility trends.
    """
    if df is None:
        print("No data to visualize.")
        return

    sns.set_theme(style="darkgrid")
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
    
    # Plot Closing Price
    sns.lineplot(data=df, x="date", y="close", ax=ax1, color="blue", marker="o")
    ax1.set_title("Bitcoin Closing Price (Last 30 Days)", fontsize=16)
    ax1.set_ylabel("Price (USD)", fontsize=12)
    
    # Plot Volatility
    sns.lineplot(data=df, x="date", y="volatility", ax=ax2, color="red", marker="o")
    ax2.set_title("Bitcoin Daily Volatility (High - Low)", fontsize=16)
    ax2.set_xlabel("Date", fontsize=12)
    ax2.set_ylabel("Volatility (USD)", fontsize=12)
    
    plt.tight_layout()
    
    # Save the plot
    filename = "market_trend.png"
    plt.savefig(filename)
    print(f"Plot saved as {filename}")
    
    # Show the plot (optional, might not work in all environments but good to have)
    # plt.show()

def main():
    print("Starting Market Data Analyzer...")
    
    # 1. Fetch Data
    raw_data = fetch_data()
    
    # 2. Process Data
    df = process_data(raw_data)
    
    if df is not None:
        print("\nData Preview:")
        print(df.head())
        print("\nData Statistics:")
        print(df.describe())
        
        # 3. Visualize Data
        visualize_data(df)
        print("\nAnalysis Complete.")
    else:
        print("Analysis failed due to missing data.")

if __name__ == "__main__":
    main()
