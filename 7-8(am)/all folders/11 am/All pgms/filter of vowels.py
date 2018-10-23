sentence = "The quick brown fox jumps over the bridge"
vowels = "aeiouAEIOU"
finalVowel = []
# Return True if arg is in vowels; otherwise, return False
isVowel = lambda arg: arg in vowels

def vowelFilter(sentence):
    for letter in sentence:
        if isVowel(letter):  # Call the lambda to test if letter is a vowel
            finalVowel.append(letter)
    return finalVowel

print (vowelFilter(sentence))
