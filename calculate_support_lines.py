def calculate_support_lines(dados):
    dados = dados.astype({'Open':'float','High':'float','Low':'float','Close':'float'})
    dados.reset_index(drop=True,inplace=True)
    
    prices = dados['Close']
    # Calculate horizontal support line
    support_level = np.min(prices)
    
    # Calculate trendline support line
    x = np.arange(len(prices))
    trendline = np.polyfit(x, prices, 1)
    
    # Calculate moving average support line
    ma50 = prices.rolling(50).mean().iloc[-1]
    ma200 = prices.rolling(200).mean().iloc[-1]
    
    # Calculate values for sell, buy, and stop loss
    sell = support_level - (trendline[0] * 2)
    buy = support_level + (trendline[0] * 2)
    stop_loss = ma200
    
    return {
        'support_level': support_level,
        'trendline': trendline[0],
        'ma50': ma50,
        'ma200': ma200,
        'sell': sell,
        'buy': buy,
        'stop_loss': stop_loss
    }
