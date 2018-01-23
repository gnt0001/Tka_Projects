import fresh_tomatoes
import media

# Making instances of the Movie class with the
# the Movie.py constructor. Calls then __init__()

# instance of the movie Baby Driver
baby_driver = media.Movie("Baby Driver",
                          "https://www.youtube.com/watch?v=z2z857RSfhk",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMDA0N2U0OTUtN2U3My00NDg4LTgwNTctZmMyOWExMDdjMjE0XkEyXkFqcGdeQXVyMDc2NTEzMw@@._V1_SY1000_SX675_AL_.jpg")  # NOQA

# instance of The Originals Film
the_orginals = media.Movie("The Originals",
                           "https://www.youtube.com/watch?v=GXrDYboUnnw",
                           "https://i.pinimg.com/736x/c8/2a/0d/c82a0d28234f9880533e747ea05d5140--originals.jpg")  # NOQA

# instance of Wonderwomen movie
wonder_women = media.Movie("Wonderwoman",
                           "https://www.youtube.com/watch?v=VSB4wGIdDwo",
                           "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg")  # NOQA

# a list of all the instance of the Movie class
movies = [baby_driver, the_orginals, wonder_women]


# function call in to display the movie page
fresh_tomatoes.open_movies_page(movies)

