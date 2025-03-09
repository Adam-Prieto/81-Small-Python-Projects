house_bitmap = """
          /\       
         /  \      
        /    \     
       /______\    
      /        \   
     /          \  
    /____________\ 
   |    ____     | 
   |   |    |    |  
   |   |    |    |  
   |   |____|    | 
   |   _______   |        o
   |  |       |  |       /|
   |  |   []  |  |       / 
   |  |_______|  |  
   |_____________|  
"""
# Print the house bitmap
print(house_bitmap)

# Print the house bitmap
print(house_bitmap)

print("Please enter a word to use later in this program.")
message = input("> ")


for line in house_bitmap.splitlines():
    for j, bit in enumerate(line):
        if bit == ' ':
            print(' ', end='')
        else:
            print(message[j % len(message)], end='')
    print()