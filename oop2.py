from abc import (
  ABC,
  abstractmethod,
)

import uuid

class Item():

    def __init__(self, name, value):
        self.name = name
        self.value = value


class Box(ABC):

    @abstractmethod
    def add(self, Item):
        ...

    @abstractmethod
    def add_many(self, Items):
        ...
    
    @abstractmethod
    def count(self):
        ...

    @abstractmethod
    def empty(self):
        ...

    @abstractmethod
    def get_items_as_array(self):
        ...

    @abstractmethod
    def print_items(self):
        ...

    


class ListBox(Box):

    def __init__(self):
        self.items = []

    def add(self, Item):
        self.items.append(Item)

    def add_many(self, Items):
        self.items = [*self.items, *Items]

    def count(self):
        return len(self.items)

    def empty(self):
        self.items = []

    def get_items_as_array(self):
        return self.items

    def print_items(self):
        print(f"\n--- {self.count()} Items in this box ---")
        for item in self.items:
            print(f"{item.name} | {item.value}")


class DictBox(Box):

    def __init__(self):
        self.items = {}

    def add(self, Item):
        id = uuid.uuid4()
        self.items[id] = Item

    def add_many(self, Items):
        for item in Items:
            id = uuid.uuid4()
            self.items[id] = item
    
    def count(self):
        return len(self.items)

    def empty(self):
        self.items = {}
    
    def get_items_as_array(self):
        return self.items.values()

    def print_items(self):
        print(f"\n--- {self.count()} Items in this box ---")
        for item in self.get_items_as_array():
            print(f"{item.name} | {item.value}")


def get_items(num_items=1, name_prefix='L', value_prefix='A'):
    items = []
    for i in range(num_items):
        items.append(Item(f"{name_prefix}-{i+1}", f"{value_prefix}-{i+1}"))
    return items

def create_many_list_or_dict_box(type = 'list',num_items=1, name_prefix='L', value_prefix='A'):
    box_list = ListBox() if type == 'list' else DictBox()
    identifier = 'ListBox' if type == 'list' else 'DictBox'
    print(f'\nCreating {identifier} {name_prefix}...')
    print(f"{identifier} {name_prefix} has {box_list.count()} Items")
    print(f'Adding {num_items} items to {identifier} {name_prefix}...')
    box_list.add_many(get_items(num_items=num_items, name_prefix=name_prefix, value_prefix=value_prefix))

    print(f"{identifier} {name_prefix} has {box_list.count()} Items")

    return box_list

def chunks(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

def repack_boxes(*args):
    if len(args) > 0:
        all_box_items = []
        for b in args:
            current_items = b.get_items_as_array()
            all_box_items = [*all_box_items, *current_items]

        chunky = list(chunks(all_box_items, len(args)))
        for index, box  in enumerate(args):
            box.empty()
            box.add_many(chunky[index])
            
    else:
        print('There are no lists to repack')

print("\n---Creating all the boxes---\n")

list_1 = create_many_list_or_dict_box('list', 20, 'List1', 'A')
list_1.print_items()
list_2 = create_many_list_or_dict_box('list', 9, 'List2', 'B')
list_2.print_items()
dict_1 = create_many_list_or_dict_box('dict', 5, 'Dict1', 'C')
dict_1.print_items()

print("\nRepacking all the boxes\n")

repack_boxes(list_1, list_2, dict_1)

print(f"List1 now has {list_1.count()} Items")
print(f"List2 now has {list_2.count()} Items")
print(f"Dict1 now has {dict_1.count()} Items")

list_1.print_items()
list_2.print_items()
dict_1.print_items()