# operations.py — Core logic for Library Management System

books = {}
members = []
genres = ("Fiction", "Non-Fiction", "Sci-Fi", "Thriller", "Romance", "Biography")

def add_book(isbn, title, author, genre, total_copies):
    if isbn in books:
        print("Book already exists.")
        return
    if genre not in genres:
        print("Invalid genre. Please choose from:", genres)
        return
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies,
        "borrowed": 0
    }
    print(f"Book '{title}' added successfully.")

def add_member(member_id, name, email):
    if any(m["member_id"] == member_id for m in members):
        print("Member already exists.")
        return
    members.append({
        "member_id": member_id,
        "name": name,
        "email": email,
        "borrowed_books": []
    })
    print(f"Member '{name}' added successfully.")

def borrow_book(member_id, isbn):
    member = next((m for m in members if m["member_id"] == member_id), None)
    if not member:
        print("Invalid member ID.")
        return
    if isbn not in books:
        print("Book not found.")
        return
    if books[isbn]["borrowed"] >= books[isbn]["total_copies"]:
        print("No copies available.")
        return
    if isbn in member["borrowed_books"]:
        print("Member already borrowed this book.")
        return

    member["borrowed_books"].append(isbn)
    books[isbn]["borrowed"] += 1
    print(f"Book '{books[isbn]['title']}' borrowed by {member['name']}.")

def return_book(member_id, isbn):
    """
    Return a borrowed book to the library.
    Checks that the member and book exist and the member has actually borrowed it.
    """
    member = next((m for m in members if m["member_id"] == member_id), None)
    if not member:
        print("Invalid member ID.")
        return
    if isbn not in books:
        print("Book not found.")
        return
    if isbn not in member["borrowed_books"]:
        print("Book not borrowed by this member.")
        return

    member["borrowed_books"].remove(isbn)
    books[isbn]["borrowed"] = max(books[isbn]["borrowed"] - 1, 0)
    print(f"Book '{books[isbn]['title']}' returned by {member['name']} successfully.")

def update_book(isbn, **kwargs):
    if isbn in books:
        books[isbn].update(kwargs)
        print(f"Book '{isbn}' updated successfully.")
    else:
        print("Book not found.")

def update_member(member_id, **kwargs):
    for m in members:
        if m["member_id"] == member_id:
            m.update(kwargs)
            print(f"Member '{member_id}' updated successfully.")
            return
    print("Member not found.")

def delete_book(isbn):
    if isbn in books:
        del books[isbn]
        print(f"Book '{isbn}' deleted successfully.")
    else:
        print("Book not found.")

def delete_member(member_id):
    global members
    before_count = len(members)
    members = [m for m in members if m["member_id"] != member_id]
    if len(members) < before_count:
        print(f"Member '{member_id}' deleted successfully.")
    else:
        print("Member not found.")
