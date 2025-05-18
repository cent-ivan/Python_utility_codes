#All in converter for the binary converters
print("Select a converter")
print("""
    1. Binary to Decimal Converter
    2. Decimal to Binary Converter
    3. Hexadecimal to Binary Converter
""")

#Parent Class
class Converter:
    def get_input(self):
        data = input("Enter data to be converted: ")
        return data

    def convert(self, data): pass


#BINARY TO DECIMAL loops through the binary and add only the 1s
class BinaryDecimal(Converter):
    def get_input(self):
        print("\nBinary to decimal Converter-------------------")
        return super().get_input() #super() lets you use the parents methods or properties
    
    def convert(self, binary:str) -> int:
        exponent:int = 0 #starts with 0 then raises as the counting continues
        sum:int = 0
        for bit in binary[::-1]: #reverse because binary starts right to left
            sum += (int(bit) * (2 ** exponent))
            exponent += 1
        
        return sum


#DECIMAL TO BINARY divides to 2 and assigns 1s if there is a remainder, 0 if none
class DecimalBinary(Converter):
    def __init__(self) -> None:
        self.binary = []

    def get_input(self):
        print("\nDecimal to binary Converter-------------------")
        return int(super().get_input())
    
    def convert(self, decimal:int) -> str:
        if decimal == 0: #break case
            pass
        elif decimal % 2 == 1: 
            self.binary.insert(0,'1')
            self.convert(decimal // 2) #recursion
        else:
            self.binary.insert(0,'0')
            self.convert(decimal // 2)

        #convert to a byte
        if len(self.binary) < 8:
            add = "0" * (8 - len(self.binary))
            byte = add  +  "".join(self.binary)
            return byte
        return "".join(self.binary)


#HEXADECIMAL TO BINARY checks the pre-made hex dictionary for the equivalent binary
class HexadecimalBinary(Converter):
    def __init__(self) -> None:
        self.hex = {
            "0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001",
            "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"
        }
    
    def get_input(self):
        print("\nHexadecimal to binary Converter-------------------")
        return super().get_input()

    def convert(self, hex_data:str) -> str:
        binary = ""

         #converted to a list to check each bit, make it big first
        hex_list = list(hex_data.upper())
        for bit in hex_list:
            if bit in self.hex:
                binary += self.hex[bit]
                binary += " " #add space
            else:
                binary += "null"
                binary += " " #add space
        
        return binary



#-------------------------------------------------------------
#returns the choosen class dynamically, FACTORY PATTERN
class ConverterFactory:
    @staticmethod
    def get_converter(choice:int) -> Converter:
        if choice == 1:
            return BinaryDecimal()
        elif choice == 2:
            return DecimalBinary()
        elif choice == 3:
            return HexadecimalBinary()        
        else:
            raise ValueError("\n[!]Unknown Command")


#starts here. User chooses what converter and enters what data to be converted
def convert_data() -> None:
    try:
        choice = int(input("Select a number: "))
        converter = ConverterFactory.get_converter(choice)
        print(converter.convert(converter.get_input()))

    except TypeError:
        print("\nInvalid key. Try again and use a number\n")
        convert_data()
    
    except Exception:
        raise Exception


convert_data()
