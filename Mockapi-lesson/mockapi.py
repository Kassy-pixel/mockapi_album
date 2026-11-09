"""
Mock API Exercise: Music Album

1. Create an "Album" resource on mockapi.io ("id", "name", "rate").
2. Paste its URL into API_ENDPOINT below.
3. Study the finished GET section.
4. Fill in the POST, PUT, DELETE TODOs. Keep the TODO comments.
"""

import requests

# TODO (SETUP): Replace this placeholder with your own mockapi.io
# resource URL, e.g. "https://<your-project-id>.mockapi.io/album/<AlbumName>"
API_ENDPOINT = "http://localhost:3777/api/album"

# ============================================================
# 1. GET METHOD (worked example, given to you)
# ============================================================

try:
    getAllSongs = requests.get(API_ENDPOINT)
    getAllSongs.raise_for_status()
    print("Status Code: ", getAllSongs.status_code)
    responseOfAllSongs = getAllSongs.json()
    print("Album Songs: ", responseOfAllSongs)

    print("\n")
    print("***************Print 1 song*****************************")

    getOneSong = requests.get(API_ENDPOINT + "/1")
    print("Status Code", getOneSong.status_code)
    responseOneSong = getOneSong.json()["name"]
    getRating = getOneSong.json()["rate"]
    print("Get one song: ", responseOneSong)
    print("\n")
    print("Get rating: ", getRating)

except requests.exceptions.HTTPError as httperror:
    print("HTTP GET ERROR: ", httperror)


# ============================================================
# 2. POST METHOD
# ============================================================

print("\n")
print("--- CREATING A NEW SONG ---")

# TODO (POST):
#   1. Build dict newSong: "id", "name", "rating" (strings), e.g. "4", "<title>", "8".
#   2. try/except requests.exceptions.HTTPError:
#   3. POST API_ENDPOINT, json=newSong -> responseOfNewSong.
#   4. print responseOfNewSong.status_code (expect 201).
#   5. responseOfNewSong.raise_for_status()
#   6. print responseOfNewSong.json()

# Write your POST code here:
newSong = {"id": "4", "name": "Blinding Lights", "rate": "8"}

try:
    responseOfNewSong = requests.post(API_ENDPOINT, json=newSong)
    print("Status Code: ", responseOfNewSong.status_code)
    responseOfNewSong.raise_for_status()
    print(responseOfNewSong.json())
except requests.exceptions.HTTPError as httperror:
    print("HTTP POST ERROR: ", httperror)


# ============================================================
# 3. PUT METHOD
# ============================================================

print("\n")
print("--- REPLACING A SONG ---")

# TODO (PUT):
#   1. Build dict updatedSong: "id", "name", "rate" (strings), e.g. "2", "<title>", "7".
#   2. try/except requests.exceptions.HTTPError:
#   3. PUT API_ENDPOINT + "/2" (the id), json=updatedSong -> responseOfReplacement.
#   4. print responseOfReplacement.status_code.
#   5. responseOfReplacement.raise_for_status()
#   6. print responseOfReplacement.json()

# Write your PUT code here:
updatedSong = {"id": "2", "name": "Shape of You (Remix)", "rate": "7"}

try:
    responseOfReplacement = requests.put(API_ENDPOINT + "/2", json=updatedSong)
    print("Status Code: ", responseOfReplacement.status_code)
    responseOfReplacement.raise_for_status()
    print(responseOfReplacement.json())
except requests.exceptions.HTTPError as httperror:
    print("HTTP PUT ERROR: ", httperror)


# ============================================================
# 4. DELETE METHOD
# ============================================================

print("\n")
print("--- DELETING A SONG ---")

# TODO (DELETE):
#   1. try/except requests.exceptions.HTTPError:
#   2. DELETE API_ENDPOINT + "/3" (a chosen id) -> deleteSong.
#   3. print deleteSong.status_code.
#   4. deleteSong.raise_for_status()
#   5. print deleteSong.json()
#   6. Bonus: GET that same id, confirm it now errors.

# Write your DELETE code here:
try:
    deleteSong = requests.delete(API_ENDPOINT + "/3")
    print("Status Code: ", deleteSong.status_code)
    deleteSong.raise_for_status()
    print(deleteSong.json())
except requests.exceptions.HTTPError as httperror:
    print("HTTP DELETE ERROR: ", httperror)

# Bonus: confirm the deleted song is gone (expect a 404 error)
try:
    checkDeletedSong = requests.get(API_ENDPOINT + "/3")
    checkDeletedSong.raise_for_status()
    print("Still there: ", checkDeletedSong.json())
except requests.exceptions.HTTPError as httperror:
    print("Confirmed deleted (404 expected): ", httperror)