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

## Usage

Run the application with the desired command and arguments. Below are examples of how to use the available commands:

### Add a Contact

```bash
python app.py add "John Doe" --number 1234567890 --email john@example.com --category Friend
```
### View all contacts
```bash
python app.py view --all
```
### View Contacts by Category
```bash
python3 app.py view -cat family
```
### Search by name
```bash
python app.py search Ahmed
```
### Update contact
```bash
python app.py edit 1 "John Smith" --number 0987654321 --email johnsmith@example.com --category Work
```
### Delete a contact
```bash
python app.py delete --cont 1
```
### Reset the database
```bash
python app.py reset --confirm
```






   
