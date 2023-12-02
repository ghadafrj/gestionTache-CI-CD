
import unittest
from GestTache import GestionnaireTaches

class TestGestionnaireTaches(unittest.TestCase):
    def setUp(self):
        # Créer une instance du gestionnaire de tâches pour les tests
        self.gestionnaire = GestionnaireTaches()

    def test_ajouter_tache(self):
        self.gestionnaire.ajouter_tache("Test tâche")
        self.assertIn("Test tâche", self.gestionnaire.taches)

    def test_afficher_taches(self):
        # Teste si l'affichage fonctionne correctement sans lever d'exception
        self.gestionnaire.afficher_taches()

    def test_marquer_complet(self):
        self.gestionnaire.ajouter_tache("Test tâche")
        self.gestionnaire.marquer_complet(1)  # Utilisez l'index 1 car nous avons une tâche
        # Vous pouvez étendre ce test pour vérifier si la tâche est effectivement marquée comme complète

    def test_supprimer_tache(self):
        self.gestionnaire.ajouter_tache("Test tâche")
        self.gestionnaire.supprimer_tache(1)  # Utilisez l'index 1 car nous avons une tâche
        self.assertNotIn("Test tâche", self.gestionnaire.taches)