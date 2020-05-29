
import pandas as pd
import yfinance as yf

stock_str = "DD PFE PPL.TO GIB-A.TO PHG MRU.TO ABT BHP NTR.TO CVX E NVS GIL.TO SNC.TO PG BABA DHR CNR.TO BP MDLZ " \
               "CRM CAJ MG.TO TXN LLY RDS-A ETN ABB ASML INTC XOM MRK MDT APD SAP LIN SNY IMO.TO FNV.TO SAP.TO ADBE " \
               "EMR SU.TO PLD JNJ TOT EXC TRI.TO RIO NKE"

def get_historical_stock_data(stock_str, filepath_stockprice_df='../../data/raw/stock_price_df.pkl'):
    stock_price_df = yf.download(stock_str, start='2015-06-01', end='2020-05-08')
    stock_price_df.to_pickle(filepath_stockprice_df)
    return

def update_stock_price(stock_str, filepath_stockprice_df='../../data/raw/stock_price_df.pkl'):
    try:
        stock_price_df = pd.read_pickle(filepath_stockprice_df)
        last_date = stock_price_df.index[-1]
        
    except FileNotFoundError:
        print('No historical stock price information found! Try running the get_historical_stock_price function!')





if __name__ == "__main__":
    
