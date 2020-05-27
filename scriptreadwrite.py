
# r- read, w- (over writing), r+ -read and append, a- append
my_file = open('my_file.txt','r+')


print(my_file.read())
my_file.write('Please yeeeee\n')




my_file.close()
