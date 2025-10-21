# tests.py — Unit testing using assert

from operations import *

# Reset
books.clear()
members.clear()

# Test add functions
add_book("123", "Book A", "Author A", "Fiction", 3)
assert "123" in books, "Book not added."

add_member(1, "John Doe", "john@example.com")
assert any(m["member_id"] == 1 for m in members), "Member not added."

# Test borrowing
borrow_book(1, "123")
assert "123" in members[0]["borrowed_books"], "Book not borrowed."

# Test returning
return_book(1, "123")
assert "123" not in members[0]["borrowed_books"], "Book not returned."

# Test updating
update_book("123", total_copies=5)
assert books["123"]["total_copies"] == 5, "Book not updated."

# Test deleting
delete_book("123")
assert "123" not in books, "Book not deleted."

print("✅ All tests passed successfully!")


