class GestionnaireTaches:
    def __init__(self):
        self.taches = []

    def ajouter_tache(self, tache):
        self.taches.append(tache)
        print(f"Tâche ajoutée : {tache}")

    def afficher_taches(self):
        if not self.taches:
            print("Aucune tâche pour le moment.")
        else:
            print("Liste des tâches:")
            for index, tache in enumerate(self.taches, start=1):
                print(f"{index}. {tache}")

    def marquer_complet(self, index):
        if 1 <= index <= len(self.taches):
            tache = self.taches[index - 1]
            print(f"Tâche '{tache}' marquée comme complète.")
            # Vous pourriez également mettre à jour une propriété de la tâche pour la marquer comme complète.
        else:
            print("Index de tâche invalide.")

    def supprimer_tache(self, index):
        if 1 <= index <= len(self.taches):
            tache = self.taches.pop(index - 1)
            print(f"Tâche '{tache}' supprimée.")
        else:
            print("Index de tâche invalide.")


# Utilisation du gestionnaire de tâches
gestionnaire = GestionnaireTaches()

while True:
    print("\nOptions:")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Marquer une tâche comme complète")
    print("4. Supprimer une tâche")
    print("5. Quitter")

    choix = input("Choisissez une option 1 à 5  ")

    if choix == '1':
        tache = input("Entrez la tâche à ajouter : ")
        gestionnaire.ajouter_tache(tache)
    elif choix == '2':
        gestionnaire.afficher_taches()
    elif choix == '3':
        index = int(input("Entrez l'index de la tâche à marquer comme complète : "))
        gestionnaire.marquer_complet(index)
    elif choix == '4':
        index = int(input("Entrez l'index de la tâche à supprimer : "))
        gestionnaire.supprimer_tache(index)
    elif choix == '5':
        print("Programme terminé.")
        break
    else:
        print("Option invalide. Veuillez réessayer.")
