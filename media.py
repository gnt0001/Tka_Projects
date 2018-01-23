class Movie():
    """A class holds instant variables of a instance of a movie class"""

    def __init__(self, title, youtube, image):
        """Constructor/ makes a instance of movie"""
        self.title = title
        self.trailer_youtube_url = youtube
        self.poster_image_url = image

