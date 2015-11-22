# Movie Trailers project main function:
#   - define a list of movies,
#   - open the "Fresh Tomatoes" web site to view list and trailers.

import fresh_tomatoes
import media
import turtle

movies = [
    media.Movie(
        "Toy Story",
        "A story of a boy and his toys that come to life.",
        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
        "https://www.youtube.com/watch?v=KYz2wyBy3kc"),
    media.Movie(
        "Henry Fool",
        "A socially inept garbage man is befriended by a talentless" +
        "novelist, opening a magical world of literature.",
        "https://upload.wikimedia.org/wikipedia/en/c/c3/Henry_fool.jpg",
        "https://www.youtube.com/watch?v=twoF56_e9mU"),
    media.Movie(
        "Eternal Sunshine of the Spotless Mind",
        "What if you could erase the memory of heartbreak, then met" +
        " your former lover?",
        "https://upload.wikimedia.org/wikipedia/en/6/62/" +
        "Eternal_sunshine_of_the_spotless_mind_ver3.jpg",
        "https://www.youtube.com/watch?v=0zFywiAh7N0"),
    media.Movie(
        "Gattaca",
        "Read about CRISPR/CAS9 and watch this movie. Then worry.",
        "https://upload.wikimedia.org/wikipedia/en/b/bb/" +
        "Gataca_Movie_Poster_B.jpg",
        "https://www.youtube.com/watch?v=_EUCiFOL1gg"),
    media.Movie(
        "Billy Elliot",
        "Miner's son Billy knows he's a lousy boxer. What he doesn't" +
        " know is that he could be a dancer.",
        "https://upload.wikimedia.org/wikipedia/en/3/31/" +
        "Billy_Elliot_movie.jpg",
        "https://www.youtube.com/watch?v=phCEwSmHpOE"),
    media.Movie(
        'Edge of Tomorrow',
        'Live Die Repeat',
        "https://upload.wikimedia.org/wikipedia/en/f/f9/" +
        "Edge_of_Tomorrow_Poster.jpg",
        'https://www.youtube.com/watch?v=vw61gCe2oqI'),
    media.Movie(
        "Beverly Hills Cop",
        "A Detroit cop solving a crime in Beverly Hills",
        "https://upload.wikimedia.org/wikipedia/en/a/a2/Beverly_Hills_Cop.jpg",
        "https://www.youtube.com/watch?v=hSPvYlipvRU")
]

fresh_tomatoes.open_movies_page(movies)
