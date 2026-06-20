import json
import tkinter as tk

FILE = "contacts.json"


# ---------- LOAD DATA ----------
def load_contacts():
    try:
        file = open(FILE, "r")
        data = json.load(file)
        file.close()
        return data
    except:
        return []


# ---------- SAVE DATA ----------
def save_contacts(data):
    file = open(FILE, "w")
    json.dump(data, file, indent=4)
    file.close()


# ---------- SHOW CONTACTS ----------
def show_contacts(data=None):
    listbox.delete(0, tk.END)

    if data is None:
        data = load_contacts()

    i = 1
    for contact in data:
        text = str(i) + ". " + contact["name"] + " | " + contact["phone"] + " | " + contact["address"]
        listbox.insert(tk.END, text)
        i += 1

# ---------- ADD CONTACT ----------
def add_contact():
    name_value = name.get()
    phone_value = phone.get()
    address_value = address.get()

    if name_value == "" or phone_value == "" or address_value == "":
        status.set("Please fill all fields")
        return

    if not phone_value.isdigit() or len(phone_value) != 10:
        status.set("Phone must be 10 digits")
        return

    data = load_contacts()

    new_contact = {
        "name": name_value,
        "phone": phone_value,
        "address": address_value
    }

    data.append(new_contact)
    save_contacts(data)

    name.set("")
    phone.set("")
    address.set("")

    status.set("Contact added successfully")
    show_contacts()

# ---------- SEARCH CONTACT ----------
def search_contact():
    search_value = name.get().lower()

    data = load_contacts()
    result = []

    for contact in data:
        if search_value in contact["name"].lower():
            result.append(contact)

    if len(result) == 0:
        status.set("No contact found")
    else:
        status.set(str(len(result)) + " contact(s) found")

    show_contacts(result)

# ---------- DELETE CONTACT ----------
def delete_contact():
    try:
        selected_index = listbox.curselection()[0]
        data = load_contacts()

        del data[selected_index]

        save_contacts(data)
        status.set("Contact deleted")

        show_contacts()

    except:
        status.set("Please select a contact")

# ---------- GUI ----------
root = tk.Tk()
root.title("Simple Contact Book")
root.geometry("450x550")


name = tk.StringVar()
phone = tk.StringVar()
address = tk.StringVar()
status = tk.StringVar()

# INPUT FIELDS
tk.Label(root, text="Name").pack()
tk.Entry(root, textvariable=name).pack()

tk.Label(root, text="Phone (10 digits)").pack()
tk.Entry(root, textvariable=phone).pack()

tk.Label(root, text="Address").pack()
tk.Entry(root, textvariable=address).pack()

# BUTTONS
tk.Button(root, text="Add Contact", command=add_contact, bg="green", fg="white").pack(pady=2)
tk.Button(root, text="Search Contact", command=search_contact, bg="blue", fg="white").pack(pady=2)
tk.Button(root, text="Show All", command=show_contacts, bg="gray", fg="white").pack(pady=2)

# LIST BOX
listbox = tk.Listbox(root, width=60, height=18)
listbox.pack(pady=10)

# DELETE BUTTON
tk.Button(root, text="Delete Selected", command=delete_contact, bg="red", fg="white").pack()

# STATUS
tk.Label(root, textvariable=status, fg="darkblue").pack(pady=10)

# START
show_contacts()
root.mainloop()
