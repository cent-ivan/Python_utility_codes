from jovian.pythondsa import evaluate_test_cases, evaluate_test_case

#when doing multiple test cases put test in dictionary and append it to a list
tests = [
    {'input':{'cards':[1,1,3,1], 'query':1}, 'output': [0,1,3]},
    {'input':{'cards':[1,4,6,12,0,0], 'query':6}, 'output':2},
    {'input':{'cards':[3,1,0,45,3], 'query':1}, 'output':1},
    {'input':{'cards':[40,1,9,6,34], 'query':34}, 'output':4},
    {'input':{'cards':[-4, -5, 8, 10], 'query':-5}, 'output':1},
    {'input':{'cards':[], 'query': 7}, 'ouput': -1},
    {'input':{'cards':[4], 'query':4}, 'output':0}
]

# #linear search algorithm
def locate(cards, query):
    duplicate_result = [] #for duplicated elements
    position = 0

    while position < len(cards):
        if cards[position] == query:

            if cards.count(cards[position]) > 1:  #check if the eleemtn is duplicated
                duplicate_result.append(position)
                if position == len(cards) - 1:   #check if it is the last element in the list
                    return duplicate_result     #if yes return a list of results
                else:
                    position += 1
            else:
                return position
            
        else:
            position += 1

    else:
        return None  
    

evaluate_test_cases(locate, tests)
