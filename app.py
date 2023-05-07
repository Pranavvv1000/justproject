from flask import Flask, jsonify , Response,render_template
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
from datetime import date
from datetime import timedelta

app = Flask(__name__)

# Define the stock symbol and start and end dates
stock_symbol_rel = 'RELIANCE.NS'
stock_symbol_tata = 'TATAMOTORS.NS'
stock_symbol_icici = 'ICICIBANK.NS'
stock_symbol_hdfc = 'HDFCBANK.NS'
stock_symbol_axis = 'AXISBANK.NS'
today = date.today()
start_date = today - timedelta(days = 60)
end_date = today - timedelta(days = 1)


# Retrieve historical data for the stock
stock_data_rel = yf.download(stock_symbol_rel, start=start_date, end=end_date)
stock_data_tata = yf.download(stock_symbol_tata, start=start_date, end=end_date)
stock_data_icici = yf.download(stock_symbol_icici, start=start_date, end=end_date)
stock_data_hdfc = yf.download(stock_symbol_hdfc, start=start_date, end=end_date)
stock_data_axis = yf.download(stock_symbol_axis, start=start_date, end=end_date)

# Calculate moving averages for 50 and 200 days
stock_data_rel['MA50'] = stock_data_rel['Close'].rolling(window=50).mean()
stock_data_rel['MA200'] = stock_data_rel['Close'].rolling(window=200).mean()
# Calculate moving averages for 50 and 200 days
stock_data_tata['MA50'] = stock_data_tata['Close'].rolling(window=50).mean()
stock_data_tata['MA200'] = stock_data_tata['Close'].rolling(window=200).mean()
# Calculate moving averages for 50 and 200 days
stock_data_icici['MA50'] = stock_data_icici['Close'].rolling(window=50).mean()
stock_data_icici['MA200'] = stock_data_icici['Close'].rolling(window=200).mean()
# Calculate moving averages for 50 and 200 days
stock_data_hdfc['MA50'] = stock_data_hdfc['Close'].rolling(window=50).mean()
stock_data_hdfc['MA200'] = stock_data_hdfc['Close'].rolling(window=200).mean()
# Calculate moving averages for 50 and 200 days
stock_data_axis['MA50'] = stock_data_axis['Close'].rolling(window=50).mean()
stock_data_axis['MA200'] = stock_data_axis['Close'].rolling(window=200).mean()

# Calculate the Relative Strength Index (RSI) and the Moving Average Convergence Divergence (MACD)


def calculate_technical_indicators_rel(data):
    delta = data['Close'].diff()
    delta= delta[1:]

    up = delta.copy()
    up[up < 0] = 0

    down = delta.copy()
    down[down > 0] = 0

    AVG_Gain = up.rolling(window=14).mean()
    AVG_Loss = abs(down.rolling(window=14).mean())

    RS = AVG_Gain/AVG_Loss
    RSI_rel = 100.0 - (100.0 / (1.0 + RS))

    exp1 = data['Close'].ewm(span=12, adjust=False).mean()
    exp2 = data['Close'].ewm(span=26, adjust=False).mean()

    MACD_rel = exp1 - exp2
    signal_rel = MACD_rel.ewm(span=9, adjust=False).mean()

    return RSI_rel, MACD_rel, signal_rel





# Calculate the Relative Strength Index (RSI) and the Moving Average Convergence Divergence (MACD)


def calculate_technical_indicators_tata(data):
    delta = data['Close'].diff()
    delta= delta[1:]

    up = delta.copy()
    up[up < 0] = 0

    down = delta.copy()
    down[down > 0] = 0

    AVG_Gain = up.rolling(window=14).mean()
    AVG_Loss = abs(down.rolling(window=14).mean())

    RS = AVG_Gain/AVG_Loss
    RSI_tata = 100.0 - (100.0 / (1.0 + RS))

    exp1 = data['Close'].ewm(span=12, adjust=False).mean()
    exp2 = data['Close'].ewm(span=26, adjust=False).mean()

    MACD_tata = exp1 - exp2
    signal_tata = MACD_tata.ewm(span=9, adjust=False).mean()

    return RSI_tata, MACD_tata, signal_tata



# Calculate the Relative Strength Index (RSI) and the Moving Average Convergence Divergence (MACD)


def calculate_technical_indicators_icici(data):
    delta = data['Close'].diff()
    delta = delta[1:]

    up = delta.copy()
    up[up < 0] = 0

    down = delta.copy()
    down[down > 0] = 0

    AVG_Gain = up.rolling(window=14).mean()
    AVG_Loss = abs(down.rolling(window=14).mean())

    RS = AVG_Gain/AVG_Loss
    RSI_icici = 100.0 - (100.0 / (1.0 + RS))

    exp1 = data['Close'].ewm(span=12, adjust=False).mean()
    exp2 = data['Close'].ewm(span=26, adjust=False).mean()

    MACD_icici = exp1 - exp2
    signal_icici = MACD_icici.ewm(span=9, adjust=False).mean()

    return RSI_icici, MACD_icici, signal_icici



# Calculate the Relative Strength Index (RSI) and the Moving Average Convergence Divergence (MACD)


def calculate_technical_indicators_hdfc(data):
    delta = data['Close'].diff()
    delta= delta[1:]

    up = delta.copy()
    up[up < 0] = 0

    down = delta.copy()
    down[down > 0] = 0

    AVG_Gain = up.rolling(window=14).mean()
    AVG_Loss = abs(down.rolling(window=14).mean())

    RS = AVG_Gain/AVG_Loss
    RSI_hdfc = 100.0 - (100.0 / (1.0 + RS))

    exp1 = data['Close'].ewm(span=12, adjust=False).mean()
    exp2 = data['Close'].ewm(span=26, adjust=False).mean()

    MACD_hdfc = exp1 - exp2
    signal_hdfc = MACD_hdfc.ewm(span=9, adjust=False).mean()

    return RSI_hdfc, MACD_hdfc, signal_hdfc




# Calculate the Relative Strength Index (RSI) and the Moving Average Convergence Divergence (MACD)


def calculate_technical_indicators_axis(data):
    delta = data['Close'].diff()
    delta= delta[1:]

    up = delta.copy()
    up[up < 0] = 0

    down = delta.copy()
    down[down > 0] = 0

    AVG_Gain = up.rolling(window=14).mean()
    AVG_Loss = abs(down.rolling(window=14).mean())

    RS = AVG_Gain/AVG_Loss
    RSI_axis = 100.0 - (100.0 / (1.0 + RS))

    exp1 = data['Close'].ewm(span=12, adjust=False).mean()
    exp2 = data['Close'].ewm(span=26, adjust=False).mean()

    MACD_axis = exp1 - exp2
    signal_axis = MACD_axis.ewm(span=9, adjust=False).mean()

    return RSI_axis, MACD_axis, signal_axis



RSI_rel, MACD_rel, signal_rel = calculate_technical_indicators_rel(stock_data_rel)
RSI_tata, MACD_tata, signal_tata = calculate_technical_indicators_tata(stock_data_tata)
RSI_icici, MACD_icici, signal_icici = calculate_technical_indicators_icici(stock_data_icici)
RSI_hdfc, MACD_hdfc, signal_hdfc = calculate_technical_indicators_hdfc(stock_data_hdfc)
RSI_axis, MACD_axis, signal_axis = calculate_technical_indicators_axis(stock_data_axis)


@app.route('/reliance')
def reliance():
    
    output = ""
    if stock_data_rel['Close'][-1] > stock_data_rel['MA50'][-1] and stock_data_rel['MA50'][-1] > stock_data_rel['MA200'][-1]:
        output += f"RELIANCE is currently in an uptrend or in bullish Market.In a bull market, the ideal thing for an investor to do is to take advantage of rising prices by buying stocks early in the trend (if possible) and then selling them when they have reached their peak."
        output += "Tip:This is only Suggestion,Invest on your own Risk."

    elif stock_data_rel['Close'][-1] < stock_data_rel['MA50'][-1] and stock_data_rel['MA50'][-1] < stock_data_rel['MA200'][-1]:
        output += f"RELIANCE is currently in a downtrend or in Bearish Market.Invest for the long term Smart investors understand that the stock market is cyclical and that bear markets are a natural part of the cycle. Therefore, they focus on the long-term outlook for their investments rather than short-term fluctuations in stock prices.\n"
        output += "Tip:This is only Suggestion,Invest on your own Risk."
    else:
        output += f"RELIANCE is currently in a sideways trend. When analyzing sideways trends, traders should look at other technical indicators and chart patterns to provide an indicator of where the price may be headed and when a breakout or breakdown may be likely to occur.\n"
        output += "Tip:This is only Suggestion,Invest on your own Risk."
    return output

@app.route('/relplot_png.png')
def relplot_png():
    
    # Create plot
    fig, axs = plt.subplots(3, sharex=True, figsize=(15, 15))
    axs[0].plot(stock_data_rel['Close'])
    axs[0].plot(stock_data_rel['MA50'])
    axs[0].plot(stock_data_rel['MA200'])
    axs[0].set_title('Stock Price')
    axs[1].plot(RSI_rel)
    axs[1].set_title('Relative Strength Index (RSI)')
    axs[2].plot(MACD_rel)
    axs[2].plot(signal_rel)
    axs[2].set_title('Moving Average Convergence Divergence (MACD)')

    # Save plot to PNG image
    output_rel = io.BytesIO()
    FigureCanvas(fig).print_png(output_rel)
    return Response(output_rel.getvalue(), mimetype='image/png')


@app.route('/tatamotors')
def tatamotors():
    
    
    output = ""
    if stock_data_tata['Close'][-1] > stock_data_tata['MA50'][-1] and stock_data_tata['MA50'][-1] > stock_data_tata['MA200'][-1]:
        output += f"Tatamotors is currently in an uptrend or in bullish Market, In a bull market, the ideal thing for an investor to do is to take advantage of rising prices by buying stocks early in the trend (if possible) and then selling them when they have reached their peak. \n"
        output += "Tip:This is only Suggestion,Invest on your own Risk."

    elif stock_data_tata['Close'][-1] < stock_data_tata['MA50'][-1] and stock_data_tata['MA50'][-1] < stock_data_tata['MA200'][-1]:
        output += f"Tatamotors is currently in a downtrend or in Bearish Market.Invest for the long term Smart investors understand that the stock market is cyclical and that bear markets are a natural part of the cycle. Therefore, they focus on the long-term outlook for their investments rather than short-term fluctuations in stock prices.\n"
        output += "Tip:This is only Suggestion,Invest on your own Risk."
    else:
        output += f"Tatamotors is currently in a sideways trend.When analyzing sideways trends, traders should look at other technical indicators and chart patterns to provide an indicator of where the price may be headed and when a breakout or breakdown may be likely to occur.\n"
        output += "Tip:This is only Suggestion,Invest on your own Risk."
    return output

@app.route('/tataplot_png.png')
def tataplot_png():
    
    # Create plot
    fig, axs = plt.subplots(3, sharex=True, figsize=(15, 15))
    axs[0].plot(stock_data_tata['Close'])
    axs[0].plot(stock_data_tata['MA50'])
    axs[0].plot(stock_data_tata['MA200'])
    axs[0].set_title('Stock Price')
    axs[1].plot(RSI_tata)
    axs[1].set_title('Relative Strength Index (RSI)')
    axs[2].plot(MACD_tata)
    axs[2].plot(signal_tata)
    axs[2].set_title('Moving Average Convergence Divergence (MACD)')

    # Save plot to PNG image
    output_tata = io.BytesIO()
    FigureCanvas(fig).print_png(output_tata)
    return Response(output_tata.getvalue(), mimetype='image/png')


@app.route('/ICICI')
def ICICI():
    
    
    output = ""
    if stock_data_icici['Close'][-1] > stock_data_icici['MA50'][-1] and stock_data_icici['MA50'][-1] > stock_data_icici['MA200'][-1]:
        output += f"ICICIBANK is currently in an uptrend or in bullish Market, In a bull market, the ideal thing for an investor to do is to take advantage of rising prices by buying stocks early in the trend (if possible) and then selling them when they have reached their peak. \n"
        output += "Tip:This is only Suggestion,Invest on your own Risk."

    elif stock_data_icici['Close'][-1] < stock_data_icici['MA50'][-1] and stock_data_icici['MA50'][-1] < stock_data_icici['MA200'][-1]:
        output += f"ICICIBANK is currently in a downtrend or in Bearish Market. Invest for the long term Smart investors understand that the stock market is cyclical and that bear markets are a natural part of the cycle. Therefore, they focus on the long-term outlook for their investments rather than short-term fluctuations in stock prices.\n"
        output += "Tip:This is only Suggestion,Invest on your own Risk."
    else:
        output += f"ICICIBANK is currently in a sideways trend.When analyzing sideways trends, traders should look at other technical indicators and chart patterns to provide an indicator of where the price may be headed and when a breakout or breakdown may be likely to occur.\n"
        output += "Tip:This is only Suggestion,Invest on your own Risk."
    return output

@app.route('/iciciplot_png.png')
def iciciplot_png():
    

    # Create plot
    fig, axs = plt.subplots(3, sharex=True, figsize=(15, 15))
    axs[0].plot(stock_data_icici['Close'])
    axs[0].plot(stock_data_icici['MA50'])
    axs[0].plot(stock_data_icici['MA200'])
    axs[0].set_title('Stock Price')
    axs[1].plot(RSI_icici)
    axs[1].set_title('Relative Strength Index (RSI)')
    axs[2].plot(MACD_icici)
    axs[2].plot(signal_icici)
    axs[2].set_title('Moving Average Convergence Divergence (MACD)')

    # Save plot to PNG image
    output_icici = io.BytesIO()
    FigureCanvas(fig).print_png(output_icici)
    return Response(output_icici.getvalue(), mimetype='image/png')


@app.route('/hdfcbank')
def hdfcbank():
    
    
    output = ""
    if stock_data_hdfc['Close'][-1] > stock_data_hdfc['MA50'][-1] and stock_data_hdfc['MA50'][-1] > stock_data_hdfc['MA200'][-1]:
        output += f"HDFCBANK is currently in an uptrend or in bullish Market, In a bull market, the ideal thing for an investor to do is to take advantage of rising prices by buying stocks early in the trend (if possible) and then selling them when they have reached their peak. \n"
        output += "Tip:This is only Suggestion,Invest on your own Risk."

    elif stock_data_hdfc['Close'][-1] < stock_data_hdfc['MA50'][-1] and stock_data_hdfc['MA50'][-1] < stock_data_hdfc['MA200'][-1]:
        output += f"HDFCBANK is currently in a downtrend or in Bearish Market Invest for the long term Smart investors understand that the stock market is cyclical and that bear markets are a natural part of the cycle. Therefore, they focus on the long-term outlook for their investments rather than short-term fluctuations in stock prices.\n"
        output += "Tip:This is only Suggestion,Invest on your own Risk."
    else:
        output += f"HDFCBANK is currently in a sideways trend.When analyzing sideways trends, traders should look at other technical indicators and chart patterns to provide an indicator of where the price may be headed and when a breakout or breakdown may be likely to occur.\n"
        output += "Tip:This is only Suggestion,Invest on your own Risk."
    return output

@app.route('/hdfcplot_png.png')
def hdfcplot_png():
   

    # Create plot
    fig, axs = plt.subplots(3, sharex=True, figsize=(15, 15))
    axs[0].plot(stock_data_hdfc['Close'])
    axs[0].plot(stock_data_hdfc['MA50'])
    axs[0].plot(stock_data_hdfc['MA200'])
    axs[0].set_title('Stock Price')
    axs[1].plot(RSI_hdfc)
    axs[1].set_title('Relative Strength Index (RSI)')
    axs[2].plot(MACD_hdfc)
    axs[2].plot(signal_hdfc)
    axs[2].set_title('Moving Average Convergence Divergence (MACD)')

    # Save plot to PNG image
    output_hdfc = io.BytesIO()
    FigureCanvas(fig).print_png(output_hdfc)
    return Response(output_hdfc.getvalue(), mimetype='image/png')



@app.route('/axisbank')
def axisbank():
    
    
    output = ""
    if stock_data_axis['Close'][-1] > stock_data_axis['MA50'][-1] and stock_data_axis['MA50'][-1] > stock_data_axis['MA200'][-1]:
        output += f"AXISBANK is currently in an uptrend or in bullish Market. In a bull market, The ideal thing for an investor to do is to take advantage of rising prices by buying stocks early in the trend (if possible) and then selling them when they have reached their peak. \n"
        output += "Tip:This is only Suggestion,Invest on your own Risk."

    elif stock_data_axis['Close'][-1] < stock_data_axis['MA50'][-1] and stock_data_axis['MA50'][-1] < stock_data_axis['MA200'][-1]:
        output += f"AXISBANK is currently in a downtrend or in Bearish Market Invest for the long term Smart investors understand that the stock market is cyclical and that bear markets are a natural part of the cycle. Therefore, they focus on the long-term outlook for their investments rather than short-term fluctuations in stock prices.\n"
        output += "Tip:This is only Suggestion,Invest on your own Risk."
    else:
        output += f"AXISBANK is currently in a sideways trend.When analyzing sideways trends, traders should look at other technical indicators and chart patterns to provide an indicator of where the price may be headed and when a breakout or breakdown may be likely to occur.\n"
        output += "Tip:This is only Suggestion,Invest on your own Risk."
    return output

@app.route('/axisplot_png.png')
def axisplot_png():


    # Create plot
    fig, axs = plt.subplots(3, sharex=True, figsize=(15, 15))
    axs[0].plot(stock_data_axis['Close'])
    axs[0].plot(stock_data_axis['MA50'])
    axs[0].plot(stock_data_axis['MA200'])
    axs[0].set_title('Stock Price')
    axs[1].plot(RSI_axis)
    axs[1].set_title('Relative Strength Index (RSI)')
    axs[2].plot(MACD_axis)
    axs[2].plot(signal_axis)
    axs[2].set_title('Moving Average Convergence Divergence (MACD)')

    # Save plot to PNG image
    output_axis = io.BytesIO()
    FigureCanvas(fig).print_png(output_axis)
    return Response(output_axis.getvalue(), mimetype='image/png')




if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
