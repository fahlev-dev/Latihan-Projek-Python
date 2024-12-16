from contacts.tui import ContactsApp
from contacts.database import Database

def main():
    app = ContactsApp(db=Database())
    app.run()
    
if __name__ == "__main__":
    main()