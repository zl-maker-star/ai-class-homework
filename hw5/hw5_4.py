#**********Zoey Lursky 9th 5**************

# קלט: מספר השחקנים
players = int(input("Enter the number of players: "))
min_number=5
# בדיקה אם אפשר להרכיב שתי קבוצות של 5 שחקנים כל אחת
if players >= min_number*2:
    print("you can play with " ,players//min_number,"teams")
else:
    print("There are not enough players to form 2 teams.")