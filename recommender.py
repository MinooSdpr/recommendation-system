from math import sqrt
import csv


def csvToDic(filename):
    dictionary = dict()
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for record in reader:
            username = record[0]
            movie = record[1]
            rating = float(record[2])
            if username not in dictionary:
                dictionary[username]=dict()
            dictionary[username][movie] = rating

    return dictionary

def manhattan(rating1, rating2):
    distance = 0
    commonRatings = False 
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
            commonRatings = True
    if commonRatings:
        return distance
    else:
        return -1


def computeNearestNeighbor(username, users):
    distances = []
    for user in users:
        if user != username:
            distance = manhattan(users[user], users[username])
            distances.append((distance, user))
    distances.sort()
    return distances

def recommend(username, users):
    nearest = computeNearestNeighbor(username, users)[0][1]

    recommendations = []
    neighborRatings = users[nearest]
    userRatings = users[username]
    for artist in neighborRatings:
        if not artist in userRatings:
            if neighborRatings[artist]>=3:
                recommendations.append((artist, neighborRatings[artist]))
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)


users = csvToDic("movie_rating.csv")
print(users)
print("\n recommend example for john", recommend('john', users))