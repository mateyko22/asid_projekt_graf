from typing import Any


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.head is None:
            return 'Pusto'
        tekst = ""
        pom = self.head
        while pom is not None:
            tekst += str(pom.data)
            pom = pom.next
            if pom is not None:
                tekst += " -> "
        return tekst

    def __len__(self):
        if self.head is None:
            return 0
        pom = self.head
        licznik = 0
        while pom is not None:
            pom = pom.next
            licznik += 1
        return licznik

    def push(self, value: Any) -> None:
        nowa_w = Node(value)
        nowa_w.next = self.head
        self.head = nowa_w

    def append(self, value: Any) -> None:
        nowa_w = Node(value)
        if self.head is None:
            self.head = nowa_w
            return
        pom = self.head
        while pom.next:
            pom = pom.next
        pom.next = nowa_w

    def node(self, at: int) -> None:
        wuwu = self.head
        for i in range(at):
            wuwu = wuwu.next
        return wuwu

    def insert(self, value: Any, after: Node) -> None:
        nowa_w = Node(value)
        nowa_w.next = after.next
        after.next = nowa_w

    def pop(self) -> Any:
        pom = self.head
        self.head = pom.next
        return pom.data

    def remove_last(self) -> Any:
        pom = self.head
        while pom.next.next is not None:
            pom = pom.next
        pom2 = pom.next.data
        pom.next = None
        return pom2

    def remove(self, after: Node) -> Any:
        if after.next is None:
            print("Wskazany wezel nie znajduje sie w liscie.")
            return
        else:
            after.next = after.next.next


class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0
        self._storage: LinkedList = LinkedList()

    def __len__(self):
        return self.size

    def __str__(self):
        tekst = ""
        pom = self.head.next
        while pom is not None:
            tekst += str(pom.data)
            pom = pom.next
            if pom is not None:
                tekst += " \n"
        return tekst

    def push(self, element: Any) -> None:
        nowa_w = Node(element)
        nowa_w.next = self.head.next
        self.head.next = nowa_w
        self.size += 1

    def pop(self) -> Any:
        usun = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return usun.data


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._storage = LinkedList()
        self.size = 0

    def __str__(self):
        if self.head is None:
            return 'Pusto'
        tekst = ""
        pom = self.head
        while pom is not None:
            tekst += str(pom.data)
            pom = pom.next
            if pom is not None:
                tekst += " -> "
        return tekst

    def __len__(self):
        return self.size

    def peek(self) -> Any:
        return self.head.data

    def enqueue(self, element: Any) -> None:
        pom = Node(element)
        if self.tail is None:
            self.head = pom
            self.tail = self.head
        else:
            self.tail.next = pom
            self.tail = self.tail.next
        self.size += 1

    def dequeue(self) -> Any:
        if self.head is None:
            return None
        pom = self.head
        self.head = self.head.next
        return pom
