import multiprocessing
import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done Sleeping...'


# p1 = multiprocessing.Process(target=do_something)
# p2 = multiprocessing.Process(target=do_something)
#
# p1.start()
# p2.start()
#
# p1.join()
# p2.join()

with concurrent.futures.ProcessPoolExecutor() as executor:
    results = [executor.submit(do_something, 1) for _ in range(10)]

    for future in concurrent.futures.as_completed(results):
        print(future.result())


# processes = []
#
# for _ in range(100):
#     p = multiprocessing.Process(target=do_something, args=[1.5])
#     p.start()
#     processes.append(p)
#
# for process in processes:
#     process.join()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')
