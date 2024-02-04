def compute_average_imdb_score_by_category(movie_list, category):
    # Filter movies by category
    movies_in_category = [movie for movie in movie_list if movie["category"] == category]
    
    # Calculate average IMDB score for movies in the category
    total_score = sum(movie["imdb"] for movie in movies_in_category)
    num_movies = len(movies_in_category)
    if num_movies == 0:
        return 0  # Return 0 if no movies in the category to avoid division by zero
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

    # Compute average IMDB score for movies in the "Action" category
    category = "Action"
    average_score = compute_average_imdb_score_by_category(movies, category)
    print(f"Average IMDB score of movies in the '{category}' category: {average_score}")
