# =====================================================================
# Functions: Moore_Movie_Collection.py
# =====================================================================

def create_movie(title, year, genres, rating):
    """
    Constructs and returns a single movie record as a dictionary.
    Does not print anything or alter external state.
    """
    movie_dict = {
        "title": title,
        "year": int(year),
        "genres": genres,
        "rating": float(rating) 
    }
    return movie_dict

def display_movies(movies, heading):
    """
    Prints a formatted, tabular view of the movie collection with a custom header.
    Utilizes f-string alignment and joins genre list dynamically.
    """
    print(f"\n{heading}")
    print("-" * 75)

    if not movies:
        print("No movies in this collection.")
        return
    
    # Using f-string format specifiers to keep columns clean and aligned
    for movie in movies:
        joined_genres = " / ".join(movie["genres"])
        print(f"{movie['title']:<20}  ({movie['year']}) | {joined_genres:<30} | {movie['rating']:.2f}")

def find_top_rated(movies, n):
    """
    Returns a new sliced list containing the top 'n' highest-rated movies.
    Preserves the original list ordering using the 'sorted' function.  
    """
    # Sorts descending order by rating key
    sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
    # Returns a subset via list slicing
    return sorted_movies[:n]

def get_average_rating(movies):
    """
    Calculates the average rating across all movies in the list.
    Uses an accumulator loop (no built-in sum()) and rounds in 2 decimals.
    """
    if not movies:
        return 0.0
    total_rating = 0.0
    for movie in movies:
        total_rating += movie["rating"]

    average = total_rating / len(movies)
    return round(average, 2)

def main():
    # 1. Define the five-movie starter list
    movies = [
        {"title": "Inception", "year": 2010, "genres": ["Thriller", "Sci-Fi"], "rating": 8.8},
        {"title": "The Matrix", "year": 1999, "genres": ["Action", "Sci-Fi"], "rating": 8.7},
        {"title": "The Godfather", "year": 1972, "genres": ["Crime", "Drama"], "rating": 9.2},
        {"title": "Pulp Fiction", "year": 1994, "genres": ["Crime", "Drama"], "rating": 8.9},
        {"title": "Spirited Away", "year": 2001, "genres": ["Animation", "Fantasy"], "rating": 9.3}
    ]

    # 2. Display collection as loaded
    display_movies(movies, "Your Movie Collection ---")

    # 3. Ask the user to add two new movies
    print("\nAdd two new movies to your collection:")
    for i in range(1, 3):
        print(f"\nMovie #{i}:")
        title = input("Enter the movie title: ")
        year = int(input("Enter the release year: "))
        
        # Take string input, split by comma, and strip whtitespace from each genre
        raw_genres = input("Enter genres (comma-separated): ")
        genres_list = [genre.strip() for genre in raw_genres.split(",")]
        rating = float(input("Enter the movie rating (0.0 - 10.0): "))

        # Build and append
        new_movie = create_movie(title, year, genres_list, rating)
        movies.append(new_movie)

    # 4. Sort the list in-place by year and display
    movies.sort(key=lambda x: x["year"])
    display_movies(movies, "all Movies Sorted by Year")

    # 5. Extract and display the top 3 rated movies
    top_3 = find_top_rated(movies, 3)
    display_movies(top_3, "Top 3 Rated Movies")

    # 6. Calculate and print collection average rating
    avg_rating = get_average_rating(movies)
    print(f"\nCollection average rating: {avg_rating}")
    print("-" * 75)

if __name__ == "__main__":
    main()