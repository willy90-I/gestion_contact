# contact.py
class Contact:
    def __init__(self, id, nom, prenom, telephone, email):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.email = email

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.telephone} ({self.email})"
