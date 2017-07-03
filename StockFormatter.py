import csv, os

def folder_analysis(folder_name):
	for filename in os.listdir(folder_name):
		if filename.endswith(".csv"):
			analysis(os.path.join(folder_name, filename))

def analysis(file_name):
	data_points = list(csv.reader(open(file_name)))
	data_points = data_points[4:]
	company_data = [{}]
	company_data[0]["Ticker"] = data_points[0][0][4:]
	company_data[0]["Name"], company_data[0]["Country"], company_data[0]["Sector"], company_data[0]["Business Type"] = data_points[0][1:5]
	company_data[0]["Business Model"] = data_points[0][5][:int(len(data_points[0][5])/2)]
	ignore_column = 0
	while True:
		try:
			if data_points[ignore_column][0] == 'Fiscal Period':
				break
		except IndexError:
			pass
		ignore_column += 1
	ignore_number = 0
	for i in data_points[100]:
		ignore_number += 1
		if i == '':
			break
	data_points = data_points[ignore_column:-3]
	for i in range(len(data_points)):
		data_points[i] = [data_points[i][0]] + data_points[i][ignore_number:]
	first_value = 1
	for i in data_points[100][1:]:
		first_value += 1
		if i != '-':
			break
	for i in range(len(data_points)):
		data_points[i] = [data_points[i][0]] + data_points[i][first_value:]
	a = dict({})
	for j in range(0, len(data_points)):
		b = list(map(lambda s: make_float(s), data_points[j][1:]))
		a[data_points[j][0]] = b
	company_data.append(a)
	f = open(file_name[:-4] + '.txt', 'w')
	f.write(repr(company_data))

def make_float(s):
	if s != '':
		s = s.replace(',', '')
		return float(s)
	return 0.0

folder_analysis("CompanyData")
# analysis(os.path.join("CompanyData", "NAS-GOOG.csv"))