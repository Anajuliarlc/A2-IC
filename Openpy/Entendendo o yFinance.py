import yfinance as yf

# DataFrame do valor da ação
lmt = yf.Ticker("LMT")
hist = lmt.history(period = "max")
print(type(hist))
print(hist)
#for column in hist:
    #print(hist[f"{column}"])
    #print(type(hist[f"{column}"]))
    #coluna = hist[f"{column}"]
    #print(coluna[0])
    #print(hist)