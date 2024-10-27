# f = open("read.txt", "r")
# result = f.read()
# print(result)
# Read the file f


# ==> method 1
# f = open("write.txt", "w")
# result = f.write("I am writing a new line in write File")

# ==> method 2

f = open("write.txt", "a")
result = f.write(" append this line in the write file")

#  we can use both methods for reading and writing the file

# if the write file is not available in this folder then the compiler will create the write.txt file