class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #İki düğüm arasındaki keşisen degeri bulur
    def intersection(self, headA, headB):
        first = headA
        second = headB
        while first.data != second.data:
            first = first.next if first is not None else headB
            second = second.next if second is not None else headA
        return first
    
    #Tüm düğümü döndürür
    def all(self):
        if self.head is None:
            return self.head   
        root = self.head
        while root:
            print(root.data)
            root = root.next 
    
    #Kaç adet düğüm var count ile sayar
    def count_node(self):
        root = self.head
        count = 0
        if self.head is None:
            return count    
        while root:
            root = root.next         
            count = count + 1
        return count

    #Düğümdeki en büyük değeri bulur
    def get_max(self):
        Max = self.head.data
        root = self.head 
        for i in range(0, self.count_node()):
             if root.data > Max:
                   Max = root.data
             root = root.next    
        return Max 
    
   #Düğümdeki en küçük değeri bulur
    def get_min(self):
        Min = self.head.data 
        root = self.head 
        for i in range(0, self.count_node()):
             if root.data < Min:
                   Min = root.data
             root = root.next    
        return Min 


# Node ve LinkedList sınıflarını kullanarak örnekler oluşturuyoruz
headA1 = Node(30)
headA2 = Node(25)
headA3 = Node(12)
headA4 = Node(9)
headA5 = Node(8)

headB1 = Node(11)
headB2 = Node(14)
headB3 = Node(8)
headB4 = Node(6)

l1 = LinkedList()  # LinkedList sınıfından bir örnek oluşturuyoruz
l2 = LinkedList()  # Başka bir LinkedList örneği oluşturuyoruz

l1.head = headA1
l2.head = headB1
                   
headB1.next = headB2 #b1->b2->b3->b4 
headB2.next = headB3
headB3.next = headB4

headA1.next = headA2 #a1->a2->a3->a4->a5
headA2.next = headA3
headA3.next = headA4
headA4.next = headA5

#print(l1.intersection(headA1, headB1).data)
print(l1.count_node())
print(f"Max data {l1.get_max()}")
print(f"Min data {l1.get_min()}")

