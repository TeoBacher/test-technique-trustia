import unittest
import sys

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
    ["clean_code"],            # Block 1
    ["test_often"],            # Block 2
    ["simplicity", "refactor"] # Block 3
]

def format_line(texte, largeur):
    """Set up a line -> lowercase letters, right-aligned, and with side margins."""
    texte_clean = texte.lower()
    available_space = largeur - 2
    
    if len(texte_clean) > available_space:
        texte_clean = texte_clean[:available_space - 3] + "..."
        
    return f"|{texte_clean.rjust(available_space)}|"

def generate_display(structure, db, width):
    """Displays the text blocks with borders according to the configuration."""
    for bloc in structure:
        print("-" * width)
        for cle in bloc:
            if cle in db:
                print(format_line(db[cle], width))
        print("-" * width)
        print()

# TESTS

class TestExercice(unittest.TestCase):
    def test_exact_width(self):
        """Check that the line is exactly 100 characters long."""
        ligne = format_line("test", MAX_WIDTH)
        self.assertEqual(len(ligne), MAX_WIDTH)

    def test_exclusion_rule(self):
        """Check that the excluded phrases are not in the display structure."""
        cles_utilisees = [cle for bloc in DISPLAY_STRUCTURE for cle in bloc]
        self.assertNotIn("no_display", cles_utilisees)
        self.assertNotIn("simple_clear", cles_utilisees)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        sys.argv.pop()
        unittest.main()
    else:
        generate_display(DISPLAY_STRUCTURE, PHRASES_DB, MAX_WIDTH)