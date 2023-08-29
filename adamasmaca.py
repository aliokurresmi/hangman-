isim = input("isminizi girin: ")
print("merhaba",isim,"adam asmaca oyununa hoş geldin!!!")

secret_word = "kalem"

guess_string = ""

can = 10


while can > 0:

    character_left = 0
    for character in secret_word:
        if character in guess_string:
            print(character)
        else:
            print("-")
            character_left += 1
    
    if character_left == 0:
        print("kazandınız!")
        break


    guess = input("harf tahmin edin: ")
    guess_string += guess

    if guess not in secret_word:
        can -= 1
        print("yanlış")
        print(f"{can}'ın kaldı")
   
    if can == 0:
        print("öldün")