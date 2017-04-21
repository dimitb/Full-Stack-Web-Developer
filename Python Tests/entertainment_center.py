"""This module stores information related to each movie such as the title,
trailer, storyline, and poster image"""

import fresh_tomatoes
import media

# Defines info such as title and storyline to each instance of movie
old_school = media.Movie("Old School",
                         "Three men relive their carefree college years by killing off as many\
                          brain cells as possible",
                         "https://upload.wikimedia.org/wikipedia/en/2/21/Old_s_poster.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=FE4XhgHrmAE")  # NOQA

they_live = media.Movie("They Live",
                        "Aliens live among us as everyday people until a drifter finds a special\
                         pair of sunglasses",
                        "https://upload.wikimedia.org/wikipedia/en/3/3d/1988They_Live_poster300.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KLRafyWhzG4")  # NOQA

big_trouble_in_little_china = media.Movie("Big Trouble in Little China",
                                          "Join Jack Burton and friends as they try to stop ancient Chinese forces\
                                          in San Francisco's Chinatown",
                                          "https://upload.wikimedia.org/wikipedia/en/7/76/Big_Trouble_in_Little_China_Film_Poster.jpg",  # NOQA
                                          "https://www.youtube.com/watch?v=592EiTD2Hgo")  # NOQA

spaceballs = media.Movie("Spaceballs",
                         "Lone Starr and his sidekick Barf must save the galaxy from\
                         the evil Dark Helmet",
                         "https://upload.wikimedia.org/wikipedia/en/4/45/Spaceballs.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=kGIM_yNzeUo")  # NOQA

the_score = media.Movie("The Score",
                        "An aging thief hopes to retire and live off his ill-gotten wealth when\
                        a young kid convinces him into doing one last heist",
                        "https://upload.wikimedia.org/wikipedia/en/9/97/The_Score_film.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=AiN6-UdxcbI")  # NOQA

north_by_northwest = media.Movie("North by Northwest",
                                 "Cary Grant is mired in a deadly game of cat and mouse when he's mistaken\
                                 for a spy",
                                 "https://upload.wikimedia.org/wikipedia/commons/8/83/Northbynorthwest1.jpg",  # NOQA
                                 "https://www.youtube.com/watch?v=ek7T9Gyl_J4")  # NOQA

# Takes all instances of movie and makes a list for use by fresh_tomatoes
movies = [old_school, they_live, big_trouble_in_little_china,
          spaceballs, the_score, north_by_northwest]

# Opens a new browser window with the html site
fresh_tomatoes.open_movies_page(movies)
