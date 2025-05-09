from binance import Client
import requests
import pandas as pd
import time
import math
import ta 

client = Client('mSXhgDL9CiFYZ6meCfUhJ4dJo1eqg9tU5NRejLV4yxAyLCKjT9IVD4hnFQKWZZuQ','R6mUZD1Ck4gmbCVIvMbPNvFAOPzFxYtM0biYIYiQf1nHqTuDn16jpvuz2quGcZ3g')

# Funciones
def telegram_bot_sendtext(bot_message):   
    bot_token = '2144404594:AAHuHI3gmo1s1sNRXPm07n3tF02xsYbZ8Wk'
    bot_chatID = '1329401409'
    send_text = 'https://api.telegram.org/bot'+ bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

def applytechnicals(df):
    df['K'] = ta.momentum.stoch(df.High,df.Low,df.Close,window=14,smooth_window=3)
    df['D'] = df['K'].rolling(3).mean()
    df['UpperBand'] = df['Close'].rolling(150).mean() + df['Close'].rolling(150).std() * 1
    df['LowerBand'] = df['Close'].rolling(150).mean() - df['Close'].rolling(150).std() * 1
    df.dropna(inplace=True)
    return df

def getdaydata(symbol):      
    frame = pd.DataFrame(client.get_historical_klines(symbol,'15m','24 hours ago UTC'))
    frame = frame.iloc[:,:6]
    frame.columns = ['Time','Open','High','Low','Close','Volume']
    frame = frame.set_index('Time')
    frame.index = pd.to_datetime(frame.index,unit='ms')
    frame = frame.astype(float) 
    return frame

def getminutedata(symbol):      
    frame = pd.DataFrame(client.get_historical_klines(symbol,'1m','200min ago UTC'))
    frame = frame.iloc[:,:6]
    frame.columns = ['Time','Open','High','Low','Close','Volume']
    frame = frame.set_index('Time')
    frame.index = pd.to_datetime(frame.index,unit='ms')
    frame = frame.astype(float) 
    return frame

def rend(df):
    rendimiento = ((df.iloc[95,3] - df.iloc[0,0])/df.iloc[0,0])*100
    return rendimiento
        
crypto = ['API3USDT','FXSUSDT','ALCXUSDT','GLMRUSDT','BICOUSDT','PLAUSDT','KP3RUSDT','VGXUSDT','CVXUSDT','SCRTUSDT','IMXUSDT','ACHUSDT','LOKAUSDT','MCUSDT','JOEUSDT','ANCUSDT','RNDRUSDT','OOKIUSDT','FLUXUSDT','VOXELUSDT','PYRUSDT','MOVRUSDT','POWRUSDT','QIUSDT','ROSEUSDT','TVKUSDT','ENSUSDT','TLMUSDT','CHESSUSDT','JASMYUSDT','ZECUSDT','DEXEUSDT','CELRUSDT','LINAUSDT','CVCUSDT','RAREUSDT','EGLDUSDT','FISUSDT','MASKUSDT','IOTXUSDT','OCEANUSDT','ZENUSDT','CELOUSDT','FRONTUSDT','GALAUSDT','BURGERUSDT','STPTUSDT','INJUSDT','LTOUSDT','FLOWUSDT','STXUSDT','ICXUSDT','FORUSDT','TOMOUSDT','CFXUSDT','TRUUSDT','SKLUSDT','ERNUSDT','PERLUSDT','UNFIUSDT','FETUSDT','MDXUSDT','AVAUSDT','FLMUSDT','ANTUSDT','ATOMUSDT','REPUSDT','VTHOUSDT','UTKUSDT','DNTUSDT','FIDAUSDT','DASHUSDT','MBLUSDT','PNTUSDT','THETAUSDT','ALICEUSDT','MDTUSDT','NKNUSDT','CLVUSDT','ONEUSDT','WANUSDT','ONTUSDT','CTXCUSDT','AKROUSDT','ARPAUSDT','IOTAUSDT','TFUELUSDT','SXPUSDT','FUNUSDT','GTCUSDT','RADUSDT','ADXUSDT','TRIBEUSDT','PERPUSDT','AIONUSDT','DCRUSDT','ONGUSDT','WINGUSDT','PHAUSDT','NMRUSDT','IOSTUSDT','ILVUSDT','FARMUSDT','CRVUSDT','QTUMUSDT','HOTUSDT','ATAUSDT','DATAUSDT','CTKUSDT','PONDUSDT','SUPERUSDT','IRISUSDT','KAVAUSDT','LINKUSDT','SCUSDT','XMRUSDT','AUCTIONUSDT','LSKUSDT','LPTUSDT','TROYUSDT','AUTOUSDT','DIAUSDT','BNTUSDT','CVPUSDT','RAYUSDT','SLPUSDT','RSRUSDT','DOCKUSDT','YFIIUSDT','YFIUSDT','C98USDT','FORTHUSDT','MTLUSDT','SRMUSDT','BARUSDT','ASRUSDT','BELUSDT','REEFUSDT','SYSUSDT','MINAUSDT','ANKRUSDT','HBARUSDT','AXSUSDT','TWTUSDT','LITUSDT','DGBUSDT','KLAYUSDT','GNOUSDT','MIRUSDT','AAVEUSDT','ALGOUSDT','TRXUSDT','BTGUSDT','XEMUSDT','ALPHAUSDT','NBSUSDT','QUICKUSDT','XLMUSDT','MFTUSDT','ELFUSDT','ETCUSDT','DFUSDT','ARDRUSDT','AUDIOUSDT','HARDUSDT','BCHUSDT','KMDUSDT','FILUSDT','BEAMUSDT','VITEUSDT','XVSUSDT','UNIUSDT','DODOUSDT','RVNUSDT','TRBUSDT','WAVESUSDT','ZILUSDT','WRXUSDT','GTOUSDT','RLCUSDT','FTTUSDT','SUSHIUSDT','STRAXUSDT','RIFUSDT','COSUSDT','EOSUSDT','NULSUSDT','NEOUSDT','REQUSDT','JSTUSDT','CKBUSDT','NEARUSDT','ZRXUSDT','TORNUSDT','XECUSDT','WINUSDT','COMPUSDT','ALPACAUSDT','BTSUSDT','BAKEUSDT','GRTUSDT','HNTUSDT','BLZUSDT','BALUSDT','BATUSDT','SNXUSDT','COTIUSDT','BANDUSDT','ORNUSDT','CHZUSDT','POLYUSDT','OXTUSDT','KNCUSDT','MATICUSDT','STMXUSDT','POLSUSDT','SFPUSDT','FTMUSDT','QNTUSDT','BONDUSDT','IDEXUSDT','TKOUSDT','ICPUSDT','FIOUSDT','GHSTUSDT','MANAUSDT','OMGUSDT','UMAUSDT','VETUSDT','ARUSDT','SUNUSDT','ENJUSDT','OGNUSDT','WNXMUSDT','MKRUSDT','RENUSDT','CAKEUSDT','SANDUSDT','DEGOUSDT','XVGUSDT','DENTUSDT','BADGERUSDT','RUNEUSDT','XTZUSDT','CHRUSDT','HIVEUSDT','DYDXUSDT','WTCUSDT','STORJUSDT','VIDTUSDT','TCTUSDT','CTSIUSDT','BETAUSDT','KEYUSDT','AGLDUSDT','DARUSDT','MBOXUSDT','YGGUSDT','DREPUSDT','MITHUSDT','COCOSUSDT']

def getnames(cryptos):
    crypto_prices = [rend(getdaydata(i)) for i in cryptos]
    names = pd.DataFrame(crypto_prices)
    names.columns = ['rendimientos']
    names['names'] = crypto
    names = names.sort_values(by=['rendimientos'], ascending=False)
    names = list(names.iloc[0:5,1])
    return names

while True:
      first_position = False
      second_position = False
      third_position = False
      four_position = False
      fifth_position = False
      try:
          nombres = getnames(crypto)
      except:
          telegram_bot_sendtext("Error de conexión.")
          continue
      telegram_bot_sendtext("Current cryptos are "+nombres[0]+", "+nombres[1]+", "+nombres[2]+', '+nombres[3]+' and '+nombres[4])
      i = 1
      while i < 1800:
          time.sleep(0.5)            
          #First
          try:
             f_price = applytechnicals(getminutedata(nombres[0]))      
             if ( first_position == False and f_price.Close[-1] <= f_price.LowerBand[-1] and math.floor(f_price.K[-1]) < 18 and math.floor(f_price.D[-1]) < 18  and  math.floor(f_price.K[-1]) < math.floor(f_price.D[-1]) ):
                 leng,integer = math.modf(f_price.Close[-1])
                 telegram_bot_sendtext("Buy "+nombres[0]+". Market price:"+str(f_price.Close[-1])+"\n"+"\n ->%1 price: "+str(round(f_price.LowerBand[-1]*0.99,len(str(leng))-2))+"\nTentative 5%(-1%) sell price: "+str(round(1.05*(f_price.LowerBand[-1]*0.99),len(str(leng))-2))+"\nTentative 8%(-1%) sell price: "+str(round(1.08*(f_price.LowerBand[-1]*0.99),len(str(leng))-2))+"\nTentative 10%(-1%) sell price: "+str(round(1.1*(f_price.LowerBand[-1]*0.99),len(str(leng))-2))+"\nTentative 15%(-1%) sell price: "+str(round(1.15*(f_price.LowerBand[-1]*0.99),len(str(leng))-2))+"\n"+"\n ->%2 price: "+str(round(f_price.LowerBand[-1]*0.98,len(str(leng))-2))+"\nTentative 5%(-2%) sell price: "+str(round(1.05*(f_price.LowerBand[-1]*0.98),len(str(leng))-2))+"\nTentative 8%(-2%) sell price: "+str(round(1.08*(f_price.LowerBand[-1]*0.98),len(str(leng))-2))+"\nTentative 10%(-2%) sell price: "+str(round(1.1*(f_price.LowerBand[-1]*0.98),len(str(leng))-2))+"\nTentative 15%(-2%) sell price: "+str(round(1.15*(f_price.LowerBand[-1]*0.98),len(str(leng))-2))+"\n"+"\n ->%3 price: "+str(round(f_price.LowerBand[-1]*0.97,len(str(leng))-2))+"\nTentative 5%(-3%) sell price: "+str(round(1.05*(f_price.LowerBand[-1]*0.97),len(str(leng))-2))+"\nTentative 8%(-3%) sell price: "+str(round(1.08*(f_price.LowerBand[-1]*0.97),len(str(leng))-2))+"\nTentative 10%(-3%) sell price: "+str(round(1.1*(f_price.LowerBand[-1]*0.97),len(str(leng))-2))+"\nTentative 15%(-3%) sell price: "+str(round(1.15*(f_price.LowerBand[-1]*0.97),len(str(leng))-2))+"\n"+"\n ->%4 price: "+str(round(f_price.LowerBand[-1]*0.96,len(str(leng))-2))+"\nTentative 5%(-4%) sell price: "+str(round(1.05*(f_price.LowerBand[-1]*0.96),len(str(leng))-2))+"\nTentative 8%(-4%) sell price: "+str(round(1.08*(f_price.LowerBand[-1]*0.96),len(str(leng))-2))+"\nTentative 10%(-4%) sell price: "+str(round(1.1*(f_price.LowerBand[-1]*0.96),len(str(leng))-2))+"\nTentative 15%(-4%) sell price: "+str(round(1.15*(f_price.LowerBand[-1]*0.96),len(str(leng))-2))+"\n"+"\n ->%5 price: "+str(round(f_price.LowerBand[-1]*0.95,len(str(leng))-2))+"\nTentative 5%(-5%) sell price: "+str(round(1.05*(f_price.LowerBand[-1]*0.95),len(str(leng))-2))+"\nTentative 8%(-5%) sell price: "+str(round(1.08*(f_price.LowerBand[-1]*0.95),len(str(leng))-2))+"\nTentative 10%(-5%) sell price: "+str(round(1.1*(f_price.LowerBand[-1]*0.95),len(str(leng))-2))+"\nTentative 15%(-5%) sell price: "+str(round(1.15*(f_price.LowerBand[-1]*0.95),len(str(leng))-2)) )              
                 first_position = True   
          except:
              continue
          #Second
          try:
             s_price = applytechnicals(getminutedata(nombres[1]))     
             if ( second_position == False and s_price.Close[-1] <= s_price.LowerBand[-1] and math.floor(s_price.K[-1]) < 18 and math.floor(s_price.D[-1]) < 18  and  math.floor(s_price.K[-1]) < math.floor(s_price.D[-1]) ):
                 leng,integer = math.modf(s_price.Close[-1])
                 telegram_bot_sendtext("Buy "+nombres[1]+". Market price:"+str(s_price.Close[-1])+"\n"+"\n ->%1 price: "+str(round(s_price.LowerBand[-1]*0.99,len(str(leng))-2))+"\nTentative 5%(-1%) sell price: "+str(round(1.05*(s_price.LowerBand[-1]*0.99),len(str(leng))-2))+"\nTentative 8%(-1%) sell price: "+str(round(1.08*(s_price.LowerBand[-1]*0.99),len(str(leng))-2))+"\nTentative 10%(-1%) sell price: "+str(round(1.1*(s_price.LowerBand[-1]*0.99),len(str(leng))-2))+"\nTentative 15%(-1%) sell price: "+str(round(1.15*(s_price.LowerBand[-1]*0.99),len(str(leng))-2))+"\n"+"\n ->%2 price: "+str(round(s_price.LowerBand[-1]*0.98,len(str(leng))-2))+"\nTentative 5%(-2%) sell price: "+str(round(1.05*(s_price.LowerBand[-1]*0.98),len(str(leng))-2))+"\nTentative 8%(-2%) sell price: "+str(round(1.08*(s_price.LowerBand[-1]*0.98),len(str(leng))-2))+"\nTentative 10%(-2%) sell price: "+str(round(1.1*(s_price.LowerBand[-1]*0.98),len(str(leng))-2))+"\nTentative 15%(-2%) sell price: "+str(round(1.15*(s_price.LowerBand[-1]*0.98),len(str(leng))-2))+"\n"+"\n ->%3 price: "+str(round(s_price.LowerBand[-1]*0.97,len(str(leng))-2))+"\nTentative 5%(-3%) sell price: "+str(round(1.05*(s_price.LowerBand[-1]*0.97),len(str(leng))-2))+"\nTentative 8%(-3%) sell price: "+str(round(1.08*(s_price.LowerBand[-1]*0.97),len(str(leng))-2))+"\nTentative 10%(-3%) sell price: "+str(round(1.1*(s_price.LowerBand[-1]*0.97),len(str(leng))-2))+"\nTentative 15%(-3%) sell price: "+str(round(1.15*(s_price.LowerBand[-1]*0.97),len(str(leng))-2))+"\n"+"\n ->%4 price: "+str(round(s_price.LowerBand[-1]*0.96,len(str(leng))-2))+"\nTentative 5%(-4%) sell price: "+str(round(1.05*(s_price.LowerBand[-1]*0.96),len(str(leng))-2))+"\nTentative 8%(-4%) sell price: "+str(round(1.08*(s_price.LowerBand[-1]*0.96),len(str(leng))-2))+"\nTentative 10%(-4%) sell price: "+str(round(1.1*(s_price.LowerBand[-1]*0.96),len(str(leng))-2))+"\nTentative 15%(-4%) sell price: "+str(round(1.15*(s_price.LowerBand[-1]*0.96),len(str(leng))-2))+"\n"+"\n ->%5 price: "+str(round(s_price.LowerBand[-1]*0.95,len(str(leng))-2))+"\nTentative 5%(-5%) sell price: "+str(round(1.05*(s_price.LowerBand[-1]*0.95),len(str(leng))-2))+"\nTentative 8%(-5%) sell price: "+str(round(1.08*(s_price.LowerBand[-1]*0.95),len(str(leng))-2))+"\nTentative 10%(-5%) sell price: "+str(round(1.1*(s_price.LowerBand[-1]*0.95),len(str(leng))-2))+"\nTentative 15%(-5%) sell price: "+str(round(1.15*(s_price.LowerBand[-1]*0.95),len(str(leng))-2)) ) 
                 second_position = True   
          except:
              continue
          #Third
          try:
             t_price = applytechnicals(getminutedata(nombres[2]))      
             if ( third_position == False and t_price.Close[-1] <= t_price.LowerBand[-1] and math.floor(t_price.K[-1]) < 18 and math.floor(t_price.D[-1]) < 18  and  math.floor(t_price.K[-1]) < math.floor(t_price.D[-1]) ):
                 leng,integer = math.modf(t_price.Close[-1])
                 telegram_bot_sendtext("Buy "+nombres[2]+". Market price:"+str(t_price.Close[-1])+"\n"+"\n ->%1 price: "+str(round(t_price.LowerBand[-1]*0.99,len(str(leng))-2))+"\nTentative 5%(-1%) sell price: "+str(round(1.05*(t_price.LowerBand[-1]*0.99),len(str(leng))-2))+"\nTentative 8%(-1%) sell price: "+str(round(1.08*(t_price.LowerBand[-1]*0.99),len(str(leng))-2))+"\nTentative 10%(-1%) sell price: "+str(round(1.1*(t_price.LowerBand[-1]*0.99),len(str(leng))-2))+"\nTentative 15%(-1%) sell price: "+str(round(1.15*(t_price.LowerBand[-1]*0.99),len(str(leng))-2))+"\n"+"\n ->%2 price: "+str(round(t_price.LowerBand[-1]*0.98,len(str(leng))-2))+"\nTentative 5%(-2%) sell price: "+str(round(1.05*(t_price.LowerBand[-1]*0.98),len(str(leng))-2))+"\nTentative 8%(-2%) sell price: "+str(round(1.08*(t_price.LowerBand[-1]*0.98),len(str(leng))-2))+"\nTentative 10%(-2%) sell price: "+str(round(1.1*(t_price.LowerBand[-1]*0.98),len(str(leng))-2))+"\nTentative 15%(-2%) sell price: "+str(round(1.15*(t_price.LowerBand[-1]*0.98),len(str(leng))-2))+"\n"+"\n ->%3 price: "+str(round(t_price.LowerBand[-1]*0.97,len(str(leng))-2))+"\nTentative 5%(-3%) sell price: "+str(round(1.05*(t_price.LowerBand[-1]*0.97),len(str(leng))-2))+"\nTentative 8%(-3%) sell price: "+str(round(1.08*(t_price.LowerBand[-1]*0.97),len(str(leng))-2))+"\nTentative 10%(-3%) sell price: "+str(round(1.1*(t_price.LowerBand[-1]*0.97),len(str(leng))-2))+"\nTentative 15%(-3%) sell price: "+str(round(1.15*(t_price.LowerBand[-1]*0.97),len(str(leng))-2))+"\n"+"\n ->%4 price: "+str(round(t_price.LowerBand[-1]*0.96,len(str(leng))-2))+"\nTentative 5%(-4%) sell price: "+str(round(1.05*(t_price.LowerBand[-1]*0.96),len(str(leng))-2))+"\nTentative 8%(-4%) sell price: "+str(round(1.08*(t_price.LowerBand[-1]*0.96),len(str(leng))-2))+"\nTentative 10%(-4%) sell price: "+str(round(1.1*(t_price.LowerBand[-1]*0.96),len(str(leng))-2))+"\nTentative 15%(-4%) sell price: "+str(round(1.15*(t_price.LowerBand[-1]*0.96),len(str(leng))-2))+"\n"+"\n ->%5 price: "+str(round(t_price.LowerBand[-1]*0.95,len(str(leng))-2))+"\nTentative 5%(-5%) sell price: "+str(round(1.05*(t_price.LowerBand[-1]*0.95),len(str(leng))-2))+"\nTentative 8%(-5%) sell price: "+str(round(1.08*(t_price.LowerBand[-1]*0.95),len(str(leng))-2))+"\nTentative 10%(-5%) sell price: "+str(round(1.1*(t_price.LowerBand[-1]*0.95),len(str(leng))-2))+"\nTentative 15%(-5%) sell price: "+str(round(1.15*(t_price.LowerBand[-1]*0.95),len(str(leng))-2)) )
                 third_position = True
          except:
              continue
          #Fourth
          try:
             fo_price = applytechnicals(getminutedata(nombres[3]))      
             if ( four_position == False and fo_price.Close[-1] <= fo_price.LowerBand[-1] and math.floor(fo_price.K[-1]) < 18 and math.floor(fo_price.D[-1]) < 18  and  math.floor(fo_price.K[-1]) < math.floor(fo_price.D[-1]) ):
                 leng,integer = math.modf(fo_price.Close[-1])
                 telegram_bot_sendtext("Buy "+nombres[3]+". Market price:"+str(fo_price.Close[-1])+"\n"+"\n ->%1 price: "+str(round(fo_price.LowerBand[-1]*0.99,len(str(leng))-2))+"\nTentative 5%(-1%) sell price: "+str(round(1.05*(fo_price.LowerBand[-1]*0.99),len(str(leng))-2))+"\nTentative 8%(-1%) sell price: "+str(round(1.08*(fo_price.LowerBand[-1]*0.99),len(str(leng))-2))+"\nTentative 10%(-1%) sell price: "+str(round(1.1*(fo_price.LowerBand[-1]*0.99),len(str(leng))-2))+"\nTentative 15%(-1%) sell price: "+str(round(1.15*(fo_price.LowerBand[-1]*0.99),len(str(leng))-2))+"\n"+"\n ->%2 price: "+str(round(fo_price.LowerBand[-1]*0.98,len(str(leng))-2))+"\nTentative 5%(-2%) sell price: "+str(round(1.05*(fo_price.LowerBand[-1]*0.98),len(str(leng))-2))+"\nTentative 8%(-2%) sell price: "+str(round(1.08*(fo_price.LowerBand[-1]*0.98),len(str(leng))-2))+"\nTentative 10%(-2%) sell price: "+str(round(1.1*(fo_price.LowerBand[-1]*0.98),len(str(leng))-2))+"\nTentative 15%(-2%) sell price: "+str(round(1.15*(fo_price.LowerBand[-1]*0.98),len(str(leng))-2))+"\n"+"\n ->%3 price: "+str(round(fo_price.LowerBand[-1]*0.97,len(str(leng))-2))+"\nTentative 5%(-3%) sell price: "+str(round(1.05*(fo_price.LowerBand[-1]*0.97),len(str(leng))-2))+"\nTentative 8%(-3%) sell price: "+str(round(1.08*(fo_price.LowerBand[-1]*0.97),len(str(leng))-2))+"\nTentative 10%(-3%) sell price: "+str(round(1.1*(fo_price.LowerBand[-1]*0.97),len(str(leng))-2))+"\nTentative 15%(-3%) sell price: "+str(round(1.15*(fo_price.LowerBand[-1]*0.97),len(str(leng))-2))+"\n"+"\n ->%4 price: "+str(round(fo_price.LowerBand[-1]*0.96,len(str(leng))-2))+"\nTentative 5%(-4%) sell price: "+str(round(1.05*(fo_price.LowerBand[-1]*0.96),len(str(leng))-2))+"\nTentative 8%(-4%) sell price: "+str(round(1.08*(fo_price.LowerBand[-1]*0.96),len(str(leng))-2))+"\nTentative 10%(-4%) sell price: "+str(round(1.1*(fo_price.LowerBand[-1]*0.96),len(str(leng))-2))+"\nTentative 15%(-4%) sell price: "+str(round(1.15*(fo_price.LowerBand[-1]*0.96),len(str(leng))-2))+"\n"+"\n ->%5 price: "+str(round(fo_price.LowerBand[-1]*0.95,len(str(leng))-2))+"\nTentative 5%(-5%) sell price: "+str(round(1.05*(fo_price.LowerBand[-1]*0.95),len(str(leng))-2))+"\nTentative 8%(-5%) sell price: "+str(round(1.08*(fo_price.LowerBand[-1]*0.95),len(str(leng))-2))+"\nTentative 10%(-5%) sell price: "+str(round(1.1*(fo_price.LowerBand[-1]*0.95),len(str(leng))-2))+"\nTentative 15%(-5%) sell price: "+str(round(1.15*(fo_price.LowerBand[-1]*0.95),len(str(leng))-2)) )
                 four_position = True
          except:
              continue
          #Fifth
          try:
             fi_price = applytechnicals(getminutedata(nombres[4]))      
             if ( fifth_position == False and fi_price.Close[-1] <= fi_price.LowerBand[-1] and math.floor(fi_price.K[-1]) < 18 and math.floor(fi_price.D[-1]) < 18  and  math.floor(fi_price.K[-1]) < math.floor(fi_price.D[-1]) ):
                 leng,integer = math.modf(fi_price.Close[-1])
                 telegram_bot_sendtext("Buy "+nombres[4]+". Market price:"+str(fi_price.Close[-1])+"\n"+"\n ->%1 price: "+str(round(fi_price.LowerBand[-1]*0.99,len(str(leng))-2))+"\nTentative 5%(-1%) sell price: "+str(round(1.05*(fi_price.LowerBand[-1]*0.99),len(str(leng))-2))+"\nTentative 8%(-1%) sell price: "+str(round(1.08*(fi_price.LowerBand[-1]*0.99),len(str(leng))-2))+"\nTentative 10%(-1%) sell price: "+str(round(1.1*(fi_price.LowerBand[-1]*0.99),len(str(leng))-2))+"\nTentative 15%(-1%) sell price: "+str(round(1.15*(fi_price.LowerBand[-1]*0.99),len(str(leng))-2))+"\n"+"\n ->%2 price: "+str(round(fi_price.LowerBand[-1]*0.98,len(str(leng))-2))+"\nTentative 5%(-2%) sell price: "+str(round(1.05*(fi_price.LowerBand[-1]*0.98),len(str(leng))-2))+"\nTentative 8%(-2%) sell price: "+str(round(1.08*(fi_price.LowerBand[-1]*0.98),len(str(leng))-2))+"\nTentative 10%(-2%) sell price: "+str(round(1.1*(fi_price.LowerBand[-1]*0.98),len(str(leng))-2))+"\nTentative 15%(-2%) sell price: "+str(round(1.15*(fi_price.LowerBand[-1]*0.98),len(str(leng))-2))+"\n"+"\n ->%3 price: "+str(round(fi_price.LowerBand[-1]*0.97,len(str(leng))-2))+"\nTentative 5%(-3%) sell price: "+str(round(1.05*(fi_price.LowerBand[-1]*0.97),len(str(leng))-2))+"\nTentative 8%(-3%) sell price: "+str(round(1.08*(fi_price.LowerBand[-1]*0.97),len(str(leng))-2))+"\nTentative 10%(-3%) sell price: "+str(round(1.1*(fi_price.LowerBand[-1]*0.97),len(str(leng))-2))+"\nTentative 15%(-3%) sell price: "+str(round(1.15*(fi_price.LowerBand[-1]*0.97),len(str(leng))-2))+"\n"+"\n ->%4 price: "+str(round(fi_price.LowerBand[-1]*0.96,len(str(leng))-2))+"\nTentative 5%(-4%) sell price: "+str(round(1.05*(fi_price.LowerBand[-1]*0.96),len(str(leng))-2))+"\nTentative 8%(-4%) sell price: "+str(round(1.08*(fi_price.LowerBand[-1]*0.96),len(str(leng))-2))+"\nTentative 10%(-4%) sell price: "+str(round(1.1*(fi_price.LowerBand[-1]*0.96),len(str(leng))-2))+"\nTentative 15%(-4%) sell price: "+str(round(1.15*(fi_price.LowerBand[-1]*0.96),len(str(leng))-2))+"\n"+"\n ->%5 price: "+str(round(fi_price.LowerBand[-1]*0.95,len(str(leng))-2))+"\nTentative 5%(-5%) sell price: "+str(round(1.05*(fi_price.LowerBand[-1]*0.95),len(str(leng))-2))+"\nTentative 8%(-5%) sell price: "+str(round(1.08*(fi_price.LowerBand[-1]*0.95),len(str(leng))-2))+"\nTentative 10%(-5%) sell price: "+str(round(1.1*(fi_price.LowerBand[-1]*0.95),len(str(leng))-2))+"\nTentative 15%(-5%) sell price: "+str(round(1.15*(fi_price.LowerBand[-1]*0.95),len(str(leng))-2)) )
                 fifth_position = True
          except:
              continue
          if len(nombres) == 0:
              break
          i += 1
      time.sleep(1)    
     


# =============================================================================
# def getdaydata(symbol):      
#     frame = pd.DataFrame(client.get_historical_klines(symbol,'1d','30 days ago UTC'))
#     frame = frame.iloc[:,:6]
#     frame.columns = ['Time','Open','High','Low','Close','Volume']
#     frame = frame.set_index('Time')
#     frame.index = pd.to_datetime(frame.index,unit='ms')
#     frame = frame.astype(float) 
#     return frame
# 
# 
# def getnames(cryptos):
#     crypto_prices = [rend(getdaydata(i)) for i in cryptos]
#     names = pd.DataFrame(crypto_prices)
#     names.columns = ['rendimientos']
#     names['names'] = crypto
#     names = names.sort_values(by=['rendimientos'], ascending=False)
#     names = list(names.iloc[0:15,1])
#     return names
# 
# def rend(df):
#     rendimiento = ((df.iloc[26,3] - df.iloc[26,0])/df.iloc[26,0])*100
#     return rendimiento
# 
# getnames(crypto)
# 
# =============================================================================




