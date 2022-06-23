#import pandas as pd
#import numpy
#import array as arr

totaloptimaldistance =[1956.409536989422, 8336.093073178992,  18772.245730020917, 4025.563128828079,  11593.249515449956]
countryList = ['KR', 'JP', 'CA', 'GB', 'CN']
scoreList=[1, 3, 1, -3, 3]

def minimumvalue(scoreList,totaloptimaldistance): #define function minimumvalue
    minValues = [min(scoreList),min(totaloptimaldistance)] #return min value of score and distance

    return minValues

def maximumvalue(scoreList,totaloptimaldistance): #define function maximumvalue
    maxValues = [max(scoreList),max(totaloptimaldistance)] #return max value of score and distance

    return maxValues

def calculateScore(scoreList,totaloptimaldistance): #calculate score using minmax normalization
    #score = (value-min/max-min) x weight

    countryScore = [] #initialize list for country score
    min = minimumvalue(scoreList,totaloptimaldistance)[0] #get the minimum score
    max = maximumvalue(scoreList,totaloptimaldistance)[0] #get the maximum score
    factor = max - min #denominator

    for i in range(len(scoreList)): 
        score = ((scoreList[i] - (min-0.01))/factor)*50  #calculate country score
        countryScore.append(score)

    return countryScore    

def calculateDistanceScore(scoreList,totaloptimaldistance): #calculate score using reversed min max normalization
    # score = (max-value/max-min) x weight

    distanceScore = [] #initialize list for distance score
    min = minimumvalue(scoreList,totaloptimaldistance)[1] #get the minimum distance score
    max = maximumvalue(scoreList,totaloptimaldistance)[1] #get the maximum distance score
    factor = max - min #denominator

    for i in range(len(totaloptimaldistance)): 
        score = (((max+0.01) - totaloptimaldistance[i])/factor)*50 #calculate country score
        distanceScore.append(score)

    return distanceScore

def overallScore(scoreList,totaloptimaldistance):#calculate overall score based on sentiment and distance
    #sentimentScore + distanceScore
    overallScore = [] # initialise List for sentiment score
    
    for i in range(len(scoreList)):
        overallScore.append (calculateScore(scoreList, totaloptimaldistance)[i] + calculateDistanceScore(scoreList, totaloptimaldistance)[i])
    
    return overallScore

def calculateProbability(scoreList, totaloptimaldistance): # calculate probability of selecting each country
    probList = [] # intitialise list for probability
    overall_Score = overallScore(scoreList, totaloptimaldistance) # calculate overall score
    total = sum(overall_Score) # sum of all countries overall score
    
    for i in range (len(overall_Score)) :
        prob = overall_Score[i] / total # calculate probability using score per total score
        probList.append(prob)
    
    return probList

def sortProbability(scoreList, totaloptimaldistance): #sorting the countries based on overall score
    probability = calculateProbability(scoreList, totaloptimaldistance) ## calculate probability of each country

    #quicksort totalscore
    def partition(l, r, list):
        pivot, pointer = list[r], l # assign pivot and pointer

        for i in range(l, r):
            if list[i] <- pivot: # check if element is smaller than pivot
                list[i], list[pointer] = list[pointer], list[i]
                pointer += 1
        list[pointer], list[r] = list[r], list[pointer]
        return pointer

    def quicksort (l, r, list):
        if len(list) == 1:
            return list

        if l < r:
            pi = partition(l, r, list)
            quicksort(l, pi - 1, list)
            quicksort (pi + 1, r, list)
        return list

    sortedProb = quicksort(0,len(probability)-1,probability) #call quick sort

    sortedProb.reverse() #reverse the order after sorting

    return sortedProb

def sortCountries (countries,scoreList,totaloptimaldistance):
    countryList = countries # copy of countries
    unsortedScore = calculateProbability(scoreList, totaloptimaldistance) # calculate probability
    sortedOverallScore = sortProbability(scoreList,totaloptimaldistance) #sort probability
    sortedCountrylist = [] # final sorted countries

# get rankings of country based on overall score
    for i in range(len(sortedOverallScore)):
        for j in range(len(unsortedScore)):
            if (sortedOverallScore[i] == unsortedScore[j]):
                sortedCountrylist.append(countries[j])
    
    return sortedCountrylist    

def Ranking (countries,scoreList,totaloptimaldistance): # ranking the countries
    rankedCountries = sortCountries(countries, scoreList, totaloptimaldistance) # sort countries
    
    scores = sortProbability(scoreList, totaloptimaldistance) # sort scores

    print("\n\t\tThe ranking on the countries based on the score ")
    print("n-------------------------------------------------------------")

    for i in range(len(rankedCountries)): # print the rankings of countries
        format_score = "{:.5f}".format(scores[i])
        print(str(i + 1) + "st position :" + rankedCountries[i] + " with the probability of " + format_score)

    print ("\nthe most recomended country is " + rankedCountries[0])
    print ("\n----------------------------------------------------------------")

#totaloptimaldistance = list(countryDistance.values())
    Ranking(countries, scoreList, totaloptimaldistance)