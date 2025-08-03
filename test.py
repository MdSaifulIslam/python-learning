import pprint

students = { 'ab1' : {'name' : 'name1', 'class' : 5, 'marks' : 400},
             'ab2' : {'name' : 'name2', 'class' : 5, 'marks' : 433},
             'ab3' : {'name' : 'name3', 'class' : 5, 'marks' : 324},
             'ab4' : {'name' : 'name4', 'class' : 6, 'marks' : 233},
             'ab5' : {'name' : 'name5', 'class' : 7, 'marks' : 143},
             'ab6' : {'name' : 'name6', 'class' : 6, 'marks' : 656},
             'ab7' : {'name' : 'name7', 'class' : 7, 'marks' : 435}
            }

##p_students = {id: 'Pass' + ', marks : ' + str(record['marks']) +
##              ', class : ' + str(record['class']) +'.'
##              if record['marks'] > 250 else 'Fail'
##              for id, record in students.items() if record['class'] < 8}
##pprint.pprint(p_students)

##print('\nGrouped by mark\n')
##grouped = {
##    cls: {id: stu for id, stu in students.items() if stu['class'] == cls}
##    cls for cls in set(stu['class'] for stu in students.values())
##}

grouped_by_mark = {
    markgroup: {
        id : stu
        for id, stu in students.items()
        if (stu['marks'] >= markgroup and stu['marks'] < (markgroup + 100))
        
        }
    for markgroup in set((stu['marks']//100)*100 for stu in students.values())
    } 

pprint.pprint(grouped_by_mark)



##L = [2, 5, 6, 7, -9, -3, -7]
##d = {n : n**2 for n in L if n > 0}
##print(d)

##---transpose matrix
##table = [
##    [1, 2, 3, 4, 5],
##    [1, 2, 3, 4, 5],
##    [1, 2, 3, 4, 5],
##    [1, 2, 3, 4, 5],
##    [1, 2, 3, 4, 5],
##    ]
##
##table = [ [row[i] for row in table if i < len(row)]
##          for i in range(len(table)*2 -1, 0, -1)
##          for j in i]
##pprint.pprint(table)

##s1 = 'xyZ'
##s2 = 'ABc'
##
##l1 = [ch1 + ch2 for ch2  in s2 if ch2.isupper() for ch1 in s1 if ch1.islower()]
##pprint.pprint(l1)

##L = [1, 2, 3, 4, 5, -1, -3, -4, 5]
##L2 = [n  for n in L if n>0 else 0]
##print(L2)



##students = {
##    'a1' : {'name' : 'Abdul', 'age' : 33, 'grade' : 'A+'},
##    'b2' : {'name' : 'Jabbar', 'age' : 24, 'grade' : 'B+'},
##    'c2' : {'name' : 'Kamal', 'age' : 52, 'grade' : 'A+'},
##    'd2' : {'name' : 'Sagor', 'age' : 42, 'grade' : 'A+'},
##    'l3' : {'name' : 'Saidul', 'age' : 21, 'grade' : 'C-'},
##    'p2' : {'name' : 'Asif', 'age' : 33, 'grade' : 'D'},
##    }
##
##data1 = [(data['name'], data['grade'])
##          for  data in students.values()
##          if data['grade'][-2:] == 'A+']
##pprint.pprint(data1)

##matrix = [
##    [1, 2, 3, 4],
##    [5, 6, 7, 8],
##    [9, 10, 11, 12],
##]
##m2 = [[row[i] for row in matrix] for i in range(4)]
##print(m2)
##
##for i in range(4):
##    for row in matrix:
##        print(row[i])
##    print()
##
##for row in matrix:
##    for i in range(4):
##        print(row[i])
##    print()
##
##for row in matrix:
##    print(row)


##L = [ ('Ted', 23), ('Lee', 18), ('Sam', 22), ('Bob', 30), ('Dev', 27), ('Ray', 25) ]
##L2 = [ name  for name, bmi in L  if 20 < bmi < 26]
##print (L2)



##L = [[1, 2, 3, 4], [5, 6, 7, 8, 9], [11, 12, 13, 14]]
##
####sumL = [ if i != 0 subL[i] + subL[i-1] else subL[0] for subL in L for i in len(subL)-1]
####print(sumL)
##
##sum_L = [ [ (0 if i == 0 else sublist[i - 1]) + sublist[i] for i in range(len(sublist))]  for sublist in L]
##print("1:-")
##print(sum_L)
##
##sum_L = [ [sublist[0] if i == 0 else  sublist[0] + sublist[i] for i in range(len(sublist))]  for sublist in L]
##print("2:-")
##print(sum_L)
####
##
##L = [['a', 'b', 'c'], ['d', 'e', 'f'], ['d', 'h', 'i']]
##sum_L = [ ch for ll in L for ch in ll]
##print(sum_L)



##
##cities = ['Dhaka', 'Khulna', 'Brazil', 'Japan', 'USA', 'Jamaica']
##f3 = {"-" + ch + "-" for city in cities for ch in city}
##print(f3)


##f3 = [c[:3] + " : " + str(len(c)) for c in cities]
##print(f3)
##
##f3 = [ ch in c for c in cities]
##print(f3)


##numbers = [2, 4, 5, 6, -2, -4, -6, 3, 4, -2, 0, 1, -7]
##copy_n = numbers[:]
##for number in copy_n:
##    if number < 0:
##        numbers.remove(number)
##        print('removed number: ', number)
##
##print('after remove: ', )
##print(copy_n)
##print(numbers)


##students=['a', 'b', 'c', 'd']
##failed_students = ['a', 'c']
##
##for student in students:
##    if student in failed_students:
##        students.remove(student)
##print(students)

##D = {'apple' : 210, "capple" : 70, 'brange' : 250, 'guava' : 80}
##
##def sortByFirst(item):
##    return item[1]
##
##for name, price in sorted(D.items(), key= sortByFirst, reverse=False):
##    print(name, price)



##numbers = [2, 1, 4, 1, 2, 5, 8, 6, 7]
##for number in sorted((numbers), reverse = False):
##    print(number)
##
##print('\n')
##
##for number in range(len((numbers))):
##    print(numbers[number])
##
##print('\n')

##for number in range(len(numbers), reverse = False):
##    print(number)

##print('\n')
##
##print(len.__doc__)
##help(len)
##dir(range)

##
##numbers = [2, 1, 4, 5, 8, 6, 7]
##
##for number in numbers:
##    print(number, end = ' ')
##    
##print('\nsorted : ' + str(list(sorted(numbers))))
##print('\nreversed: ' + str(list(reversed(numbers))))
##
##print('\nin sorted list:')
##for number in sorted(numbers):
##    print(number, end = ' ')

##i = 10
##while i < 100:
##    print(i)
##    i += 1
####    if(i > 55):
####        break
##    
##else:
##    print('break naturally')


### Using curly braces {}
##my_set = {1, 2, 3, 4, 5}
##print(my_set)  # Output: {1, 2, 3, 4, 5}
##
### Using set() constructor
##another_set = set([1, 2, 3, 3, 4, 5])  # Converts list to set
##print(another_set)  # Output: {1, 2, 3, 4, 5}
##
### Empty set (IMPORTANT!)
##empty_set = set([1])  # Correct way
##wrong_set = {}     # This is an empty dictionary!
##print(empty_set, wrong_set)


##lst = [1, 2, 3, "hello"]
##print(lst['2'])
##
##
##tpl = (1, 2, 3)
##print(tpl['1'])

##students_list = [
####    1:
##    {
##        'id': 105416,
##        'name': 'John',
##        'gender': 'M',
##        'city': 'Paris',
##        'age': 21,
##        'marks': {'Maths': 89, 'Physics': 78, 'Chemistry': 91},
##        'is_sporty': True
##    },
####    2:
##    {
##        'id': 144547,
##        'name': 'Dev',
##        'gender': 'M',
##        'city': 'London',
##        'age': 23,
##        'marks': {'Maths': 88, 'Physics': 77, 'Chemistry': 98},
##        'is_sporty': False
##    },
####    3:
##    {
##        'id': 132399,
##        'name': 'Mary',
##        'gender': 'F',
##        'city': 'Paris',
##        'age': 22,
##        'marks': {'Maths': 99, 'Physics': 87, 'Chemistry': 88},
##        'is_sporty': True
##    }
##]
##import pprint
##
##for student in students_list:
##    total = 0
##    pprint.pprint(student)
##    for mark in student['marks'].values():
##        total += mark
##    student['total'] = total
##
##pprint.pprint(students_list)

# Print the list
##for student in students_list:
##    print(student)




##x, y = 0, 1
##for i in range(1000):
##    print(f'{x}')
##    x, y = y, x+y



##import sys
##import time
##from collections import defaultdict
##
##def count_words(files):
##    word_count = defaultdict(int)
##    
##    for file in files:
##        try:
##            with open(file, 'r', encoding='utf-8') as f:
##                for line in f:
##                    words = line.strip().split()
##                    for word in words:
##                        word_count[word] += 1
##        except FileNotFoundError:
##            print(f"Error: File '{file}' not found.")
##        except Exception as e:
##            print(f"Error reading '{file}': {e}")
##    
##    return word_count
##
##if __name__ == "__main__":
##    if len(sys.argv) < 2:
##        print("Usage: python <script.py> <file1> <file2> ... <fileN>")
##        sys.exit(1)
##    
##    start_time = time.time()
##    files = sys.argv[1:]
##    word_counts = count_words(files)
##    end_time = time.time()
##    
##    print(word_counts)
##    print(f"Execution time: {end_time - start_time:.4f} seconds")

##n = int(input('Enter a number to print factorial: '))
##factorial = 1
##for i in range(2, n+1):
##    factorial *= i
##    print(factorial)
##print(f'The factorial of {n} is {factorial}')

##total = 0
##for i in range(5, 20, 2):
##    total += i*i
##    print(i, ' > ', i*i) 
##print(f'the sum of all square {total}')
##

##matrix = [
##    [1, 2, 3],
##    [1, 2, 3],
##    [1, 2, 3],
##    [1, 2, 3],
##    ]
##for i in range(len(matrix)):
##    for j in range(len(matrix[0])):
##        print(matrix[i][j], end=' ' )
##    print()


##n = 3
##for i in range(1, 11):
##    print(f'{n} X {i:2} = {n*i:30}')


##import time
##
##x, y, i = 1, 1, 1
##
##start_time = time.time()  # Start timer
##
##while x <= 10261062362033262336604926729245222132668558120602124277764622905699407982546711488272859468887457959087733119242564077850743657661180827326798539177758919828135114407499369796465649524266755391104990099120377:
##    i += 1
##    print(i, ' > ', x)
##    x, y = y, x + y
##
##end_time = time.time()  # End timer
##
##execution_time = end_time - start_time
##print(f"\nExecution Time: {execution_time:.6f} seconds")
##

##import time
##
##x, y, i = 1, 1, 1
##
##start_time = time.time()  # Start timer
##
##for i in range(1000):
##    i += 1
####    print(i, ' > ', x)
##    x, y = y, x + y
##
##end_time = time.time()  # End timer
##
##execution_time = end_time - start_time
##print(f"\nExecution Time: {execution_time:.6f} seconds")


##for i in range(5, 25, 5):
##    print(i * i, ' < ', i)


##import collections
##
##Card = collections.namedtuple('Card', ['rank', 'suit'])
##class FrenchDeck:
##    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
##    suits = 'spades diamonds clubs hearts'.split()
##    def __init__(self):
##        self._cards = [Card(rank, suit) for suit in self.suits
##                                        for rank in self.ranks]
##    def __len__(self):
##        return len(self._cards)
##    def __getitem__(self, position):
##        return self._cards[position]
##
##cards = FrenchDeck()
##print(cards.__len__())
##
##i = 0 
##for card in cards:
##    i += 1
##    print(f"{i} : {card.suit} → {card.rank}")
    
##for i in range(1, 6):
##        print((' ' * (int((6-i)/2))) + '*' * i)

##for i in range(999, 5, -2):
##    print(i, ' -> ', i * i, end = '\n')



##L = [('name 1', 20), ('name 2', 21), ('name 3', 22), ('name 4', 23)]
##D = dict(L)
##
##for key, value in D.items():
##    print(key, value)



##L = [('name 1', 20), ('name 2', 21), ('name 3', 22), ('name 4', 23)]
##
##for _, age in L:
####    name, age = t
##    print('name: ' + 'name' + ', age: ' + str(age))


##for item in dir(str):
##    print(item)


##fruit_price = {'apple': 210, 'banana': 700, 'Mango': '1000', 'Papaya': '700'}
##
##for fruit in fruit_price:
##    print(fruit + " " + str(fruit_price[fruit]), end = ", ")
##
##print('Here is all the keys:')
##for friut in fruit_price.keys():
##    print(friut)
##
##print('Here is all the Values:')
##for friut in fruit_price.values():
##    print(friut)
##
##print('Here is all the tuples:')
##for friut in fruit_price.items():
##    print(friut)
##
##print('Here is all the seperate:')
##for friut, price in fruit_price.items():
##    print(f'Price of {friut} is {price}')



##fruit_price = {
##    'apple' : 210,
##    'banana' : 700
##    }
##
##done = False
##
##while not done:
##    fruit_name = input('Enter the fruit name: ')
##    fruit_price_unit = input('Enter price: ')
##    fruit_price[fruit_name] = fruit_price_unit
##    if input('Want to enter more: ') == 'n':
##        done = True
##print(fruit_price)




##name = input('Enter a title: ')
##
##if not name.istitle():
##    print('wrong input')
##else:
##    print(name)




##l = [1, 2, 3, 2, 4, 3, 2, 5, 2]
##
##n = 2
##
##while n in l:
##    l.remove(n)
##
##print(l)
