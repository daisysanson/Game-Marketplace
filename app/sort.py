from app import app, db
from app.models import Games

#render in view page 

def add_games_to_array(games):
    list_of_games = []
    for game in games:
        list_of_games.append(game)

    print(list_of_games)
    quickSort(list_of_games,0, len(list_of_games) -1 )
    print(list_of_games)
    return list_of_games
    
        
def partition(array, low, high):
    i = (low-1)         
    pivot = array[high].rating     
  
    for j in range(low, high):
  
        if array[j].rating <= pivot:
  
        
            i = i+1
            array[i], array[j] = array[j], array[i]
  
    array[i+1], array[high] = array[high], array[i+1]
    return (i+1)

def quickSort(array, low, high):
    if len(array) == 1:
        return array
    if low < high:
        pi = partition(array, low, high)
  
        quickSort(array, low, pi-1)
        quickSort(array, pi+1, high)
