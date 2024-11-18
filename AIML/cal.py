class bestfriend:
    bestfriend = {}
    def __init__(self,name,name_best,bestfriend):
        self.name = name
        self.bestfriend[str(name)] = []
        print (self.name , self.bestfriend )


#return type of args is tuple

# class dog:
#     tricks = []
#     def __init__(self,name,bread,trick):
#         self.name = name
#         self.bread = bread
#         self.trick = trick
#         print (self.name , self.bread ,self.trick)

# def adder(a,b,*args):
#     print(a)
#     print(b)
#     print(args)
#     print(*args)

# adder(1,2,3,4,5,6,name='Jugal',age=18):

# class-> Blueprint of something.
# Function,Class,Variable can be called
# Function define in a class is called method

# class Studdent:
#     mentor='Tushar'
#     age =40
#     def hell

# a=student()
# print(a)
# print(a.mentor())
# print(a.age())

# def hello(self,name,age):
#     self.mentor = "mentor"
#     print(name,age)

# a=Student()
# a.mentor()

# a.hello("Hi",1)

#SET

# li_1=[]
# li_2=[]

# for i in range(50,150):
#     li_1.append(i)

# for j in range(100,150):
#     li_2.append(j)

# set_1 =set(li_1)
# set_2 =set(li_2)

# print(set_1.intersection(set_2))
# print(set_1.union(set_2))


# def add(a,b,*x):
#     a = a+b
#     for i in x:
#         a = a+i
#     return a
# print(add(1,2,32,3,2,3,4,45,5))