import unittest
import sys

# Conf
MAX_WIDTH = 100

PHRASES = {
    "Le code propre facilite la maintenance":   {"block": [1],    "enabled": True},
    "Tester souvent évite beaucoup d erreurs":   {"block": [2],    "enabled": True},
    "Cette phrase ne doit pas s afficher":       {"block": [2, 3], "enabled": False},
    "Un bon code doit rester simple et clair":   {"block": [3],    "enabled": False},
    "La simplicité améliore la qualité du code": {"block": [3],    "enabled": True},
    "Refactoriser améliore la compréhension":    {"block": [3],    "enabled": True},
}


def format_line(text, width):
    """Format a line: lowercase, right-aligned with padding, framed with |."""
    text_lower = text.lower()
    inner_width = width - 4  # "| " + " |"

    if len(text_lower) > inner_width:
        text_lower = text_lower[:inner_width - 3] + "..."

    return f"| {text_lower.rjust(inner_width)} |"


def generate_display(phrases, width):
    """Display text blocks with borders according to the configuration."""
    blocks = {}
    for text, entry in phrases.items():
        if entry["enabled"]:
            for block in entry["block"]:
                if block not in blocks:
                    blocks[block] = []
                blocks[block].append(text)

    separator = "-" * width
    for block_num in sorted(blocks):
        print(separator)
        for text in blocks[block_num]:
            print(format_line(text, width))
        print(separator)
        print()


# TESTS

class TestExercice(unittest.TestCase):
    def test_exact_width(self):
        """Check that the line is exactly MAX_WIDTH characters long."""
        ligne = format_line("test", MAX_WIDTH)
        self.assertEqual(len(ligne), MAX_WIDTH)

    def test_lowercase(self):
        """Check that text is rendered in lowercase."""
        ligne = format_line("MAJUSCULES", MAX_WIDTH)
        self.assertIn("majuscules", ligne)
        self.assertNotIn("MAJUSCULES", ligne)

    def test_exclusion_rule(self):
        """Check that the excluded phrases have enabled=False and keep their block."""
        self.assertFalse(PHRASES["Cette phrase ne doit pas s afficher"]["enabled"])
        self.assertIn(2, PHRASES["Cette phrase ne doit pas s afficher"]["block"])
        self.assertIn(3, PHRASES["Cette phrase ne doit pas s afficher"]["block"])
        self.assertFalse(PHRASES["Un bon code doit rester simple et clair"]["enabled"])
        self.assertIn(3, PHRASES["Un bon code doit rester simple et clair"]["block"])

    def test_excluded_phrases_not_displayed(self):
        """Check that disabled phrases do not appear in displayed blocks."""
        import io
        from contextlib import redirect_stdout

        f = io.StringIO()
        with redirect_stdout(f):
            generate_display(PHRASES, MAX_WIDTH)
        output = f.getvalue()

        self.assertNotIn("cette phrase ne doit pas s afficher", output)
        self.assertNotIn("un bon code doit rester simple et clair", output)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        sys.argv.pop()
        unittest.main()
    else:
        generate_display(PHRASES, MAX_WIDTH)
