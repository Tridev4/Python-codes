def count_vowel(st):
    v='aeiouAEIOU'
    print(len([letter for letter in st if letter in v]))
    print([letter for letter in st if letter in v])
st=input('Enter a string:')
print(count_vowel(st))