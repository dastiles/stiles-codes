from math import sqrt

# A dictionary of movie critics and their ratings of a small
# set of movies
critics = {'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
                         'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
                         'The Night Listener': 3.0},
           'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
                            'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
                            'You, Me and Dupree': 3.5},
           'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
                                'Superman Returns': 3.5, 'The Night Listener': 4.0},
           'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
                            'The Night Listener': 4.5, 'Superman Returns': 4.0,
                            'You, Me and Dupree': 2.5},
           'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                            'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
                            'You, Me and Dupree': 2.0},
           'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                             'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
           'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0, 'Superman Returns': 4.0}}

# returns a distance-based similarity score for person1 and person2


def sim_distance(prefs, p1, p2):
    # get the list of shared items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    #         # if they have no rating in common return 0
    if len(si) == 0:
        return 0
    # print(si)

    # add up the squares of all the diffrence
    sum_of_squares = sum([pow(prefs[p1][item]-prefs[p2][item], 2)
                          for item in prefs[p1] if item in prefs[p2]])

    return 1/(1+sum_of_squares)


print(sim_distance(critics, 'Jack Matthews', 'Mick LaSalle'))

# returns the pearson corretaion for p1 and p2


def sim_pearson(prefs, p1, p2):
    # get the list mutually rated items
    si = {}
    for i in prefs[p1]:
        if i in prefs[p2]:
            si[i] = 1

    # find the number of elements
    n = len(si)

    #  if they no ratings in common return 0
    if n == 0:
        return 0

    # add all preferances
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    # sum up the squares
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])

    # sum up the products
    pSum = sum([prefs[p1][it]*prefs[p2][it] for it in si])

    # calculate Pearson score
    num = pSum-(sum1*sum2/n)
    den = sqrt((sum1Sq-pow(sum1, 2)/n)*(sum2Sq-pow(sum2, 2)/n))
    if den == 0:
        return 0
    r = num/den
    return r


print(sim_pearson(critics, 'Lisa Rose', 'Gene Seymour'))


def topMatches(prefs, p, n=5, sim=sim_pearson):
    scores = [(sim(prefs, p, other), other) for other in prefs if other != p]
    scores.sort()
    scores.reverse()
    return scores[0:n]


# print(topMatches(critics, 'Lisa Rose', n=3))


def getRecommendations(prefs, p, siml=sim_pearson):
    totals = {}
    simSums = {}
    for other in prefs:
        # dont compare to myself
        sim = siml(prefs, p, other)

        # ignore score of zero or lower
        if sim <= 0:
            continue
        for item in prefs[other]:
            # only score movies i havent seen yet
            if item not in prefs[p] or prefs[p][item] == 0:
                # similarity * score
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item]*sim
                # sum of similarites
                simSums.setdefault(item, 0)
                simSums[item] += sim
        # create the normal list
        rankings = [(total/simSums[item], item)
                    for item, total in totals.items()]

        # return the sorted list
        rankings.sort()
        rankings.reverse()
        return rankings


# print(getRecommendations(critics, 'Jack Matthews'))


def tranformPrefs(prefs):
    result = {}
    for p in prefs:
        for i in prefs[p]:
            result.setdefault(i, {})
            # print(result)
            result[i][p] = prefs[p][i]
    return result


movies = tranformPrefs(critics)
print(topMatches(movies, 'Superman Returns'))
print(getRecommendations(movies, 'Superman Returns'))
