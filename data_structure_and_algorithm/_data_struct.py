from jovian.pythondsa import evaluate_test_cases, evaluate_test_case

#when doing multiple test cases put test in dictionary and append it to a list
tests = [
    {'input':{'cards':[1,4,6,12], 'query':6}, 'output':2},
    {'input':{'cards':[12,6,4,1,0], 'query':12}, 'output':0},
    {'input':{'cards':[-3,-4,-6,-25], 'query':-25}, 'output':3},
    {'input':{'cards':[92,93,93,93,102,204,500], 'query':93}, 'output':1},
    {'input':{'cards':[], 'query': 7}, 'ouput': -1},
    {'input':{'cards':[4], 'query':4}, 'output':0}
]

#test for large list
test2 = [
    {'input':{'cards':[i for i in range(1,10000)], 'query':9999}, 'output':9998}
]

