items = []  

def insert(pos, elem) :   #O(n) 삽입하면 밀어서 ..
    items.insert(pos, elem)

def delete(pos) :  #O(n) 1번 삭제하면 앞으로 이동
    items.pop(pos)  

def getEntry(pos): return items[pos]

def isEmpty( ):
    return size() == 0
def size( ):   #리스트의 크기 반환
    return len(items)
def clear( ):   
    global items
    items = []      

def find(item) : return items.index(item)
def replace(pos, elem): items[pos] = elem
def sort() : items.sort()
def merge(lst) : items.extend(lst)

def display(msg='ArrayList:' ):  #디폴트 매개변수
    print(msg, size(), items) #items값은 파이썬의 리스트를 문자열로 출력
