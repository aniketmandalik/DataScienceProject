import webbrowser, time

def open_tabs():
	with open("StockTickers.txt") as f:
		content = f.readlines()
	content = [x.strip() for x in content]
	for i in content:
		webbrowser.open_new_tab("http://www.gurufocus.com/financials/" + i)
		time.sleep(1)
open_tabs()