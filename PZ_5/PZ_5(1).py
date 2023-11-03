# Составить функцию, которая напечатает сорок любых символов.
import random


def forty_characters():
    count = 0
    lst = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';',
           '[', ']', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '?', '1', '2', '3', '4', '5', '6', '7', ]

    for i in range(40):
        count += 1
        print(f"{count}: {random.choice(lst)}")


forty_characters()
