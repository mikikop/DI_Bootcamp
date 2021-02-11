import requests
from time import process_time

url1 = 'https://www.google.co.il/'
url2 = 'https://www.ynet.co.il/home/0,7340,L-8,00.html'
url3 = 'https://www.imdb.com/'


t1_start = process_time()
res = requests.get(url1)
t1_stop = process_time()
t1_final = t1_stop-t1_start
print("Elapsed time - url1: ",t1_final)

t2_start = process_time()
res = requests.get(url2)
t2_stop = process_time()
t2_final = t2_stop-t2_start
print("Elapsed time - url2: ",t2_final)

t3_start = process_time()
res = requests.get(url3)
t3_stop = process_time()
t3_final = t3_stop-t3_start
print("Elapsed time - url3: ",t3_final)

