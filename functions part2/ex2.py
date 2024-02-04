def get_high_rated_movies(movie_list):
    high_rated_movies = [movie for movie in movie_list if movie["imdb"] > 5.5]
    return high_rated_movies

# Test the function
if __name__ == "__main__":
    # Example movie list
    movies = [
        {
            "name": "Usual Suspects", 
            "imdb": 7.0,
            "category": "Thriller"
        },
        {
            "name": "Hitman",
            "imdb": 6.3,
            "category": "Action"
        },
        {
            "name": "Dark Knight",
            "imdb": 9.0,
            "category": "Adventure"
        },
        # Add more movies here...
    ]

    high_rated_movies = get_high_rated_movies(movies)
    print("Movies with an IMDB score above 5.5:")
    for movie in high_rated_movies:
        print(f"Name: {movie['name']}, IMDB: {movie['imdb']}")
