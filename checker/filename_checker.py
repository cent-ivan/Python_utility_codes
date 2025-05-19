filename_dict = {".py":"Python", ".java":"Java", ".cpp":"C++", ".js":"Javascript"}
data = input("Enter filename: ")
dot_index = data.index(".")

for filename in filename_dict:
    if data[dot_index:].lower() == filename:
        print(f"\nProgramming Language Detected: {filename_dict[data[dot_index:]]}")
