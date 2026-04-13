#Conf
MAX_WIDTH = 100

# phrase dictionary
PHRASES_DB = {
    "clean_code": "Le code propre facilite la maintenance",
    "test_often": "Tester souvent évite beaucoup d erreurs",
    "no_display": "Cette phrase ne doit pas s afficher",       # Excluded
    "simple_clear": "Un bon code doit rester simple et clair", # Excluded
    "simplicity": "La simplicité améliore la qualité du code",
    "refactor": "Refactoriser améliore la compréhension"
}

# The order and selection of lines
DISPLAY_STRUCTURE = [
    ["clean_code"],            # Bloc 1
    ["test_often"],            # Bloc 2
    ["simplicity", "refactor"] # Bloc 3
]