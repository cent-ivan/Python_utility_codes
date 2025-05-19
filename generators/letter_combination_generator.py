import random
#How many differemt words can you make with A,B,C,D without repetition
letters = ["A", "B", "C", "D","E"]

class LetterCombinationGenerator:
    def __init__(self) -> None:
        self.words = [] #stores all of the combinations


    def is_duplicate(self, data:str) -> bool:
        upper_data = data.upper()
        counter = 0

        #loops the data to check if it si duplicated (set  data type)
        for letters in upper_data:
            number = upper_data.count(data)
            counter += number
        
        if counter > 1:
            return True
        else:
            return False
        

    def factorial(self, n:int) -> int:
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)
        
    #N= Total numbers of distinct items, r=number of items to arrange, and factorial method
    def permutation(self, N, r, factorial) -> int:
        permu = factorial(N) / factorial(N - r)
        return int(permu)

generator = LetterCombinationGenerator()
ans = generator.permutation(len(letters),3, (generator.factorial))

#accepts the total length of each combinations
def create_combinations(length:int) -> None:
    #creates the combinations
    while len(generator.words) != ans:
        word = ""
        while True:
            if len(word) != length:
                letter = random.choice(letters)
                if letter in word:
                    continue
                else:
                    word += letter
            else:
                break

        #checks to the word list if there and checks for duplicates if yes reset 
        if word in generator.words and generator.is_duplicate(word):
            word = ""
            continue
        else:    
            generator.words.append(word)

length = int(input(f"Enter Length of each combinations not greater that {len(letters)}: "))
create_combinations(length)

generator.words.sort()
for k in generator.words:
    print(k)

print(f"\nTotal Words: {len(generator.words)}")



