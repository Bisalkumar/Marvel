import argparse
from marvel import Marvel
from keys import PUBLIC_KEY, PRIVATE_KEY

def initialize_marvel_api():
    return Marvel(PUBLIC_KEY=PUBLIC_KEY, PRIVATE_KEY=PRIVATE_KEY)

def fetch_characters_with_name_starting_with(starting_name):
    marvel = initialize_marvel_api()
    characters = marvel.characters.all(nameStartsWith=starting_name)["data"]["results"]
    return characters

def fetch_character_comics(character_id):
    marvel = initialize_marvel_api()
    comics = marvel.characters.get(character_id, "comics")["data"]["results"]
    return comics

def fetch_character_events(character_id):
    marvel = initialize_marvel_api()
    events = marvel.characters.get(character_id, "events")["data"]["results"]
    return events

def fetch_character_series(character_id):
    marvel = initialize_marvel_api()
    series = marvel.characters.get(character_id, "series")["data"]["results"]
    return series

def fetch_character_stories(character_id):
    marvel = initialize_marvel_api()
    stories = marvel.characters.get(character_id, "stories")["data"]["results"]
    return stories

def print_character_info(character):
    print(f"ID: {character['id']}\nName: {character['name']}")
    print(f"Description: {character['description']}")
    print(f"Modified Date: {character['modified']}")
    print(f"Resource URI: {character['resourceURI']}")
    print("URLs:")
    for url in character["urls"]:
        print(f"- Type: {url['type']}, URL: {url['url']}")
    print("Thumbnail Image:")
    print(f"- Path: {character['thumbnail']['path']}, Extension: {character['thumbnail']['extension']}")
    print("---------------------")

def print_comic_info(comic):
    print(f"ID: {comic['id']}\nTitle: {comic['title']}")
    print(f"Issue Number: {comic['issueNumber']}")
    print(f"Description: {comic['description']}")
    print(f"Modified Date: {comic['modified']}")
    print(f"ISBN: {comic['isbn']}")
    print(f"UPC: {comic['upc']}")
    print(f"Resource URI: {comic['resourceURI']}")
    print("URLs:")
    for url in comic["urls"]:
        print(f"- Type: {url['type']}, URL: {url['url']}")
    print("Thumbnail Image:")
    print(f"- Path: {comic['thumbnail']['path']}, Extension: {comic['thumbnail']['extension']}")
    print("---------------------")

def print_event_info(event):
    print(f"ID: {event['id']}\nTitle: {event['title']}")
    print(f"Description: {event['description']}")
    print(f"Modified Date: {event['modified']}")
    print(f"Start Date: {event['start']}")
    print(f"End Date: {event['end']}")
    print(f"Resource URI: {event['resourceURI']}")
    print("URLs:")
    for url in event["urls"]:
        print(f"- Type: {url['type']}, URL: {url['url']}")
    print("Thumbnail Image:")
    print(f"- Path: {event['thumbnail']['path']}, Extension: {event['thumbnail']['extension']}")
    print("---------------------")

def print_series_info(series):
    print(f"ID: {series['id']}\nTitle: {series['title']}")
    print(f"Description: {series['description']}")
    print(f"Start Year: {series['startYear']}")
    print(f"End Year: {series['endYear']}")
    print(f"Rating: {series['rating']}")
    print(f"Modified Date: {series['modified']}")
    print(f"Resource URI: {series['resourceURI']}")
    print("URLs:")
    for url in series["urls"]:
        print(f"- Type: {url['type']}, URL: {url['url']}")
    print("Thumbnail Image:")
    print(f"- Path: {series['thumbnail']['path']}, Extension: {series['thumbnail']['extension']}")
    print("---------------------")

def print_story_info(story):
    print(f"ID: {story['id']}\nTitle: {story['title']}")
    print(f"Description: {story['description']}")
    print(f"Type: {story['type']}")
    print(f"Modified Date: {story['modified']}")
    print("Thumbnail Image:")
    print(f"- Path: {story['thumbnail']['path']}, Extension: {story['thumbnail']['extension']}")
    print("Comics in which this Story takes place:")
    if story["comics"]:
        for comic in story["comics"]["items"]:
            print(f"- Comic Name: {comic['name']}")
    print("Series in which this Story appears:")
    if story["series"]:
        for series in story["series"]["items"]:
            print(f"- Series Name: {series['name']}")
    print("Events in which this Story appears:")
    if story["events"]:
        for event in story["events"]["items"]:
            print(f"- Event Name: {event['name']}")
    print("Characters in this Story:")
    if story["characters"]:
        for character in story["characters"]["items"]:
            print(f"- Name: {character['name']}, Role: {character['role']}")
    print("Creators of this Story:")
    if story["creators"]:
        for creator in story["creators"]["items"]:
            print(f"- Name: {creator['name']}, Role: {creator['role']}")
    print("---------------------")

def main():
    character_name = input("Enter the name of the character: ")
    
    character = fetch_characters_with_name_starting_with(character_name)
    if character:
        character_id = character[0]["id"]
        comics = fetch_character_comics(character_id)
        events = fetch_character_events(character_id)
        series = fetch_character_series(character_id)
        stories = fetch_character_stories(character_id)

        print_character_info(character[0])

        if comics:
            print("Comics for this character:")
            for comic in comics:
                print_comic_info(comic)

        if events:
            print("Events for this character:")
            for event in events:
                print_event_info(event)

        if series:
            print("Series for this character:")
            for s in series:
                print_series_info(s)

        if stories:
            print("Stories for this character:")
            for story in stories:
                print_story_info(story)
    else:
        print(f"No character found with the name: {character_name}")

if __name__ == "__main__":
    main()
