import requests
import json


def get_random_joke():
    url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"
    headers = {
        "x-rapidapi-key": "18dda6a34dmshb8069e422d2ec2cp1e705bjsnb2f9c95e5570",
        "x-rapidapi-host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com",
        "accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    json_data = response.json()
    joke = json_data["value"]
    print("Random Chuck Norris Joke:")
    print(joke)


def get_joke_categories():
    url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/categories"
    headers = {
        "x-rapidapi-key": "18dda6a34dmshb8069e422d2ec2cp1e705bjsnb2f9c95e5570",
        "x-rapidapi-host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com",
        "accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    categories = response.json()
    print("Joke Categories:")
    for category in categories:
        print(category)


def search_jokes():
    query = input("Enter a search query: ")
    url = f"https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/search?query={query}"
    headers = {
        "x-rapidapi-key": "18dda6a34dmshb8069e422d2ec2cp1e705bjsnb2f9c95e5570",
        "x-rapidapi-host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com",
        "accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    search_results = response.json()
    print("Search Results:")
    for result in search_results["result"]:
        print(result["value"])


def main():
    while True:
        print("\nChuck Norris Jokes Menu:")
        print("1. Get a random joke")
        print("2. Get joke categories")
        print("3. Search for jokes")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            get_random_joke()
        elif choice == "2":
            get_joke_categories()
        elif choice == "3":
            search_jokes()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
