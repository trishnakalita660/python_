import os
# # importing threading module
import threading
import time

import concurrent.futures
import requests

def do_something():
    print('Sleeping 1 second')
    time.sleep(1)
    print('Done Sleeping')

#  running fn once (manual way)

# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)

# t1.start()
# t2.start()

# making sure that the thread is finished running 
# t1.join()
# t2.join()

#  running fn multiple times (manual way)

#  running the function do_something in less than 10 seconds even though it is inside a loop
#  it would have taken 15 seconds if runned synchronously

# threads = []
# for _ in range(10):
#     t = threading.Thread(target=do_something)
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()
# print('Script finished in {}'.format(time.perf_counter()))


# Passing arguments inside function #  running fn multiple times with args (manual way)


#  specifying sleeping time
#  will run for 2 seconds , since its running asynchronously

def do_something2(seconds):
    print(f'Sleeping for {seconds} seconds.')
    time.sleep(seconds)
    return f'Done Sleeping {seconds}'

# threads2 = []

# for _ in range(10):
#     t= threading.Thread(target=do_something2, args=[2])
#     t.start()
#     threads2.append(t)

# for thread2 in threads2:
#     thread2.join()

# print('Script finished in {}'.format(time.perf_counter()))


# 
# 
#  EFFICIENT WAY OF IMPLEMENTING THREAD
# 
# 

# Thread pool executor
 
with concurrent.futures.ThreadPoolExecutor() as executor:
    # executing function once at a time
    f1 = executor.submit(do_something2, 1)
    print(f1.result()) # it will wait until fn will complete executing and returns the future object

    # executing function mutiple times
    time_secs = [1, 2, 3, 4, 5]
    results = [executor.submit(do_something2, sec) for sec in time_secs]  #list comprehension (regular for loop)
    for f in concurrent.futures.as_completed(results):
        print(f.result())
    
    #  using map
    results2 = executor.map(do_something2, time_secs) # map returns results in order they were started
    for result2 in results2:
        print(result2)


print('Script finished in {}'.format(time.perf_counter()))


# EXAMPLE

# download images from a given list of URL asynchronously

img_urls = [ 'romeRandomImage/1/1', 'romeRandomImage/2/2', 'romeRandomImage/3/3' ]

def download(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]

    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)


with concurrent.futures.ThreadPoolExecutor() as ex:
    ex.map(download, img_urls)
