# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self, name):
        self.name = name
        self.next = None


# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, name):
        new_node = Node(name)

        if self.head is None:
            self.head = new_node
            return f'{name} added to the end of the waitlist'

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        return f'{name} added to the end of the waitlist'

    def remove(self, name):
        current = self.head
        previous = None

        while current is not None:
            if current.name == name:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                return f'Removed {name} from the waitlist'

            previous = current
            current = current.next

        return f'{name} not found'

    def print_list(self):
        if self.head is None:
            print('The waitlist is empty')
            return

        current = self.head
        while current is not None:
            print(f'- {current.name}')
            current = current.next


def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            waitlist.add_front(name)
            

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            print(waitlist.add_end(name))

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            print(waitlist.remove(name))
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            waitlist.print_list()
            
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
waitlist_generator()

'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?

This linked list works by storing customer names in a node, 
so that each node contains the customer name stored and a pointer. 
The pointer will connect it to the next customer in the waiting list.
To add a new customer at the start of the list, it uses add_front.
To add a new customer at the end of the list, it uses add_end.
To remove a customer's name from the list, it uses remove.
To display the current waitlist, it uses print_list,
to go through each node and display it.

- What role does the head play?
The head is the first node or the first customer name stored in the linked list.
This is to give the program a starting point so it can read the rest of the list.
Every time a new customer is added to the front, the head is updated,
so that it now points to the new customer name added.

- When might a real engineer need a custom list like this?
To create a customer waiting list for a restaurant.
Almost all restaurants have some sort of waiting list system,
that keeps track of their customers waiting on a table to be seated.
As customers come in they get added,
those who are not present when called get removed,
or someone that had a reservation gets bumped to the front of the list.
'''
