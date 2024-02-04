def compute_average_imdb_score(movie_list):
    total_score = sum(movie["imdb"] for movie in movie_list)
    num_movies = len(movie_list)
    if num_movies == 0:
        return 0  # Return 0 if the list is empty to avoid division by zero
    average_score = total_score / num_movies
    return average_score

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

    average_score = compute_average_imdb_score(movies)
    print(f"Average IMDB score of the movies: {average_score}")
