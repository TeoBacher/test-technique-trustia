# Test Technique Trustia

## Exercice 1

### Lancer le programme

```bash
cd exo1
python exercice_1.py
```

### Lancer les tests

```bash
cd exo1
python exercice_1.py test
```

---

## Exercice 2

Application web Django de gestion de produits et de facturation.

### Installation

```bash
cd exo2
python -m venv venv
source venv/bin/activate  # Windows : venv\Scripts\activate
pip install -r requirements.txt
```

### Lancer l'application

```bash
python manage.py migrate
python manage.py runserver
```

L'application est accessible sur [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Lancer les tests

```bash
python manage.py test inventory
```
