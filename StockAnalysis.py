import os

def stock_eval(file_name):
	with open(file_name) as f:
		company_data = eval(f.read())
	dep_var = company_data[1]["Month End Stock Price"]

stock_eval(os.path.join("CompanyData", "NAS-GOOG.txt"))