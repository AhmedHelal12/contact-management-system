# Contact Management System (CLI Application)

This is a simple **Command-Line Interface (CLI)** application for managing a contact database. Built using Python and SQLite, it allows users to perform CRUD operations (Create, Read, Update, Delete) on contacts efficiently. The application includes robust validation and features a user-friendly command-line interface for seamless interaction.

---

## Features

1. **Add Contacts**:
   - Add a new contact with a name, phone number, email, and category.
   - Validates inputs to ensure data integrity (e.g., email format, phone number length).

2. **View Contacts**:
   - View all saved contacts.
   - Filter contacts by category.

3. **Search Contacts**:
   - Search contacts by name using partial matching.

4. **Update Contacts**:
   - Edit contact details using the contact ID.

5. **Delete Contacts**:
   - Delete a specific contact by its ID.
   - Reset the entire contact database with a confirmation flag.

6. **Data Persistence**:
   - All contacts are stored in an SQLite database (`contact.db`), ensuring data is retained between sessions.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/AhmedHelal12/contact-management-system.git
   
