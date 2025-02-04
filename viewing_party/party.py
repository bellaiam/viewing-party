# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    movies_info = {}
    movies_info['title'] = title
    movies_info['genre'] = genre
    movies_info['rating'] = rating
    if not title or not genre or not rating:
        return None
    return movies_info

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data['watchlist']:
        if movie['title'] == title:   
            user_data['watchlist'].remove(movie)
            user_data['watched'].append(movie)
            # return user_data
    # If the movie is not found in the watchlist or the watchlist is empty, return the original user_data
    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    watched_movies = user_data.get("watched", [])
    if not watched_movies:
        return 0.0
    ratings_sum = 0.0 
    for movie_dict in watched_movies:
        ratings_sum += movie_dict.get('rating', 0.0)  
    return ratings_sum / len(watched_movies)

def get_most_watched_genre(user_data):
    genre_occur = {}
    if not user_data["watched"]:
        return None
    for movie_dict in user_data["watched"]:
        genre_occur[movie_dict["genre"]] = genre_occur.get(movie_dict["genre"], 0) + 1
    return max(genre_occur, key=genre_occur.get)



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data): 
    user_watched = set()
    user_watched_dict = {}
    for movie in user_data['watched']:
        user_watched.add(movie['title'])
        user_watched_dict[movie['title']] = movie
    friends_watched = set()
    for friend in user_data['friends']:
        for movie in friend['watched']:
            friends_watched.add(movie['title'])
    user_unique_watched = []
    for title in user_watched.difference(friends_watched):
        if title in user_watched_dict:
            user_unique_watched.append(user_watched_dict[title])
    return user_unique_watched


def get_friends_unique_watched(user_data):
    user_watched = []
    for movie in user_data['watched']:
        user_watched.append(movie['title'])
    friends_watched = []
    friends_watched_titles = []
    for friend in user_data['friends']:
        for movie in friend['watched']:
            title = movie['title']
            if title not in user_watched and title not in friends_watched_titles:
                friends_watched.append(movie)
                friends_watched_titles.append(title)

    friends_unique_watched = friends_watched
    return friends_unique_watched

    
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    friends_unique_watched = get_friends_unique_watched(user_data)
    recommended_list=[]
    for dict in friends_unique_watched:
        if dict["host"] in user_data["subscriptions"]: 
            recommended_list.append(dict)
    return recommended_list


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    user_fav_genre = get_most_watched_genre(user_data)
    friends_unique_watched = get_friends_unique_watched(user_data)
    rec_by_genre = []
    for dict in friends_unique_watched:
        if user_fav_genre == dict["genre"]:
            rec_by_genre.append(dict)
    return rec_by_genre


def  get_rec_from_favorites(user_data):
    rec_list = []
    friends_not_watched = get_unique_watched(user_data)
    for dict in user_data["favorites"]:
        if dict in friends_not_watched:
            rec_list.append(dict)
    return rec_list