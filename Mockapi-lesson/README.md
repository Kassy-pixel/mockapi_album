Mock API Exercise: Music Album

Practice GET, POST, PUT, and DELETE against a real API using Python's
requests library.

Steps:

1. Go to mockapi.io and create a new project.
2. Add a resource named Album with three string fields: id, name, rate.
3. Pick any album. On the Data tab, add at least 3 songs, for example:

   {
     "id": "1",
     "name": "Good Morning",
     "rate": "9"
   }

4. Copy the resource's API URL.
5. Open mockapi.py and paste your URL into API_ENDPOINT:

   API_ENDPOINT = "PASTE_YOUR_MOCKAPI_URL_HERE"

   Use your own URL, not a shared or example one.

6. Read the GET section, it's done, use it as a reference.
7. Complete the three TODOs below it: POST (create a song), PUT
   (replace a song), DELETE (remove a song). Each TODO lists the exact
   steps and variable names. Keep the TODO comments.
8. Run the script:

   python mockapi.py

9. Check the output: GET (200), POST (201), PUT (200), DELETE (200,
   then a GET on that id errors).
10. Submit your completed mockapi.py and a screenshot of the mockapi.io
    Data tab showing your songs after POST, PUT, and DELETE.
