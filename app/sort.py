from app import app, db
from app.models import Games

''' 
Using a quicksort to sort the ratings of each game from highest to lowest
obviously, this could be done a much simpler way, but for the purpose of this assignment
I am demonstrating how we can use such an algorithm to sort data in an array.
I am using a Quicksort 
A quicksort divides and conquers recursively, 
it picks an index known as a 'pivot' to split the array into smaller arrays containing higher and lower numbers from
below and above the value of pivot. 
Quicksort 
list_ofgames(array) : the list of an array that is to be sorted
low(int): smallest index of the array
high(int) : the last index of the list_of_games array

The algorithm is mediocre efficiency when measured on BigO Notation
as it performs O(n2) at worse case due to its use of recursion.
'''


def add_games_to_array(games):
    list_of_games = []
    for game in games:
        list_of_games.append(game)
    quickSort(list_of_games,0, len(list_of_games) -1 ) 
    #passing through our orginal array, the smallest, and last index of our array
    return list_of_games
    
        
def partition(array, low, high): 
    i = (low-1)         
    #finding the index of the smallest value in array
    pivot = array[high].rating     
    #value at which larger array is split into 2 smaller arrays of higher and lower numbers
  
    for j in range(low, high):
        #sorting in descending order
        if array[j].rating >= pivot:
  
        
            i = i+1
            array[i], array[j] = array[j], array[i]
  
    array[i+1], array[high] = array[high], array[i+1]
    #swapping round smaller and higher values of sub arrays
    return (i+1)

def quickSort(array, low, high):
    if len(array) == 1:
        return array
    if low < high:
        pi = partition(array, low, high)
        #recusivly passing in the smaller arrays back through function
        quickSort(array, low, pi-1)
        quickSort(array, pi+1, high)
