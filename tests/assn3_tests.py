import requests
import pytest

# Base URL of the Books Service
BASE_URL = "http://localhost:5001"

books = [
    {"title": "Adventures of Huckleberry Finn", "ISBN": "9780520343641", "genre": "Fiction"},
    {"title": "The Best of Isaac Asimov", "ISBN": "9780385050784", "genre": "Science Fiction"},
    {"title": "Fear No Evil", "ISBN": "9780394558783", "genre": "Biography"},
    {"title": "No such book", "ISBN": "000000111111", "genre": "Biography"},
    {"title": "The Greatest Joke Book Ever", "authors": "Mel Greene", "ISBN": "9780380798490", "genre": "Jokes"}
]

ids = []

@pytest.mark.parametrize("book", books[:3])
def test_post_books_unique_ids(book):
    response = requests.post(f"{BASE_URL}/books", json=book)
    assert response.status_code == 201
    ids.append(response.json()['ID'])
    assert len(set(ids)) == len(ids), "IDs are not unique"

def test_get_book_by_id():
    assert ids, "No IDs available from book creation"
    response = requests.get(f"{BASE_URL}/books/{ids[0]}")
    assert response.status_code == 200
    assert response.json()['authors'] == "Mark Twain"

def test_get_all_books():
    response = requests.get(f"{BASE_URL}/books")
    assert response.status_code == 200
    assert len(response.json()) == 3

def test_post_invalid_book_isbn():
    response = requests.post(f"{BASE_URL}/books", json=books[3])
    assert response.status_code == 500

def test_delete_book():
    assert ids, "No IDs available from book creation"
    response = requests.delete(f"{BASE_URL}/books/{ids[1]}")
    assert response.status_code == 200

def test_get_deleted_book():
    assert ids, "No IDs available from book creation"
    response = requests.get(f"{BASE_URL}/books/{ids[1]}")
    assert response.status_code == 404

def test_post_unacceptable_genre():
    response = requests.post(f"{BASE_URL}/books", json=books[4])
    assert response.status_code == 422
