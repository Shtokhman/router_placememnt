from timeit import default_timer
start = default_timer()
a = {}
b = 'test.txt'
a[b[:-4]] = {'t': 'TTT', 'e': 'EEE'}
finish = default_timer()
time = round(finish - start, 8)
