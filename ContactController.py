import sqlite3
import re


class Contact:
    def __init__(self,name,number=None,email=None,category=None):
        self.name = name
        self.number = number
        self.email = email
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.number}, {self.email}, {self.category}"
    
class ContactController():
    def __init__(self):
        self.conn = sqlite3.connect('contact.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            '''
                CREATE TABLE IF NOT EXISTS contact(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    number INTEGER,
                    email TEXT UNIQUE,
                    category TEXT
                )
            ''')
        self.conn.commit()
    
    def close_connection(self):
        self.conn.commit()
        self.conn.close()
        
    def add_contact(self,args):

        name = args.name
        number = args.number
        email = args.email
        category = args.category

        try:
            validated_name,validated_number,validated_email,validated_category = self.validate_contact(name,number,email,category)
            if validated_name and validated_number  and validated_email  and validated_category:
                self.cursor.execute('''
                    INSERT INTO contact(name,number,email,category) values(?,?,?,?)
                ''',(name,number,email,category))
                print("The contact was added successfully!")
        except Exception as e:
            print(f"Error: {e}")
        
    
    def update_contact(self, args):
        contact_number = args.contact
        name = args.name
        number = args.number
        email = args.email
        category = args.category

        try:
            # Validate the inputs
            validated_name, validated_number, validated_email, validated_category = self.validate_contact(
                name, number, email, category
            )

            # Check if the contact exists
            self.cursor.execute("SELECT id FROM contact WHERE id = ?", (contact_number,))
            contact = self.cursor.fetchone()

            if not contact:
                print(f"No contact found with ID {contact_number}. Update operation aborted.")
                return

            # Perform the update if validation passes and contact exists
            self.cursor.execute(
                '''
                UPDATE contact 
                SET name = ?, number = ?, email = ?, category = ? 
                WHERE id = ?
                ''',
                (name, number, email, category, contact_number)
            )
            self.conn.commit()
            print("Contact updated successfully.")

        except Exception as e:
            print(f"Error: {e}")

    
    def view_contacts(self,args):
        all_contacts=[]
        category = args.category
        all_arg = args.all
        try:
            if all_arg and isinstance(all_arg,int):
                self.cursor.execute(
                    ''' SELECT * FROM contact
                        ''')
                all_contacts = self.cursor.fetchall()

            if category :
                self.cursor.execute(
                    ''' SELECT * FROM contact where category = ?
                        ''',(category,))
                all_contacts = self.cursor.fetchall()

        except Exception as e:
            print(f"Error: {e}")

        self.print_contacts(all_contacts)


    def search_contacts(self,args):
        name = args.name + '%'
        if isinstance(name,str) and name is not None:
            try:
                self.cursor.execute(
                    ''' SELECT * FROM contact WHERE name LIKE ?
                        ''',(name,))   

                results = self.cursor.fetchall()   
                self.print_contacts(results)
            
            except Exception as e:
                print(f"Error: {e}")


    def delete_contact(self,args):
        id = args.cont
        if isinstance(id,int):
            try:
                self.cursor.execute('''DELETE FROM contact where id = ?''',(id,))
                print("The contact was deleted successfully")
            except Exception as e:
                print(f"Error: {e}")

    def reset(self,args):
        try:
            if args.confirm:
                self.cursor.execute("Delete from contact")
                print("All contacts were deleted successfully!")
            else:
                raise Exception("you should type --confirm to reset")
        except Exception as e:
            print(f"Error: {e}")


    def validate_name(self,name):
        if not isinstance(name, str) or len(name) < 2:
            raise ValueError("Enter a valid name. name must be string and not less that two characters!")
        else:
            return name
             
        
    def validate_number(self,number):
        if number:
            print(number)
            matched = re.match(r'^\d{10}$',str(number).strip())
            if matched:
                return number
            else:
                raise ValueError("Enter a valid number, the length of the number is 10 digits")
            
        else:
            return True
        
    def validate_email(self,email):
        if email:
            matched = re.match(r'^[a-zA-Z0-9]+([-._+%]?[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$',str(email))
            if matched:
                return matched
            else:
                raise ValueError("Enter a valid email address!")
        else:
            return True
        


    def validate_category(self,category):
        if category and len(category) >= 2:
            return category
        if not category:
            return True
        else:
            raise ValueError ("Please enter a valid category, not a number or not less that two characters")
    
    def validate_contact(self,name,number,email,category):
        validated_name = self.validate_name(name)
        validated_number = self.validate_number(number)
        validated_email = self.validate_email(email)
        validated_category = self.validate_category(category)

        return [validated_name,validated_number,validated_email,validated_category]
    
    def print_contacts(self,results):
        if len(results):
            for x in results:
                print(x)
        else:
            print("No contacts to show")



        