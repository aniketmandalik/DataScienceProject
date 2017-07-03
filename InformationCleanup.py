import os
from LinAlgStatsProb import get_range

def folder_analysis(folder_name):
	for filename in os.listdir(folder_name):
		if filename.endswith(".txt"):
			ignore_invalid_stock(os.path.join(folder_name, filename))

def ignore_invalid_stock(file_name):
	with open(file_name) as f:
		company_data = eval(f.read())
	dep_var = company_data[1]["Month End Stock Price"]
	i = 0
	while i < len(dep_var) and dep_var[i] == 0:
		i += 1
	i -= 1
	if i == -1:
		i = 0
	for j in company_data[1]:
		var = company_data[1][j]
		company_data[1][j] = var[i:]
	company_data[1]["Month End Stock Price"] = dep_var[i + 1:]
	to_del = []
	for j in company_data[1]:
		if get_range(company_data[1][j]) < .01:
			to_del += [j]
	for j in to_del:
		del company_data[1][j]
	f = open(file_name[:-4] + '.txt', 'w')
	f.write(repr(company_data))

folder_analysis("CompanyData")