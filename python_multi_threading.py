import threading
from datetime import datetime
from time import sleep
import requests
import json

url = "http://localhost:3001/api/auth/login"
payload = json.dumps({
	"email": "admin@ally.com",
	"password": "Admin@12345"
})
headers = {
	'Content-Type': 'application/json',
}
results = []
def login(value):
	response = requests.request("POST", url, headers=headers, data=payload)
	# print(response.text)
	result = {
		"index": value,
		"response": response.text
	}
	results.append(result)


def print_cube(num):
	sleep(2)
	print("Cube: {}" .format(num * num * num))


def print_square(num):
	print("Square: {}" .format(num * num))


if __name__ =="__main__":
	now = datetime.now()

	current_time = now.strftime("%H:%M:%S")
	print("Current Time =", current_time)

	# print_cube(10000)
	# print_square(10000000)

	# t2 = threading.Thread(target=print_cube, args=(10,))
	# t1 = threading.Thread(target=print_square, args=(10,))

	# t2.start()
	# t1.start()

	# t2.join()
	# t1.join()
	threads = []
	for i in range(1000):
		# login(i)
		thread = threading.Thread(target=login, args=(i, ))
		thread.start()
		threads.append(thread)
	for thread in threads:
		thread.join()
	now = datetime.now()

	current_time = now.strftime("%H:%M:%S")
	print("Current Time =", current_time)
	# print(results)
	print("Done!")

