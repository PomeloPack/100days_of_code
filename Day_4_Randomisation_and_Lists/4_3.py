
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

#left to rigt
horizontal = int(position[0])

# up to down
vertical = int(position[1])

#there isn't row in position 3 ( list start from 0 to up) we use - 1 
map[vertical -1][horizontal - 1 ] = "X"

print(f"{row1}\n{row2}\n{row3}")