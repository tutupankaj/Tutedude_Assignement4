try:
   file1 = open('sample.txt','r')
   obj1 = file1.read(100)
   print(obj1)
   file1.close()
except:
    print('Error:The file \'Sample.txt\' was not found')
