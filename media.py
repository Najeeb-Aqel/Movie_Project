import webbrowser


class Movie():
    # constructor for the movie class
    def __init__(self, movie_title, movie_storyline, poster, movie_url):
        # creating the instance variables of the class movie
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = movie_url

# instance method of the movie class, playing the trailer of your movie


def show_trailer(self):
    webbrowser.open(self.url)
