# open
# file = open('file.txt','r')
# print(file.read())

# file.seek(0)
# file.read() #only reading operation can be performed.
# file.read(7) #first 7 char will be read.
# file.close() # To avoid leakage / breach of data.
# file.readline() #in order to read particular line. For loop will be used to read all the lines
# file.readlines() # output of Readlines will be List

# file = open('file.txt','w') #It will delete exsisting data.
# file.write('RAM RAM')
# file.write(7)
# file.close() # It will truncate all the data.

# # t='abcd'
# # file.write(t)

# file = open('file.txt','a') # Previous and new data  will exsist together with the help of append.
# file.write('ji')
# # append and write data will be shown when the file closes.

# with open ('file.txt','r') as file:
#     print(file.read()) #if we want to open and closes file only once not repetatively.

# with open ('file.txt',''w) as file:
#     print(file.write('Hello')) #if we want to open and closes file only once not repetatively.

# with open ('file.txt','a') as file:
#     print(file.read('hello \n')) #if we want to open and closes file only once not repetatively.

# import pywhatkit
# pywhatkit.search('machine learning')

# a="Machine learning (ML) is a field of study in artificial intelligence concerned with the development and study of statistical algorithms that can learn from data and generalize to unseen data, and thus perform tasks without explicit instructions.[1] Recently, generative artificial neural networks have been able to surpass many previous approaches in performance"
# file = open('file.txt','w')
# file.write(a)


# for i in range(len(a))
# n=int(input('num :'))
# part_a = a[i:i+n]
# i=i+n;
# file.write(a)

# if i>=len(a):
#     break

                                            # ERROR HANDLING
# import calendar
# y=int(input('year:'))
# m=int(input('month:'))
# print(calendar.month(y,m))


def divider(a,b):
    try:
        return a / b
    
#     except zero divisonError :
# print('something went wrong')
    
    except :
        print('hello')


                                                # JSON FILE 
# data stored as dictionary
# faster in comparison to others
# used for larger data input.
        
import json
        
with open('dummy.json','r') as file:
    text = file.read('')
    print(text)
        