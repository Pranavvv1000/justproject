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
# today = date.today()
# start_date = today - timedelta(days = 90)
# end_date = today - timedelta(days = 1)
start_date = '2023-01-01'
end_date = '2023-05-05'

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


def calculate_technical_indicators(data):
    delta_rel = data['Close'].diff()
    delta_rel = delta_rel[1:]

    up_rel = delta_rel.copy()
    up_rel[up_rel < 0] = 0

    down_rel = delta_rel.copy()
    down_rel[down_rel > 0] = 0

    AVG_Gain_rel = up_rel.rolling(window=14).mean()
    AVG_Loss_rel = abs(down_rel.rolling(window=14).mean())

    RS_rel = AVG_Gain_rel/AVG_Loss_rel
    RSI_rel = 100.0 - (100.0 / (1.0 + RS_rel))

    exp1_rel = data_rel['Close'].ewm(span=12, adjust=False).mean()
    exp2_rel = data_rel['Close'].ewm(span=26, adjust=False).mean()

    MACD_rel = exp1_rel - exp2_rel
    signal_rel = MACD_rel.ewm(span=9, adjust=False).mean()

    return RSI_rel, MACD_rel, signal_rel





# Calculate the Relative Strength Index (RSI) and the Moving Average Convergence Divergence (MACD)


def calculate_technical_indicators1(data):
    delta_tata = data['Close'].diff()
    delta_tata = delta_tata[1:]

    up_tata = delta_tata.copy()
    up_tata[up_tata < 0] = 0

    down_tata = delta_tata.copy()
    down_tata[down_tata > 0] = 0

    AVG_Gain_tata = up_tata.rolling(window=14).mean()
    AVG_Loss_tata = abs(down_tata.rolling(window=14).mean())

    RS_tata = AVG_Gain_tata/AVG_Loss_tata
    RSI_tata = 100.0 - (100.0 / (1.0 + RS_tata))

    exp1_tata = data_tata['Close'].ewm(span=12, adjust=False).mean()
    exp2_tata = data_tata['Close'].ewm(span=26, adjust=False).mean()

    MACD_tata = exp1_tata - exp2_tata
    signal_tata = MACD_tata.ewm(span=9, adjust=False).mean()

    return RSI_tata, MACD_tata, signal_tata


# Calculate the Relative Strength Index (RSI) and the Moving Average Convergence Divergence (MACD)


def calculate_technical_indicators2(data):
    delta_icici = data['Close'].diff()
    delta_icici = delta_icici[1:]

    up_icici = delta_icici.copy()
    up_icici[up_icici < 0] = 0

    down_icici = delta_icici.copy()
    down_icici[down_icici > 0] = 0

    AVG_Gain_icici = up_icici.rolling(window=14).mean()
    AVG_Loss_icici = abs(down_icici.rolling(window=14).mean())

    RS_icici = AVG_Gain_icici/AVG_Loss_icici
    RSI_icici = 100.0 - (100.0 / (1.0 + RS_icici))

    exp1_icici = data_icici['Close'].ewm(span=12, adjust=False).mean()
    exp2_icici = data_icici['Close'].ewm(span=26, adjust=False).mean()

    MACD_icici = exp1_icici - exp2_icici
    signal_icici = MACD_icici.ewm(span=9, adjust=False).mean()

    return RSI_icici, MACD_icici, signal_icici



# Calculate the Relative Strength Index (RSI) and the Moving Average Convergence Divergence (MACD)


def calculate_technical_indicators3(data_hdfc):
    delta_hdfc = data_hdfc['Close'].diff()
    delta_hdfc = delta_hdfc[1:]

    up_hdfc = delta_hdfc.copy()
    up_hdfc[up_hdfc < 0] = 0

    down_hdfc = delta_hdfc.copy()
    down_hdfc[down_hdfc > 0] = 0

    AVG_Gain_hdfc = up_hdfc.rolling(window=14).mean()
    AVG_Loss_hdfc = abs(down_hdfc.rolling(window=14).mean())

    RS_hdfc = AVG_Gain_hdfc/AVG_Loss_hdfc
    RSI_hdfc = 100.0 - (100.0 / (1.0 + RS_hdfc))

    exp1_hdfc = data_hdfc['Close'].ewm(span=12, adjust=False).mean()
    exp2_hdfc = data_hdfc['Close'].ewm(span=26, adjust=False).mean()

    MACD_hdfc = exp1_hdfc - exp2_hdfc
    signal_hdfc = MACD_hdfc.ewm(span=9, adjust=False).mean()

    return RSI_hdfc, MACD_hdfc, signal_hdfc



# Calculate the Relative Strength Index (RSI) and the Moving Average Convergence Divergence (MACD)


def calculate_technical_indicators4(data_axis):
    delta_axis = data_axis['Close'].diff()
    delta_axis = delta_axis[1:]

    up_axis = delta_axis.copy()
    up_axis[up_axis < 0] = 0

    down_axis = delta_axis.copy()
    down_axis[down_axis > 0] = 0

    AVG_Gain_axis = up_axis.rolling(window=14).mean()
    AVG_Loss_axis = abs(down_axis.rolling(window=14).mean())

    RS_axis = AVG_Gain_axis/AVG_Loss_axis
    RSI_axis = 100.0 - (100.0 / (1.0 + RS_axis))

    exp1_axis = data_axis['Close'].ewm(span=12, adjust=False).mean()
    exp2_axis = data_axis['Close'].ewm(span=26, adjust=False).mean()

    MACD_axis = exp1_axis - exp2_axis
    signal_axis = MACD_axis.ewm(span=9, adjust=False).mean()

    return RSI_axis, MACD_axis, signal_axis


RSI_rel, MACD_rel, signal_rel = calculate_technical_indicators(stock_data_rel)
RSI_tata, MACD_tata, signal_tata = calculate_technical_indicators1(stock_data_tata)
RSI_icici, MACD_icici, signal_icici = calculate_technical_indicators2(stock_data_icici)
RSI_hdfc, MACD_hdfc, signal_hdfc = calculate_technical_indicators3(stock_data_hdfc)
RSI_axis, MACD_axis, signal_axis = calculate_technical_indicators4(stock_data_axis)


@app.route('/reliance')
def reliance():
    
    output_rel = ""
    if stock_data_rel['Close'][-1] > stock_data_rel['MA50'][-1] and stock_data_rel['MA50'][-1] > stock_data_rel['MA200'][-1]:
        output_rel += f"RELIANCE is currently in an uptrend or in bullish Market.In a bull market, the ideal thing for an investor to do is to take advantage of rising prices by buying stocks early in the trend (if possible) and then selling them when they have reached their peak."
        output_rel += "Tip:This is only Suggestion,Invest on your own Risk."

    elif stock_data_rel['Close'][-1] < stock_data_rel['MA50'][-1] and stock_data_rel['MA50'][-1] < stock_data_rel['MA200'][-1]:
        output_rel += f"RELIANCE is currently in a downtrend or in Bearish Market.Invest for the long term Smart investors understand that the stock market is cyclical and that bear markets are a natural part of the cycle. Therefore, they focus on the long-term outlook for their investments rather than short-term fluctuations in stock prices.\n"
        output_rel += "Tip:This is only Suggestion,Invest on your own Risk."
    else:
        output_rel += f"RELIANCE is currently in a sideways trend. When analyzing sideways trends, traders should look at other technical indicators and chart patterns to provide an indicator of where the price may be headed and when a breakout or breakdown may be likely to occur.\n"
        output_rel += "Tip:This is only Suggestion,Invest on your own Risk."
    return output_rel

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
    
    
    output_tata = ""
    if stock_data_tata['Close'][-1] > stock_data_tata['MA50'][-1] and stock_data_tata['MA50'][-1] > stock_data_tata['MA200'][-1]:
        output_tata += f"Tatamotors is currently in an uptrend or in bullish Market, In a bull market, the ideal thing for an investor to do is to take advantage of rising prices by buying stocks early in the trend (if possible) and then selling them when they have reached their peak. \n"
        output_tata += "Tip:This is only Suggestion,Invest on your own Risk."

    elif stock_data_tata['Close'][-1] < stock_data_tata['MA50'][-1] and stock_data_tata['MA50'][-1] < stock_data_tata['MA200'][-1]:
        output_tata += f"Tatamotors is currently in a downtrend or in Bearish Market.Invest for the long term Smart investors understand that the stock market is cyclical and that bear markets are a natural part of the cycle. Therefore, they focus on the long-term outlook for their investments rather than short-term fluctuations in stock prices.\n"
        output_tata += "Tip:This is only Suggestion,Invest on your own Risk."
    else:
        output_tata += f"Tatamotors is currently in a sideways trend.When analyzing sideways trends, traders should look at other technical indicators and chart patterns to provide an indicator of where the price may be headed and when a breakout or breakdown may be likely to occur.\n"
        output_tata += "Tip:This is only Suggestion,Invest on your own Risk."
    return output_tata

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
    
    
    output_icici = ""
    if stock_data_icici['Close'][-1] > stock_data_icici['MA50'][-1] and stock_data_icici['MA50'][-1] > stock_data_icici['MA200'][-1]:
        output_icici += f"ICICIBANK is currently in an uptrend or in bullish Market, In a bull market, the ideal thing for an investor to do is to take advantage of rising prices by buying stocks early in the trend (if possible) and then selling them when they have reached their peak. \n"
        output_icici += "Tip:This is only Suggestion,Invest on your own Risk."

    elif stock_data_icici['Close'][-1] < stock_data_icici['MA50'][-1] and stock_data_icici['MA50'][-1] < stock_data_icici['MA200'][-1]:
        output_icici += f"ICICIBANK is currently in a downtrend or in Bearish Market. Invest for the long term Smart investors understand that the stock market is cyclical and that bear markets are a natural part of the cycle. Therefore, they focus on the long-term outlook for their investments rather than short-term fluctuations in stock prices.\n"
        output_icici += "Tip:This is only Suggestion,Invest on your own Risk."
    else:
        output_icici += f"ICICIBANK is currently in a sideways trend.When analyzing sideways trends, traders should look at other technical indicators and chart patterns to provide an indicator of where the price may be headed and when a breakout or breakdown may be likely to occur.\n"
        output_icici += "Tip:This is only Suggestion,Invest on your own Risk."
    return output_icici

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
    
    
    output_hdfc = ""
    if stock_data_hdfc['Close'][-1] > stock_data_hdfc['MA50'][-1] and stock_data_hdfc['MA50'][-1] > stock_data_hdfc['MA200'][-1]:
        output_hdfc += f"HDFCBANK is currently in an uptrend or in bullish Market, In a bull market, the ideal thing for an investor to do is to take advantage of rising prices by buying stocks early in the trend (if possible) and then selling them when they have reached their peak. \n"
        output_hdfc += "Tip:This is only Suggestion,Invest on your own Risk."

    elif stock_data_hdfc['Close'][-1] < stock_data_hdfc['MA50'][-1] and stock_data_hdfc['MA50'][-1] < stock_data_hdfc['MA200'][-1]:
        output_hdfc += f"HDFCBANK is currently in a downtrend or in Bearish Market Invest for the long term Smart investors understand that the stock market is cyclical and that bear markets are a natural part of the cycle. Therefore, they focus on the long-term outlook for their investments rather than short-term fluctuations in stock prices.\n"
        output_hdfc += "Tip:This is only Suggestion,Invest on your own Risk."
    else:
        output_hdfc += f"HDFCBANK is currently in a sideways trend.When analyzing sideways trends, traders should look at other technical indicators and chart patterns to provide an indicator of where the price may be headed and when a breakout or breakdown may be likely to occur.\n"
        output_hdfc += "Tip:This is only Suggestion,Invest on your own Risk."
    return output_hdfc

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
    
    
    output_axis = ""
    if stock_data_axis['Close'][-1] > stock_data_axis['MA50'][-1] and stock_data_axis['MA50'][-1] > stock_data_axis['MA200'][-1]:
        output_axis += f"AXISBANK is currently in an uptrend or in bullish Market. In a bull market, The ideal thing for an investor to do is to take advantage of rising prices by buying stocks early in the trend (if possible) and then selling them when they have reached their peak. \n"
        output_axis += "Tip:This is only Suggestion,Invest on your own Risk."

    elif stock_data_axis['Close'][-1] < stock_data_axis['MA50'][-1] and stock_data_axis['MA50'][-1] < stock_data_axis['MA200'][-1]:
        output_axis += f"AXISBANK is currently in a downtrend or in Bearish Market Invest for the long term Smart investors understand that the stock market is cyclical and that bear markets are a natural part of the cycle. Therefore, they focus on the long-term outlook for their investments rather than short-term fluctuations in stock prices.\n"
        output_axis += "Tip:This is only Suggestion,Invest on your own Risk."
    else:
        output_axis += f"AXISBANK is currently in a sideways trend.When analyzing sideways trends, traders should look at other technical indicators and chart patterns to provide an indicator of where the price may be headed and when a breakout or breakdown may be likely to occur.\n"
        output_axis += "Tip:This is only Suggestion,Invest on your own Risk."
    return output_axis

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
