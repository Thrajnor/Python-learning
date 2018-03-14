import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "Historia chlopca i jego zabawek",
                        "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0%2C0%2C300%2C450",
                        "https://www.youtube.com/watch?v=JcpWXaA2qeg",
                        "120m")
avatar = media.Movie("Avatar",
                     "Film o niebieskich ludzikach",
                     "http://cafmp.com/wp-content/uploads/2012/12/Avatar-Neytiri.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "170m")
school_of_rock = media.Movie("School of Rock",
                             "Film o roku",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc",
                             "120m")

steinsgate = media.Tvseries("Steins;Gate",
                         "Anime o czasie",
                         "https://vignette.wikia.nocookie.net/vsbattles/images/2/2a/Steins%3BGate.jpg/revision/latest?cb=20160314191813",
                         "https://www.youtube.com/watch?v=LwcTi86cFeg",
                         "120m")
arrow = media.Tvseries("Steins;Gate",
                     "Anime o czasie",
                     "https://vignette.wikia.nocookie.net/vsbattles/images/2/2a/Steins%3BGate.jpg/revision/latest?cb=20160314191813",
                     "https://www.youtube.com/watch?v=LwcTi86cFeg",
                     "120m")
#movies = [toy_story,avatar,steinsgate,school_of_rock]
#fresh_tomatoes.open_movies_page(movies)
#print(steinsgate.title)
#print(steinsgate.storyline)
#steinsgate.show_image()
#steinsgate.show_trailer()
print(media.Movie.VALID_RATINGS)
