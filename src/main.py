import time
l=range(100000000)
v=range(1000000)
T1=time.time()
s=list(l)+list(v)
T2=time.time()
print(' + execution time: :' , T2-T1,  's')
T3=time.time()
l.extend(v)
T4=time.time()
print('extend execution time:', T4-T3 , 's')
stack=[1, 2, 3, 4]
print("Initial Stack : ", stack)
for i in range(5,7):
  stack.append(i)
  print ("Append: ", stack)
  stack.pop()
  print ("Pop: " , stack)
queue=[ 'a','b','c','d' ]
print("Initial Queue : ", queue)
queue.append('e')
queue.append('f')
print("Append : ", queue)
queue.pop(0)
print("Pop : ", queue)
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print("tup1[0]: ", tup1[0])   
print("tup2[1:5]: ", tup2[1:5])  
tup = ('physics', 'chemistry', 1997, 2000)
print(tup)
mydict={1:'Lucrezia', 2:'Luca'}
print(mydict)
mydict2={'name':'John', 1:[2,3,4]}
print(mydict2)
my_dict = dict([(1,'apple'), (2,'ball')])
print(my_dict)
print(my_dict[1])
print(my_dict.get(1))
my_dict['yes']='no'
print(my_dict)
squares={x:x*x for x in range(7)}
print(squares)
odd_squares={x:x*x for x in range(7) if x%2==1}
print(odd_squares)
number = 23
var = True


while var:
    guess=int(input('Enter an integer : '))
    if (guess==number):
        print('yeeeeee')
        var = False
    elif (guess<number):
        print('è più alto')
    else: 
        print('è più basso')

print('fatto')    
