from random import randrange

while True:
    comp = randrange(3) + 1
    print(''' ქვა, ფურცელი, მაკრატელი.
        პირობითი ნუმერაცია:
                        0. თამაშის დასრულება
                        1. ქვა
                        2. ფურცელი
                        3. მაკრატელი
        ''')
    user = int(input('აირჩიეთ:'))
    if user == 0:
        print('თამაშის დასრულება!')
        break
    elif user == 1:
        print('თქვენ აირჩიეთ ქვა')
    elif user == 2:
        print('თქვენ აირჩიეთ ფურცელი')
    elif user == 3:
        print('თქვენ აირჩიეთ მაკრატელი')
    else:
        exit('თქვენ შეიყვანეთ არასწორი მონაცემები, დაიწყეთ თავიდან!')

    if comp == 1:
        print('კომპიუტერმა აირჩია ქვა')
    elif comp == 2:
        print('კომპიუტერმა აირჩია ფურცელი')
    elif comp == 3:
        print('კომპიუტერმა აირჩია მაკრატელი')

    if comp == user:
        print('თამაში დამთავრდა ფრედ')
    elif comp == 1 and user == 3 or comp == 2 and user == 1 or comp == 3 and user == 2:
        print('თქვენ დამარცხდით')
    elif user == 1 and comp == 3 or user == 2 and comp == 1 or user == 3 and comp == 2:
        print('გილოცავთ, თქვენ გაიმარჯვეთ!!')
