class ArrayList:
    def __init__(self):
        self.items = []  

    def insert(self,pos, elem) :   #O(n) 삽입하면 밀어서 ..
        self.items.insert(pos, elem)

    def delete(self,pos) :  #O(n) 1번 삭제하면 앞으로 이동
        self.items.pop(pos)  

    def getEntry(self,pos): return self.items[pos]

    def isEmpty(self):
        return self.size() == 0
        #if len(items) == 0 :
            #return True
        #else :
           # return False

    #def isEmpty( ): return len(items) == 0

    def size(self):   #리스트의 크기 반환
        return len(self.items)
    def clear(self):   
        global items
        self.items = []      

    def find(self,item) : return self.items.index(item)
    def replace(self, pos, elem): self.items[pos] = elem
    def sort(self) : self.items.sort()
    def merge(self,lst) : self.items.extend(lst)

    def display(self,msg='ArrayList:' ):  #디폴트 매개변수
        print(msg, self.size(), self.items) #items값은 파이썬의 리스트를 문자열로 출력
