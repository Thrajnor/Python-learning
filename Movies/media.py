import webbrowser
class Video():
    VALID_RATINGS=["G","PG","PG-13","R"]
    def __init__(self, movie_title,duration):
        self.title = movie_title
        self.duration = duration

    def show_trailer(self):
            webbrowser.open(self.trailer_youtube_url)
    def show_image(self):
            webbrowser.open(self.poster_image_url)



class Movie(Video):
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube,):
        Video.__init__(self, movie_title)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube



class Tvseries(Video):
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube,duration):
        Video.__init__(self, movie_title,duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
