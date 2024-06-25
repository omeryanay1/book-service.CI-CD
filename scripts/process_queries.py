import requests

# Assuming the Books Service is running on localhost and exposed on port 5001
BASE_URL = "http://localhost:5001/books"

def process_queries():
    with open('query.txt', 'r') as file:
        queries = file.readlines()

    with open('response.txt', 'w') as file:
        for i, query in enumerate(queries, start=1):
            query = query.strip()
            response = requests.get(f"{BASE_URL}{query}")
            if response.ok:
                json_response = response.json()
                file.write(f"query: qs-{i}\nresponse: {json_response}\n")
            else:
                file.write(f"query: qs-{i}\nerror: {response.status_code}\n")

if __name__ == "__main__":
    process_queries()
