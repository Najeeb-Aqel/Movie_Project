import webbrowser


class Movie():
    """
    The movie class provide the infrastructure to create new movies
    with all the related information,and also interact with the movie
    by showing their trailers
    """
    def __init__(self, movie_title, movie_storyline, poster, movie_url):
        """
        Args:
            movie_title (String): The title of the movie.
            movie_storyline (String): Briefe info of your movies's storyline.
            poster (String): URL of the movie's poster.
            movie_url(String): The URL of the movie's trailer.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = movie_url


def show_trailer(self):
    """
    The show_trailer method shows the movie's trailer on your web broswer.
    Args:
        self (obj:Movie): The same created intsnace of the movie itself.
    """
    webbrowser.open(self.url)

