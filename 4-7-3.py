import FinanceDataReader as fdr
import datetime
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


#조회 시작날짜
start = datetime.datetime(2019,10,1)
end = datetime.datetime(2019,10,10)

#한국거래소 상장종목 전체
#df_krx = fdr.StockListing('KRX')

#리스트 10개 출력
#print(df_krx.head(10))

#출력
#print(df_krx.index)
#print(df_krx['Symbol'])
#print(df_krx.ix[0])
#print(df_krx.describe)

#미국주식 아마존 금융 정보 호출
df_amz = fdr.DataReader('AMZN', start, end)
#print(df_amz.head(10))
print(df_amz.describe())
