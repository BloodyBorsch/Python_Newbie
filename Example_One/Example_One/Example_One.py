class LessonOne:

    count = 0    
    firstFriendSpeed = 1
    secondFriendSpeed = 2
    dogSpeed = 5
    distance = 0
    minDistanceBetween = 10
    
    def TimeCount(distance, speedOfFriend, speedOfDog):        
        distance/(speedOfFriend + speedOfDog)
        
    def DistanceCheck(distanceBetween, minDistance):       
        return(bool(distanceBetween > minDistance))    
    
    #print(DistanceCheck(distance, minDistanceBetween))            

class LessonTwo:
    
    count = 0
    factorial = int(input())    
    solution = 1

    while count < factorial:
        count += 1
        solution *= count
    else:
        print(solution)
        
    
    
    