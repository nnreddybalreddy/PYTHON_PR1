import re 
def panagram(phrase):
    letters=re.sub(r"[^a-zA-Z]","",phrase)
    letter_set=set(letters.lower())
    if len(letter_set) == 26:
        return True
    else:
        return False

str="The quick brown ox jumps over the lazy dog"
print(panagram(str))