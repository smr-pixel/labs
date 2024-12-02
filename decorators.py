import time

#standard recursive fibonacci
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

#create decorator for memoization
def memoization(func):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result
    return wrapper

#apply decorator to fibonacci
@memoization
def recur_fibo_new(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo_new(n-1) + recur_fibo_new(n-2))


#print time to finish
start_time_r = time.time()
result_r = recur_fibo(35)
end_time_r = time.time()
print(f"result: {result_r}; time to finish recursively {end_time_r - start_time_r} seconds")

#print new time to finish
start_time_r = time.time()
result_r = recur_fibo_new(35)
end_time_r = time.time()
print(f"result: {result_r}; time to finish recursively {end_time_r - start_time_r} seconds")