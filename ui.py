# ui.py
import tkinter as tk
from tkinter import messagebox
from database import add_contact, update_contact, delete_contact, get_all_contacts, search_contacts
from contact import Contact

def add_contact_ui(entry_nom, entry_prenom, entry_telephone, entry_email, listbox):
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    telephone = entry_telephone.get()
    email = entry_email.get()

    if nom and prenom and telephone:
        contact = Contact(None, nom, prenom, telephone, email)
        add_contact(contact)
        messagebox.showinfo("Succès", "Contact ajouté avec succès")
        display_contacts_ui(listbox)  # Passe 'listbox' comme argument ici
    else:
        messagebox.showerror("Erreur", "Nom, prénom et téléphone sont obligatoires")

def display_contacts_ui(listbox):
    listbox.delete(0, tk.END)
    contacts = get_all_contacts()
    for contact in contacts:
        listbox.insert(tk.END, f"{contact.nom} {contact.prenom} - {contact.telephone} ({contact.email})")

def search_contacts_ui(entry_search, listbox):
    query = entry_search.get()
    contacts = search_contacts(query)
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact.nom} {contact.prenom} - {contact.telephone} ({contact.email})")

def delete_contact_ui(listbox):
    try:
        selected_contact = listbox.curselection()[0]
        contact_info = listbox.get(selected_contact)
        contact_id = int(contact_info.split(" ")[0].split(":")[1].strip())
        delete_contact(contact_id)
        messagebox.showinfo("Succès", "Contact supprimé avec succès")
        display_contacts_ui(listbox)
    except IndexError:
        messagebox.showerror("Erreur", "Veuillez sélectionner un contact à supprimer")
