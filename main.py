import media
import fresh_tomatoes


# create an instance of class movie
Avengers = media.Movie("Avengers: Infinity War",
                       "invasion of aliens",
                       "https://static1.squarespace.com/static/51b3dc8ee4b051b96ceb10de/t/5a837b5ae2c483e436e4d198/1518566242734/new-promo-poster-art-for-avengers-infinity-war-brings-all-the-heroes-together1?format=1500w",  # noqa
                       "https://www.youtube.com/watch?v=6ZfuNTqbHE8"
                       )

# create an instance of class movie
Inferno = media.Movie("Inferno",
                      "professor saving the world",
                      "http://www.impawards.com/2016/posters/inferno.jpg",
                      "https://www.youtube.com/watch?v=RH2BD49sEZI"
                      )

# create an instance of class movie
Lincoln = media.Movie("Lincoln",
                      "story of president lincoln",
                      "https://www.movieposter.com/posters/archive/main/153/MPW-76603",  # noqa
                      "https://www.youtube.com/watch?v=qiSAbAuLhqs"
                      )

movies = [Avengers, Inferno, Lincoln]

# passing an array of movies to display
fresh_tomatoes.open_movies_page(movies)
