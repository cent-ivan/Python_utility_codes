    # position = len(cards) // 2

    # while position < len(cards):
    #     #take the right part of the halfed list
    #     if cards[position] < query:
    #         second_half = cards[position + 1 : ] #right part
    #         position = position + 1 + (len(second_half) // 2) #takes the middle of the right part
    #         if cards[position] < query:
    #             return position + 1
    #         elif cards[position] > query:
    #             return position - 1
    #         else:
    #             return position
                
    #     #take the left part of the halfed list
    #     elif cards[position] > query:
    #         first_half = cards[ : position ] #left
    #         position = len(first_half) // 2 #takes the middle of the left part
    #         if first_half[position] < query:
    #             return position + 1
    #         elif first_half[position] > query:
    #             return position - 1
    #         else:
    #             return position
            
    #     else:
    #         return position

    # else:
    #     return - 1