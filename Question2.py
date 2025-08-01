with open('output.txt','r+') as file2:
    str3 = str(input('Enter text to write to the file:'))
    file2.write(str3+'\n')
    print('Data Successfully written to output.txt.')
with open('output.txt','a') as file3:
    str1=str(input('Enter additional text to append:'))
    file3.write(str1)
    print('Data Successfully appended.')
with open('output.txt', 'r+') as file4:
    obj = file4.read(100)
    print('Final content of output.txt:\n',obj)