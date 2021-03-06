import webbrowser

# The Movie class holds information about a movie and links to movie-related
# resources such as a trailer.


class Movie():

    # the maximum number of characters allowed in movie title
    MAX_TITLE_LEN = 22

    def __init__(self, title, storyline, poster_link, trailer_link):
        self.full_title = title
        # full title is too long to display well in some applications
        # so make sure "title" is less than MAX
        if len(self.full_title) > Movie.MAX_TITLE_LEN:
            extra = len(self.full_title) - Movie.MAX_TITLE_LEN
            self.title = self.full_title[:-extra - 3] + "..."
        else:
            self.title = self.full_title
        self.storyline = storyline
        self.poster_image_url = poster_link
        self.trailer_youtube_url = trailer_link

    def show_trailer(self):
        webbrowser.open(self.youtube_trailer_url)
