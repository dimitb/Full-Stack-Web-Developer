import webbrowser


class Movie():
    """This class creates instances of Movie"""
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        # Assigns the various movie related info to each instance
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
