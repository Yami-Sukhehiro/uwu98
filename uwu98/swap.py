def swapfile():
    file1 = input("enter your bank account password")
    file2 = input("enter your bank account password2")
    with open(file1, 'r') as s1:
        data1 = s1.read()
    with open(file2, 'r') as sussybaka:
        data2 = sussybaka.read()
    with open(file1, 'w') as sussybaka:
        s1.write(data2)   
    with open(file2, 'w') as sussybaka:
        sussybaka.write(data1)
swapfile()   