import cv2

filePath = "test.jpeg"
image = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)

# deletes prev file
file_to_delete = open("output.txt",'w')
file_to_delete.close()

f = open("output.txt", "a")

# most luminous to least. total of 73 ascii characters
asciiCharacters = ['@', '&', '%', 'Q', 'W', 'N', '0', 'g', 'b', 'G', 'O', 'p', '4', 'd', '9', 'h', '6', 'P', 'k', 'q', 'w', 'S', 'E', '2', ']', 'a', 'y', 'j', 'x', '5', 'Z', 'o', 'e', 'n', '[', 'u', 'l', 't', '3', 'I', 'f', '}', '{', 'i', '|', '7', 'J', 'v', 'T', 's', '?', 'z', '/', '*', 'c', 'r', '!', '+', '>', '<', ';', '=', '^', ',', '_', ':', '-', "'", '.', ':', '"', '`', ' ']

output = ''

print("running")

# skips every other row, hardcoded cause i cant be bothered otherwise
for row in range(0, len(image),2):
    for col in range(0, len(image[row]), 1):
        currValue = round(image[row][col]/3.5)
        currValue = abs(currValue - 72)
        output += asciiCharacters[currValue]
    output += "\n"
    
f.write(output)
f.close()
