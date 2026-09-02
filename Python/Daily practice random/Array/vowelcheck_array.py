a = ["Apple","Banana","Orange","Grapes","Watermelon","Kiwi","Mango","Pineapple","Papaya","Stawberry"]
vowels = ["A" ,"a" ,"E", "e", "I", "i", "O", "o", "U", "u"]

for fruit in a:
    vowel_count = 0
    
    for letter in fruit:
        if letter in vowels:
            vowel_count += 1
            
    consonant_count = len(fruit) - vowel_count 
    print(f"{fruit} has {vowel_count} vowels and {consonant_count} consonants")
        