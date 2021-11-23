class Node:

    def __init__(self,data, next = None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head =None
    

    def print(self):

        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next

        print(llstr)
        
    def insert_at_first(self,data):
        first = Node(data, self.head)
        self.head = first


    def insert_at_last(self,data):

        last = Node(data)

        if self.head is None:
            self.head = last
            return
        
        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        last_node.next = last

    def insert_at(self,data,idx):

        count = 0

        if idx ==0:
            self.insert_at_first(data)
            return

        new_node = self.head
        while new_node:

            if count == idx-1:
                new = Node(data,new_node.next)
                new_node.next = new
                break
            new_node = new_node.next
            count += 1

    def delete_at (self,idx):

        if idx ==0:
            return ('ll is empty')

        count = 0
        itr = self.head
        while itr:
            if count == idx-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def length(self):
        count =0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_after_value(self,value,data1):

        

        loop = self.head
        while loop :
            if loop.next.data == value:
                new = Node(data1,loop.next)
                loop.next = new
                break
            loop = loop.next

    def remove_at_value(self,value):

        itr = self.head
        while itr:
            if itr.data == value:
                itr.next = itr.next.next
                break
            itr = itr.next

    def check(self,value):

        if self.head is None:
            return False

        itr = self.head
        while itr:
            if itr.data == value:
                return True
            itr = itr.next
        return False

    def kth(self,k):

        count = 1
        itr = self.head
        while itr.next :
            count += 1
            itr = itr.next

        value = count-k-1
        itr = self.head
        for i in range(count):
            if i == value:
                return itr.data
            itr = itr.next
    
    def reverse(self):

        prev = None
        itr = self.head
        while itr:
            nxt = itr.next
            itr.next = prev
            prev = itr
            itr = nxt
        self.head = prev
    
    def palindrome(self):
        list = []

        itr = self.head
        while itr :
            list.append(itr.data)
            itr = itr.next

        left = 0
        right = len(list)-1

        while left < right:
            if list[left] != list[right]:
                return False
            left += 1
            right -= 1
        return True



            


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_first(1)
    ll.insert_at_first(2)
    ll.insert_at_first(0)
    ll.insert_at_first(2)
    ll.insert_at_first(7)
    # ll.insert_at("99",2)
    # ll.delete_at(2)
    # print(ll.length())
    # ll.insert_after_value(2, "khaled")
    # ll.remove_at_value(2)
    # ll.reverse()
    ll.print()
    print(ll.palindrome())
    # print(ll.check(7))




