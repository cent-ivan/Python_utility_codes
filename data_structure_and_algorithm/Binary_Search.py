#binary search algorithm version 5

#test1 = [1,4,12,12,12,12,15,21,25,28]
test1 = [28, 25, 25, 25, 8, 8, 3]

#created helper function to locate other duplicated elements in a REVERSE list
def test_duplicate_reverse(cards, query, position):
    if cards[position] == query:
        if position - 1 >= 0 and cards[position - 1] == query: #check if the left of the mid is the same
            return "left"
        else:
            return "found"
    elif cards[position] > query:
            return "right"
    else:
        return "left"
    
#created helper function to locate other duplicated elements
def test_duplicate(cards, query, position):
    if cards[position] == query:
        if position - 1 >= 0 and cards[position - 1] == query: #check if the left of the mid is the same
            return "left"
        else:
            return "found"
    elif cards[position] > query:
            return "left"
    else:
        return "right"
    

#binary search----------------------------------------------------------------------------------------------------------------
def binary_search(cards, query):
    start = 0
    
    if len(cards) - 1 == -1: #catches if the cards is empty
        return -1
    else:
        end = len(cards) - 1

    if cards[start] > cards[end]: #check first if the list is reverse
        while start <= end:
            position = (start + end) // 2 #gets the middle poisiton
            part = test_duplicate_reverse(cards, query, position) #checks for duplicate and get its location
            
            if part == "left": #if reverse and middle is less than query, the position of the list is subtracted and become the new end to go to the left side
                end = position - 1
            elif part == "right": #if reverse and middle is greater than query, the position of the list is incremented and become the new start to go to the right side
                start = position + 1
            else:
                return position
            
        else:
            return -1  #did not found
        
    else:
        while start <= end:
            position = (start + end) // 2
            part = test_duplicate(cards, query, position) #checks for duplicate and get its location
            
            if part == "left": #if middle is greater than query, the position is subtracted and become the new end to go to the left side
                end = position - 1
            elif part == "right": #if middle is less than query, the position is incremented and become the new start to go to the right side
                start = position + 1
            else:
                return position
    
        else:
            return -1  #did not found

result = binary_search(test1, 3)
print(result)