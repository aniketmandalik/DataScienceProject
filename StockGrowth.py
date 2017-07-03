import os
from LinAlgStatsProb import get_range

def folder_analysis(folder_name):
	for filename in os.listdir(folder_name):
		if filename.endswith(".txt"):
			find_change(os.path.join(folder_name, filename))

def find_change(file_name):
	with open(file_name) as f:
		company_data = eval(f.read())
	to_add_dict = {}
	for i in company_data[1]:
		if get_range(company_data[1][i]) > .01:
			to_add_dict[i + ' Change'] = [(j-i)/i if i != 0 else j * 100 for i, j in zip(company_data[1][i][:-1], company_data[1][i][1:])]
	company_data[1].update(to_add_dict)
	f = open(file_name, 'w')
	f.write(repr(company_data))

folder_analysis("CompanyData")