from engine import client

import random
import string

def generate_courseID():
    """
    Generates a unique 3-character ID.
    """
    # Define the characters allowed in the ID (excluding ambiguous ones)
    allowed_chars = string.ascii_uppercase + string.digits
    # Generate a random 3-character ID
    unique_id = ''.join(random.choice(allowed_chars) for _ in range(3))
    return unique_id


def generate_userID():
    """
    Generates a unique ID of specified length.
    """
    allowed_chars = string.ascii_uppercase + string.digits
    unique_id = ''.join(random.choice(allowed_chars) for _ in range(5))
    return unique_id

db = client['edu_app_db']


users_collection = db['users']
courses_collection = db['courses']
enrollments_collection = db['enrollments']
assignments_collection = db['assignments']
grades_collection = db['grades']

# Drop collections if they already exist (for testing purposes)
users_collection.drop()
courses_collection.drop()
enrollments_collection.drop()
assignments_collection.drop()
grades_collection.drop()


# insertion samples

# users_data = [
#     {"name": "student1", "email": "student1@example.com", "password": "hashed_password", "roles": ["student"]},
#     { "name": "instructor1", "email": "instructor1@example.com", "password": "hashed_password", "roles": ["instructor"]}
# ]

# Sample courses
courses_data = [
  {
    "title": "Français pour débutants",
    "description": "Apprenez les bases du français et commencez à converser !",
    "instructor_id": 1,
    "students_enrolled": [],
    "modules": [
      "Introduction à la langue française",
      "Salutations et présentations",
      "L'alphabet et la prononciation",
      "Les phrases de base"
    ],
    "embed_link": '<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vR76f5BnkUdLaQXVsMurmeFS9QPSDJ6uIP3NkUKcS24EsWTQKpg9EBgowpGuxTrpA/embed?start=false&loop=false&delayms=10000" frameborder="0" width="1920" height="1109" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>',
    "test": {
      "Q1": ["Quelle est la capitale de la France?", "Paris", "Lyon", "Marseille", "Toulouse"],
      "Q2": ["Comment dit-on 'hello' en français?", "Bonjour", "Au revoir", "Merci", "S'il vous plaît"],
      "Q3": ["Quelle est la couleur du ciel?", "Vert","Bleu", "Rouge", "Jaune"],
      "Q4": ["Combien de jours y a-t-il dans une semaine?", "7", "5", "10", "14"],
      "Q5": ["Quel est le chiffre après 3?", "4", "2", "5", "6"],
      "answers": {
        "Q1": 1,
        "Q2": 1,
        "Q3": 2,
        "Q4": 1,
        "Q5": 1
      }
    }
  },
  {
    "title": "Français intermédiaire",
    "description": "Développez vos compétences linguistiques et renforcez votre conversation en français.",
    "instructor_id": 1,
    "students_enrolled": [],
    "modules": [
      "Grammaire française plus avancée",
      "Compréhension orale et écrite",
      "Expression écrite et conversation",
      "Les temps verbaux"
    ],
    "embed_link": '<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vR76f5BnkUdLaQXVsMurmeFS9QPSDJ6uIP3NkUKcS24EsWTQKpg9EBgowpGuxTrpA/embed?start=false&loop=false&delayms=10000" frameborder="0" width="1920" height="1109" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>',
    "test": {
      "Q1": ["Quel est le participe passé du verbe 'manger'?", "Mangée", "Mangeait", "Mangés", "Mangé"],
      "Q2": ["Quelle est la traduction de 'book' en français?", "Livre", "Boucle", "Boîte", "Banc"],
      "Q3": ["Quel est le contraire de 'grand'?", "Petit", "Lourd", "Léger", "Court"],
      "Q4": ["Comment dit-on 'to play' en français?", "Jouer", "Manger", "Lire", "Écrire"],
      "Q5": ["Quelle est la couleur de l'herbe?", "Bleue",  "Verte", "Rouge", "Jaune"],
      "answers": {
        "Q1": 3,
        "Q2": 1,
        "Q3": 1,
        "Q4": 1,
        "Q5": 2
      }
    }
  },
  {
    "title": "Français avancé",
    "description": "Maîtrisez la langue française et exprimez-vous avec aisance.",
    "instructor_id": 1,
    "students_enrolled": [],
    "modules": [
      "Vocabulaire thématique",
      "Stylistique et expression nuancée",
      "Préparation aux examens (DELF, TCF)",
      "Français des affaires"
    ],
    "embed_link": '<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vR76f5BnkUdLaQXVsMurmeFS9QPSDJ6uIP3NkUKcS24EsWTQKpg9EBgowpGuxTrpA/embed?start=false&loop=false&delayms=10000" frameborder="0" width="1920" height="1109" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>',
    "test": {
      "Q1": ["Que signifie 'périphrase'?", "Une phrase complexe", "Une figure de style", "Une forme verbale", "Un temps grammatical"],
      "Q2": ["Quel est le synonyme de 'rapide'?", "Vite", "Lent", "Fort", "Haut"],
      "Q3": ["Comment dit-on 'to understand' en français?",  "Apprendre", "Comprendre", "Vendre", "Entendre"],
      "Q4": ["Quel est le pluriel de 'cheval'?", "Chevaux", "Chevals", "Chevalles", "Chevales"],
      "Q5": ["Quelle est la capitale du Canada?", "Ottawa", "Toronto", "Vancouver", "Montréal"],
      "answers": {
        "Q1": 2,
        "Q2": 1,
        "Q3": 2,
        "Q4": 1,
        "Q5": 2
      }
    }
  },
  {
    "title": "Français pour voyager",
    "description": "Apprenez les phrases essentielles pour voyager en français.",
    "instructor_id": 1,
    "students_enrolled": [],
    "modules": [
      "Expressions utiles en voyage",
      "Hôtellerie et restauration",
      "Transport et directions",
      "Culture et coutumes"
    ],
    "embed_link": '<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vR76f5BnkUdLaQXVsMurmeFS9QPSDJ6uIP3NkUKcS24EsWTQKpg9EBgowpGuxTrpA/embed?start=false&loop=false&delayms=10000" frameborder="0" width="1920" height="1109" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>',
    "test": {
      "Q1": ["Comment dit-on 'train' en français?", "Train", "Voiture", "Avion", "Bateau"],
      "Q2": ["Quel est le plat typique français?", "Croissant", "Pizza", "Hamburger", "Sushi"],
      "Q3": ["Quelle est la monnaie en France?", "Euro", "Dollar", "Livres sterling", "Yen"],
      "Q4": ["Quel est le monument emblématique de Paris?", "Tour Eiffel", "Big Ben", "Statue de la Liberté", "Colisée"],
      "Q5": ["Comment dit-on 'merci' en français?", "Merci", "Hello", "Goodbye", "Please"],
      "answers": {
        "Q1": 1,
        "Q2": 1,
        "Q3": 1,
        "Q4": 1,
        "Q5": 1
      }
    }
  }]

# for user_data in users_data:
#     user_data['_id'] = generate_userID()  # Generate 5-character ID

for course_data in courses_data:
    course_data['_id'] = generate_courseID()  # Generate 3-character ID

# # Sample enrollments
# enrollments_data = [
#     {"user_id": 2, "course_id": 101, "enrollment_date": "2024-06-18", "completion_status": "in-progress"},
#     {"user_id": 2, "course_id": 102, "enrollment_date": "2024-06-18", "completion_status": "completed"}
# ]

# # Sample assignments
# assignments_data = [
#     {"_id": 203, "course_id": 101, "title": "Module 1 Quiz", "description": "Quiz on MongoDB basics", "due_date": "2024-06-25", "assigned_date": "2024-06-18", "max_score": 10, "submissions": []},
#     {"_id": 204, "course_id": 102, "title": "Python Project", "description": "Create a Python project", "due_date": "2024-07-02", "assigned_date": "2024-06-18", "max_score": 20, "submissions": []}
# ]

# # Sample grades
# grades_data = [
#     {"user_id": 1, "assignment_id": 201, "course_id": 101, "score": 8, "graded_by": 2, "submission_date": "2024-06-25"},
#     {"user_id": 1, "assignment_id": 202, "course_id": 102, "score": 18, "graded_by": 2, "submission_date": "2024-07-02"}
# ]

# Insert data into collections
# users_collection.insert_many(users_data)
courses_collection.insert_many(courses_data)
# enrollments_collection.insert_many(enrollments_data)
# assignments_collection.insert_many(assignments_data)
# grades_collection.insert_many(grades_data)

# Confirm data insertion
print("Sample data inserted successfully.")

# Close MongoDB connection
client.close()