def swapFileData():

    file1=input("name of the file you want to transfer data to: ")
    file2=input("name of the file you want transfer data from: ")

    with open(file1, 'r') as a:
        data_a = a.read()

    with open(file2, 'r') as b:
        data_b = b.read()

    with open(file1, 'w') as a:
        a.write(data_b)
 
    with open(file2, 'w') as b:
        b.write(data_a)

print(swapFileData())
print("files swapped.")
