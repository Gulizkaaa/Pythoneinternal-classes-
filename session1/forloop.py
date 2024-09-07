sentence = """Python is a versatile and widely-used programing labguage."""

inp = input("Please give a word: ")
#print(sentence.find(inp))

if "and" in sentence:
    print(sentence.find(inp))
else:
    print("please try again")

