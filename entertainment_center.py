import fresh_tomatoes
# this imports the media module made in the media.py file
import media

# these classes create movies and their trailers and taglines
superbad = media.Movie("The Hangover",
                       "Some guys just can't handle Vegas",
                       "http://upload.wikimedia.org/wikipedia/en/b/b9/Hangoverposter09.jpg",
                       "https://www.youtube.com/watch?v=tcdUhdOlz9M")
edge_of_tomorrow = media.Movie("Edge of Tomorrow",
                               "Live, Die, Repeat",
                               "http://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg",
                               "https://www.youtube.com/watch?v=vw61gCe2oqI")
twenty_one_jumpstreet = media.Movie("21 Jump Street",
                           "They thought the streets were mean. Then they went back to high school.",
                           "http://upload.wikimedia.org/wikipedia/en/9/93/21JumpStreetfilm.jpg",
                           "https://www.youtube.com/watch?v=ZirgAYBcOgo")
toy_story = media.Movie("Toy Story","A story of a boy and his toys that come to life",
           "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
           "https://www.youtube.com/watch?v=vwyZH85NQC4")
hunger_games = media.Movie("Hunger Games", "A really real reality show",
            "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
            "https://www.youtube.com/watch?v=PbA63a7H0bo")

midnight_in_paris = media.Movie("Midnight in Paris", "Going back in time to meet authors",
            "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
            "https://www.youtube.com/watch?v=atLg2wQQdvU")
# create list of movies
movies = [superbad, edge_of_tomorrow, twenty_one_jumpstreet,
          toy_story, hunger_games, midnight_in_paris]
# create movie website
fresh_tomatoes.open_movies_page(movies)
