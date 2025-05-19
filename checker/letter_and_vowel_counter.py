import time
print("\nThis program counts how many letters and vowels of a word")

def letter_counter():
    print("\nLetter Counter")
    word = input("Enter a word: ").lower()
    result = {}
    remove_duplicates = set()

    #removes the duplicated letters in word variable
    for letters in word:
        remove_duplicates.add(letters) 

    #loops the data inide the removes_duplicates (set  data type)
    for letters2 in remove_duplicates:
        number = word.count(letters2)
        result[letters2.upper()]= number

    print(f"\"{word}\" has {len(word)} letters")
    print(result)

#----------------------------------------------------------------------------------------------------
def vowel_counter():
    print("\nVowel Counter")
    word = input("Enter a word: ").lower()
    vowels = "aeiou"
    result = {}
    setVar = set()
    

    #removes the duplicated letters in word variable
    for letter in word:
        if letter in vowels:
            setVar.add(letter)

    for i in setVar:
        key_word = i.upper()
        num = word.count(i)
        result[key_word] = num

    count = len(result)
    print(f"\n\"{word}\" have {count} vowel/s.\n{result}")

#----------------------------------------------------------------------------------------------------
#Starting prompt for the user
def action():
    time.sleep(2)
    print("\nChoose what you will do.")
    ask_user = int(input("[1] Letter Counter\n[2] Vowel Counter: "))

    if ask_user == 1:
        letter_counter()
    elif ask_user == 2:
        vowel_counter()
    else:
        print("Uknown Command. Please try again")
        action() #recursion

action()