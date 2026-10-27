print("----text analyzer---------")
text=input("please enter the text here !!")
charc=len(text)
words = text.split()
word_count=len(words)
vowels=0
spaces=0
for chars in text:
    if chars.lower() in "aeiou":
        vowels=vowels+1
    if chars == " ":
        spaces=spaces+1
print("-------result-------")
print(f"original text:{text}")
print(f"total charc:{charc}")
print(f"Total words: {word_count}")
print(f"total vowels:{vowels}")
print(f"total spaces:{spaces}")
print(f"upper:{text.upper()}")
print(f"lower:{text.lower()}")
print(f"reverse:{text[::-1]}")
