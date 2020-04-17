import requests
from bs4 import BeautifulSoup
import time
import csv
import send_email

csv_file = open("scrape.csv", "w")
csv_writer = csv.writer(csv_file)

csv_writer.writerow(["STOCK NAME", "CURRENT PRICE", "Previous Close", "Open", "Bid", "Ask", "Days Range", "52 Week Range", "Volume", "Average Volume"])

URL1 = "https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch"
URL2 = "https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch"
URL3 = "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"
URL4 = "https://finance.yahoo.com/quote/TTM?p=TTM&.tsrc=fin-srch"
URL_LIST = [URL4, URL3, URL2, URL1]

HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}


################################################################
def collect_from_url(URL):
	stock = []
	html_page_data = requests.get(URL, headers = HEADER)

	#print(html_page_data.content)

	soup = BeautifulSoup(html_page_data.content, 'lxml')

	#TITLE = soup.find('title').get_text()

	stock_title = soup.find_all("div", id = "quote-header-info")[0].find("h1").get_text()
	current_price = soup.find_all("div", id = "quote-header-info")[0].find('div', class_="My(6px) Pos(r) smartphone_Mt(6px)").find("span").get_text()

	table_info = soup.find_all("div", class_= "D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)")[0].find_all('tr')
	print('-'*50)
	print("COMPANY:", stock_title)
	print("PRICE:",current_price)
	print('-'*50)

	stock.append(stock_title)
	stock.append(current_price)

	for i in range(8):
		previous_close_h =table_info[i].find_all("td")[0].get_text()
		previous_close_c =table_info[i].find_all("td")[1].get_text()
		print(previous_close_h,".............",previous_close_c)
		stock.append(previous_close_c)
	csv_writer.writerow(stock)

	time.sleep(5)
	print("*"*100)
####################################

########################################
for URL in URL_LIST:
	collect_from_url(URL)
####################################
csv_file.close()
#####################################
print("Sending Mail..............")
send_email.sendmail()
print("Done.")
