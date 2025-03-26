import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, "w", encoding="utf-8", newline="") as f:
        columns = contacts[0].keys()
        writer = csv.DictWriter(f, delimiter=",", fieldnames=columns)
        writer.writeheader()
        for row in contacts:
            writer.writerow(row)
    
        
        
        
            

path = "contacts.csv"
def read_contacts_from_file(filename):
    with open(filename, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        contacts = []
        for row in reader:
            # Update 'favorite' field: convert 'False' to False, 'True' stays True
            if row['favorite'] == 'False':
                row['favorite'] = False
            else:
                row['favorite'] = True
            contacts.append(row)
        print(contacts)
        return contacts
read_contacts_from_file(path)