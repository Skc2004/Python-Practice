import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.widgets import Button, TextBox

class LibraryManagementSystem:
    def __init__(self, max_size):
        self.max_size = max_size
        self.data = [None] * max_size  # To store the book titles
        self.next = [-1] * max_size    # To store the index of the next book
        self.head = -1                # Head index of the linked list (books collection)
        self.free = 0                 # Points to the first free position (empty slot)

        # Initialize the free list
        for i in range(max_size - 1):
            self.next[i] = i + 1
        self.next[max_size - 1] = -1  # End of free list

    # Function to add a new book to the collection
    def add_book(self, title):
        if self.free == -1:
            print("No space available to add a new book.")
            return False
        
        # Get the first free node
        new_node_index = self.free
        # Update the free pointer to the next available node
        self.free = self.next[self.free]

        # Insert the new book title
        self.data[new_node_index] = title
        # Set the next of the new node to current head
        self.next[new_node_index] = self.head
        # Update the head to point to the new node
        self.head = new_node_index
        return True

    # Function to delete the first book (if necessary, can be modified to delete by title)
    def delete_book(self):
        if self.head == -1:
            print("Library is empty. No book to delete.")
            return False
        
        # Get the index of the current head node (first book)
        node_to_delete = self.head
        # Update head to the next node (next book)
        self.head = self.next[node_to_delete]
        # Add the deleted node back to the free list
        self.next[node_to_delete] = self.free
        self.free = node_to_delete
        self.data[node_to_delete] = None  # Clear the book title
        return True

    # Function to get the current state of the linked list
    def get_linked_list(self):
        books = []
        if self.head == -1:
            return books

        index = self.head
        while index != -1:
            books.append((self.data[index], index, self.next[index]))
            index = self.next[index]
        return books


class LinkedListVisualizer:
    def __init__(self, library_system):
        self.library = library_system
        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(left=0.3, bottom=0.4)
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 2)
        self.ax.axis('off')

        # Add UI components (buttons, text box)
        self.add_text_box = TextBox(plt.axes([0.05, 0.8, 0.2, 0.05]), "Add Book:")
        self.add_button = Button(plt.axes([0.05, 0.7, 0.2, 0.05]), "Add Book")
        self.delete_button = Button(plt.axes([0.05, 0.6, 0.2, 0.05]), "Delete Book")
        self.update_button = Button(plt.axes([0.05, 0.5, 0.2, 0.05]), "Update View")

        # Connect events to the buttons
        self.add_button.on_clicked(self.add_book)
        self.delete_button.on_clicked(self.delete_book)
        self.update_button.on_clicked(self.update_view)

        # Initial view
        self.update_view()

    def add_book(self, event):
        title = self.add_text_box.text
        if title:
            success = self.library.add_book(title)
            if not success:
                print("Failed to add book. No space available.")
            self.update_view()

    def delete_book(self, event):
        success = self.library.delete_book()
        if not success:
            print("Failed to delete book. No book available.")
        self.update_view()

    def update_view(self, event=None):
        self.ax.clear()
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 2)
        self.ax.axis('off')

        books = self.library.get_linked_list()
        x_start = 1

        for book, idx, next_idx in books:
            # Create a rectangle for each node
            self.ax.add_patch(FancyBboxPatch((x_start, 1), 2, 0.8,
                                             boxstyle="round,pad=0.3", edgecolor='black', facecolor='lightblue'))
            self.ax.text(x_start + 1, 1.4, f"{book}", ha="center", va="center")

            # Draw an arrow for the next pointer
            if next_idx != -1:
                self.ax.arrow(x_start + 2.2, 1.4, 0.8, 0, head_width=0.2, head_length=0.2, fc='black', ec='black')

            x_start += 3

        self.fig.canvas.draw_idle()


# Main interactive function
def main():
    max_size = 5
    library_system = LibraryManagementSystem(max_size)
    visualizer = LinkedListVisualizer(library_system)
    plt.show()

# Run the application
main()
