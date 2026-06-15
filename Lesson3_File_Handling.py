# ### **Steps to be followed:**

# 1. Read a file
# 2. Write to a file
# 3. Append to a file
# 4. Read after writing
# 5. Read line by line
# 6. Write strings and close the file



with open("example.txt","r") as file:
    content = file.read()
    print(content)

# with open("example.txt","w") as file:   
#     file.write("Hello, World!") 

with open("example.txt","a") as file:
    file.write("\nThis is a new line.")

with open("example.txt","r") as file:
    content = file.read()
    print(content)

print("Line by line:")

with open("example.txt","r") as file:
    for line in file:
        print(line.strip())

file = open("example1.txt", "w")
file.write("Final content replacing everything.\n")
file.write("Closing the file explicitly.\n")
file.close()  # Manually closing the file