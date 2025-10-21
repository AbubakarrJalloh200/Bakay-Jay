# demo.py — Demonstrates how the system works

from operations import *

print("===== LIBRARY SYSTEM DEMO =====")

# Add books
add_book("111", "1984", "George Orwell", "Fiction", 3)
add_book("222", "The Martian", "Andy Weir", "Sci-Fi", 2)

# Add members
add_member(1, "Alice", "alice@example.com")
add_member(2, "Bob", "bob@example.com")

# Borrow & Return
print("\n--- Borrowing Books ---")
borrow_book(1, "111")
borrow_book(1, "222")

print("\n--- Returning Book ---")
return_book(1, "111")

# Update info
print("\n--- Updating Info ---")
update_book("222", total_copies=5)
update_member(2, email="bob.new@example.com")

# Delete
print("\n--- Deleting ---")
delete_book("111")
delete_member(2)

print("\n--- Final Data ---")
print("Books:", books)
print("Members:", members)

