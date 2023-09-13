# Find out whether the given character is Vowel or Consonant.
ch=input("Enter a character: ")
str='aeiouAEIOU'
if ch not in str:
    print(f"'{ch}' is a Consonant")
else:
    print(f"'{ch}' is a Vowel")
    
    
