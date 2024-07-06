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
      "Les phrases de base",
    ],
    "embed_link": '<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vR76f5BnkUdLaQXVsMurmeFS9QPSDJ6uIP3NkUKcS24EsWTQKpg9EBgowpGuxTrpA/embed?start=false&loop=false&delayms=10000" frameborder="0" width="1920" height="1109" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>',
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
      "Les temps verbaux",
    ],
    "embed_link": '<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vR76f5BnkUdLaQXVsMurmeFS9QPSDJ6uIP3NkUKcS24EsWTQKpg9EBgowpGuxTrpA/embed?start=false&loop=false&delayms=10000" frameborder="0" width="1920" height="1109" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>',
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
      "Français des affaires",
    ],
    "embed_link": '<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vR76f5BnkUdLaQXVsMurmeFS9QPSDJ6uIP3NkUKcS24EsWTQKpg9EBgowpGuxTrpA/embed?start=false&loop=false&delayms=10000" frameborder="0" width="1920" height="1109" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>',
  },
  {
    "title": "Conversation française",
    "description": "Améliorez votre aisance à l'oral et pratiquez la conversation en français dans un cadre dynamique.",
    "instructor_id": 1,
    "students_enrolled": [],
    "modules": [
      "Discussions sur des sujets d'actualité",
      "Jeux de rôle et simulations",
      "Débats et présentations",
      "Expression orale spontanée",
    ],
    "embed_link": '<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vR76f5BnkUdLaQXVsMurmeFS9QPSDJ6uIP3NkUKcS24EsWTQKpg9EBgowpGuxTrpA/embed?start=false&loop=false&delayms=10000" frameborder="0" width="1920" height="1109" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>',
  },
  {
    "title": "Français sur objectifs spécifiques",
    "description": "Apprenez le français adapté à vos besoins professionnels ou personnels.",
    "instructor_id": 1,
    "students_enrolled": [],
    "modules": [
      "Français du tourisme",
      "Français des affaires",
      "Français juridique",
      "Français médical",
    ],
    "embed_link": '<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vR76f5BnkUdLaQXVsMurmeFS9QPSDJ6uIP3NkUKcS24EsWTQKpg9EBgowpGuxTrpA/embed?start=false&loop=false&delayms=10000" frameborder="0" width="1920" height="1109" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>',
  },
  {
    "title": "French for Travelers",
    "description": "Learn essential French phrases and vocabulary for navigating French-speaking destinations with confidence.",
    "instructor_id": 1,
    "students_enrolled": [],
    "modules": [
      "Greetings and basic conversation",
      "Asking for directions and transportation",
      "Ordering food and drinks",
      "Shopping and bargaining",
      "Cultural etiquette and customs",
    ],
    "embed_link": '<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vR76f5BnkUdLaQXVsMurmeFS9QPSDJ6uIP3NkUKcS24EsWTQKpg9EBgowpGuxTrpA/embed?start=false&loop=false&delayms=10000" frameborder="0" width="1920" height="1109" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>',
  },
  {
    "title": "Français pour les affaires",
    "description": "Améliorez vos compétences linguistiques pour le monde des affaires.",
    "instructor_id": 1,
    "students_enrolled": [],
    "modules": [
      "Vocabulaire commercial",
      "Correspondance professionnelle",
      "Négociations et réunions",
      "Culture d'entreprise française",
    ],
    "embed_link": '<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vR76f5BnkUdLaQXVsMurmeFS9QPSDJ6uIP3NkUKcS24EsWTQKpg9EBgowpGuxTrpA/embed?start=false&loop=false&delayms=10000" frameborder="0" width="1920" height="1109" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>',
  },
]





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