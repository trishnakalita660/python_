import time
import multiprocessing
import concurrent.futures

start = time.perf_counter()

def do_something():
    print('Sleeping for 1 second..')
    time.sleep(1)
    return 'Done Sleeping..'


def do_something_Param(seconds):
    print('Sleeping for {} second..'.format(seconds))
    time.sleep(1)
    return f'Done Sleeping {seconds} seconds..'



# OLD way of multiprocessing

# run a function multiple times
if __name__ == "__main__":

    processes = []
    processes2 = []
    for _ in range(10):
        p = multiprocessing.Process(target=do_something)
        p.start()
        processes.append(p)

    for process in processes:
        process.join()     

# unlike threads for passing arguements to multiprocessing process the arguements
#  must be able to be serialized using pickle, i.e we are converting python objects
#  into a format that can be deconstructed and reconstructed in another py script.

    for _ in range(10):
        p2 = multiprocessing.Process(target=do_something_Param, args=[2])
        p2.start()
        processes2.append(p2)
    
    for process2 in processes2:
        process2.join()     
    

#------------------------------------ 
#  EFFICIENT

# Process pull executor


    process_multiple = [1, 2, 3, 4, 5]
     

    with concurrent.futures.ProcessPoolExecutor() as executor:
        # run function once at a time
        # p3 = executor.submit(do_something_Param,1) # return future obj
        # print(p3.result()) 

        #  run multiple times
        
        results = executor.map(do_something_Param, process_multiple)
        for result in results:
            print(result)
        # results = [executor.submit(do_something_Param,proces) for proces in process_multiple]
        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())




finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} seconds')



