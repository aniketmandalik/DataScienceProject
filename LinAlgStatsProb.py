from math import sqrt, exp, pi, erf

def vector_add(v, w):
	return [i + j for i, j in zip(v, w)]

def vector_subtract(v, w):
	return [i - j for i, j in zip(v, w)]

def vector_sum(vectors):
	return reduce(vector_add, vectors)

def scalar_multiple(c, v):
	return [c * i for i in v]

def vector_mean(vectors):
	return scalar_multiply(1/(len(vectors)), vector_sum(vectors))

def dot(v, w):
	return sum([i * j for i, j in zip(v, w)])

def sum_squares(lst):
	return dot(lst, lst)

def magnitude(v):
	return sqrt(sum_squares(v))

def distance(v, w):
	return magnitude(vector_subtract(v, w))

def shape(A):
	return len(A), len(A[0])

def get_row(A, i):
	return A[i]

def get_col(A, j):
	return [A_row[j] for A_row in A]

def make_matrix(rows, cols, fn):
	return [[fn(i, j) for j in range(cols)] for i in range(rows)]

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = int(len(lst)/2)
    return quick_sort([x for x in lst if x < lst[pivot]]) + [x for x in lst if x == lst[pivot]] + quick_sort([x for x in arr if x > lst[pivot]])

def mean(lst):
	return sum(lst)/len(lst)

def median(lst):
	if lst == []:
		return
	a = quick_sort(lst)
	if len(a)%2 == 0:
		return (a[len(a)/2] + a[len(a)/2 - 1])/2
	return (a[int(len(a)/2)])

def quantile(lst, p):
	i = int(p*en(lst))
	return quick_sort(lst)[i]

def mode(lst):
	a = Counter(lst)
	num = max(a.values)
	return [i for i, count in a.iteritems() if count == num]

def get_range(lst):
	return max(lst) - min(lst)

def de_mean(lst):
	num = mean(lst)
	return [i - num for i in lst]

def variance(lst):
	a = de_mean(lst)
	return sum_squares(a) / (len(a) - 1)

def std_dev(lst):
	return math.sqrt(variance(lst))

def inter_quartile_range(lst):
	return quantile(lst, .75) - quantile(lst, .25)

def covariance(lst1, lst2):
	return dot(de_mean(lst1), de_mean(lst2))/(len(lst1) - 1)

def correlation(lst1, lst2):
	i, j = std_dev(lst1), std_dev(lst2)
	if i > 0 and j > 0:
		return covariance(lst1, lst2) / i / j
	return 0

def uniformpdf(x):
	return 1 if 0 <= x < 1 else 0

def uniformcdf(x):
	if x <= 0:
		return 0
	if x < 1:
		return x
	return 1

def normalpdf(x, mu=0, sigma=1):
	return exp(-((x - mu) ** 2)/(2 * (sigma ** 2))) / (sqrt(2 * pi) * sigma)

def normalcdf(x, mu=0, sigma=1):
	return (1 + erf((x - mu) / sqrt(2) / sigma))/2

def inversenormalcdf(p, mu=0, sigma=1, tol=.00001):
	if mu != 0 or sigma != 1:
		return mu + sigma * inversenormalcdf(p, tol=tol)
	lo_z, lo_p = -10, 0
	hi_z, hi_p = 10, 1
	while hi_z - lo_z > tol:
		mid_z = (lo_z + hi_z) / 2
		mid_p = normalcdf(mid_z)
		if mid_p > p:
			hi_z = mid_z
			hi_p = mid_p
		if mid_p < p:
			lo_z = mid_z
			lo_p = mid_p
		return mid_p
	return (hi_z + lo_z) / 2

def bernoulli_trial(p):
	return 1 if random.random() < p else 0

def binomial(n, p):
	return sum(bernoulli_trial(p) for i in n)