import json

favorite_movie = {
    "title": "Fight Club",
    "director": "David Fincher",
    "year": 1999,
    "genre": "Drama, Thriller",
    "rating": 8.8,
    "main_actor": "Brad Pitt",
    "language": "English"
}

# Save data to JSON file
with open("favorite.json", "w", encoding="utf-8") as file:
    json.dump(favorite_movie, file, indent=4)

print("Data has been saved to favorite.json")
