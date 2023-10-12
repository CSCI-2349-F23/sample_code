import json

# Read and load the json file
with open("movies_short.json", "r") as file:
    data = json.load(file)

# Print all the movies and their year of release
for entry in data:

    # Print the title and year
    print(entry["title"] + " " + str(entry["year"]))

print("\nHorror Movies:")

# Print all the horror movies
for movie in data:
    if "Horror" in movie["genres"]:
        print(movie["title"])
