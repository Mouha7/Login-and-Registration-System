import re
import csv
import os
import time
import getpass
import bcrypt

class User:
    def __init__(self, email, password):
        self._email = email
        self._password = password
        self._state = False
    
    def check_email(self) -> str:
        """
        Fonction qui vérifie la présence de l'arobase et de point.
        """
        while True:
            cpt = 0
            email = input("E-mail : ")
            if email.find("@") == -1 or email.find('.') == -1:
                print("Erreur, un E-mail doit comporter un '@' et un '.'.")
                continue
            elif email.startswith("@") or email.startswith('.'):
                print("Erreur, un E-mail ne commence pas par un '@' ou un '.'.")
                continue
            elif email.endswith("@") or email.endswith('.'):
                print("Erreur, un E-mail ne termine pas par un '@' ou un '.'.")
                continue
            else:
                for i in email:
                    if '@' == i:
                        cpt += 1
                if cpt > 1:
                    print("Erreur, un E-mail doit comporter qu'un seul '@'.")
                    continue
            return email
    
    def check_password(self, message: str) -> str:
        """
        Pour vérifier si un mot de passe contient au minimum un chiffre et 
        qu'il ne soit pas inférieur à 4 caractères.
        """
        while True:
            password = getpass.getpass(message)
            regex_chiffre = re.compile(r'\d')
            if len(password) < 4:
                print("Erreur, le mot de passe doit être minimum supérieur à 4 caractères.")
                continue
            elif password[0].capitalize() != password[0]:
                print("Erreur, le mot de passe doit commencer par une lettre majuscule.")
                continue
            elif password.isdigit():
                print("Erreur, le mot de passe ne doit pas contenir que des chiffres.")
                continue
            elif not bool(regex_chiffre.search(password)):
                print("Erreur, le mot de passe doit contenir au moins un chiffre.")
                continue
            return password
    
    def clear(self):
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

class SignUp(User):
    def __init__(self, name, lastname, email, password, confirm_password):
        super().__init__(email, password)
        self._name = name
        self._lastname = lastname
        self._confirm_password = confirm_password
    
    def inscription(self):
        """
        L'inscription d'un utilisateur dans le système en POO
        """
        name = input("Nom : ").capitalize()
        lastname = input("Prénom : ").capitalize()
        email = self.check_email()
        while True:
            password = self.check_password("Password : ")
            confirm_password = self.check_password("Confirmer le mot de passe : ")
            if password == confirm_password:
                break
            else:
                print("Les deux mots de passe ne correspondent pas.")
        self._name = name.strip().capitalize()
        self._lastname = lastname.strip().capitalize()
        self._email = email
        self._password = password
        self._confirm_password = confirm_password
        self._state = True
    
    def save(self):
        """
        Ajouter les utilisateurs inscrivent dans un fichier csv appeler 'db_users.csv'
        """
        hashed_password = bcrypt.hashpw(self._password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        row_titles = ["Nom", "Prénom", "E-mail", "Password", "Status"]
        row_data = [self._name, self._lastname, self._email, hashed_password, self._state]
        with open('db_users.csv', 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            if f.tell() == 0:
                writer.writerow(row_titles)
            writer.writerow(row_data)
        print("Ajouté avec succès.")
        self.clear()

class SignIn(User):
    def __init__(self, email, password):
        super().__init__(email, password)
    
    def connexion(self, users):
        email = self.check_email()
        password = getpass.getpass("Saisie votre mot de passe : ")
        for user in users:
            if user['E-mail'] == email and bcrypt.checkpw(password.encode('utf-8'), user['Password'].encode('utf-8')):
                print(f"Bienvenu(e) sur votre compte {user['Prénom']} {user['Nom']}.")
                return
        print("Erreur, E-mail ou mot de passe incorrect.")
    
    def update_db(self):
        users = []
        with open('db_users.csv', 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                users.append(row)
        return users
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Bienvenue sur Login and Registration System")
    while True:
        print("1. Inscription")
        print("2. Connexion")
        print("3. Quitter")
        choix = input("Faites votre choix : ")
        if choix.isdigit() and 1 <= int(choix) <= 3:
            if choix == '1':
                u = SignUp("", "", "", "", "")  # Les arguments vides seront saisis par l'utilisateur
                u.inscription()
                u.save()
            elif choix == '2':
                c = SignIn("", "")
                users = c.update_db()
                c.connexion(users)
                c.clear()
            else:
                print("Au revoir...")
                break
        else:
            print("Erreur, veuillez faire un bon choix.")

if __name__ == '__main__':
    main()
