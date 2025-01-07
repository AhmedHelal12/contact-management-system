from argparse import ArgumentParser
from ContactController import ContactController
controller = ContactController()
def main():
    parser = ArgumentParser(description="CLI Contact Mangement System Applicatioin ")
    subparsers = parser.add_subparsers(description="Add, Edit, Delete, and search contacts")

    add_parser = subparsers.add_parser("add",help="Add Name, phone number, email, category")
    add_parser.add_argument("name",type=str,help="Add the name of the contact")
    add_parser.add_argument('-no',"--number",type=int,help="Add the number of the contact")
    add_parser.add_argument('-em',"--email",type=str,help="Add the email of the contact")
    add_parser.add_argument('-cat',"--category",type=str,help="Add the category of the contact")
    add_parser.set_defaults(func = controller.add_contact)

    view_parser = subparsers.add_parser("view",help="view all contacts")
    view_parser.add_argument("-a","--all",action="store_true",help="View all contacts")
    view_parser.add_argument("-cat","--category",type=str,help="View contacts by category")
    view_parser.set_defaults(func=controller.view_contacts)

    edit_parser = subparsers.add_parser("edit",help="Edit Name, phone number, email, category")
    edit_parser.add_argument("contact",type=int,help="the id of the contact")
    edit_parser.add_argument("name",type=str,help="Add the name of the contact")
    edit_parser.add_argument('-no',"--number",type=int,help="Add the number of the contact")
    edit_parser.add_argument('-em',"--email",type=str,help="Add the email of the contact")
    edit_parser.add_argument('-cat',"--category",type=str,help="Add the category of the contact")
    edit_parser.set_defaults(func = controller.update_contact)

    search_parser = subparsers.add_parser("search",help="Looking for a contact")
    search_parser.add_argument("name",help="Search using the name")
    search_parser.set_defaults(func = controller.search_contacts)

    delete_parser = subparsers.add_parser("delete",help="Looking for a contact")
    delete_parser.add_argument("--cont",type=int,help="Delete using id")
    delete_parser.set_defaults(func = controller.delete_contact)

    reset_parser = subparsers.add_parser("reset",description="Delete all contacts")
    reset_parser.add_argument("--confirm",action="store_true",help="delete all")
    reset_parser.set_defaults(func = controller.reset)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
    controller.close_connection()
    

