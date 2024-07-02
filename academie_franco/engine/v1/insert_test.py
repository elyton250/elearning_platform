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

users_data = [
    {"name": "student1", "email": "student1@example.com", "password": "hashed_password", "roles": ["student"]},
    { "name": "instructor1", "email": "instructor1@example.com", "password": "hashed_password", "roles": ["instructor"]}
]

# Sample courses
courses_data = [
  # Add French course data here (10 courses)
  {
    "title": "Français pour débutants",  # French for Beginners
    "description": "Apprenez les bases du français et commencez à converser !",  # Learn the basics of French and start conversing!
    "instructor_id": 1,  # Assign an instructor ID for French courses (replace with actual ID)
    "students_enrolled": [],
    "modules": [
      "Introduction à la langue française",  # Introduction to the French Language
      "Salutations et présentations",  # Greetings and Introductions
      "L'alphabet et la prononciation",  # The Alphabet and Pronunciation
      "Les phrases de base",  # Basic Phrases
    ],
  },
  {
    "title": "Français intermédiaire",  # Intermediate French
    "description": "Développez vos compétences linguistiques et renforcez votre conversation en français.",  # Develop your language skills and strengthen your French conversation.
    "instructor_id": 1,
    "students_enrolled": [],
    "modules": [
      "Grammaire française plus avancée",  # More Advanced French Grammar
      "Compréhension orale et écrite",  # Listening and Reading Comprehension
      "Expression écrite et conversation",  # Written Expression and Conversation
      "Les temps verbaux",  # Verb Tenses
    ],
  },
  {
    "title": "Français avancé",  # Advanced French
    "description": "Maîtrisez la langue française et exprimez-vous avec aisance.",  # Master the French language and express yourself with ease.
    "instructor_id": 1,
    "students_enrolled": [],
    "modules": [
      "Vocabulaire thématique",  # Thematic Vocabulary
      "Stylistique et expression nuancée",  # Stylistics and Nuanced Expression
      "Préparation aux examens (DELF, TCF)",  # Exam Preparation (DELF, TCF)
      "Français des affaires",  # Business French
    ],
  },
  {
    "title": "Conversation française",  # French Conversation
    "description": "Améliorez votre aisance à l'oral et pratiquez la conversation en français dans un cadre dynamique.",  # Improve your speaking fluency and practice French conversation in a dynamic setting.
    "instructor_id": 1,
    "students_enrolled": [],
    "modules": [
      "Discussions sur des sujets d'actualité",  # Discussions on Current Events
      "Jeux de rôle et simulations",  # Role-playing and Simulations
      "Débats et présentations",  # Debates and Presentations
      "Expression orale spontanée",  # Spontaneous Speaking
    ],
  },
  {
    "title": "Français sur objectifs spécifiques",  # French for Specific Purposes
    "description": "Apprenez le français adapté à vos besoins professionnels ou personnels.",  # Learn French tailored to your professional or personal needs.
    "instructor_id": 1,
    "students_enrolled": [],
    "modules": [
      "Français du tourisme",  # French for Tourism
      "Français des affaires",  # Business French
      "Français juridique",  # Legal French
      "Français médical",  # Medical French
    ],
  },
  {
    "title": "French for Travelers",  # Added course
    "description": "Learn essential French phrases and vocabulary for navigating French-speaking destinations with confidence.",
    "instructor_id": 1,  # Assign an instructor ID for French courses (replace with actual ID)
    "students_enrolled": [],
    "modules": [
      "Greetings and basic conversation",
      "Asking for directions and transportation",
      "Ordering food and drinks",
      "Shopping and bargaining",
      "Cultural etiquette and customs",
    ],
  },
  
  {
        "title": "Français pour débutants",  # French for Beginners
        "description": "Apprenez les bases du français et commencez à converser !",  # Learn the basics of French and start conversing!
        "instructor_id": 1,  # Assign an instructor ID for French courses (replace with actual ID)
        "students_enrolled": [],
        "modules": [
            "Introduction à la langue française",  # Introduction to the French Language
            "Salutations et présentations",  # Greetings and Introductions
            "L'alphabet et la prononciation",  # The Alphabet and Pronunciation
            "Les phrases de base",  # Basic Phrases
        ],
    },
    {
        "title": "Français intermédiaire",  # Intermediate French
        "description": "Développez vos compétences linguistiques et renforcez votre conversation en français.",  # Develop your language skills and strengthen your French conversation.
        "instructor_id": 1,
        "students_enrolled": [],
        "modules": [
            "Grammaire française plus avancée",  # More Advanced French Grammar
            "Compréhension orale et écrite",  # Listening and Reading Comprehension
            "Expression écrite et conversation",  # Written Expression and Conversation
            "Les temps verbaux",  # Verb Tenses
        ],
    },
    {
        "title": "Français avancé",  # Advanced French
        "description": "Maîtrisez la langue française et exprimez-vous avec aisance.",  # Master the French language and express yourself with ease.
        "instructor_id": 1,
        "students_enrolled": [],
        "modules": [
            "Vocabulaire thématique",  # Thematic Vocabulary
            "Stylistique et expression nuancée",  # Stylistics and Nuanced Expression
            "Préparation aux examens (DELF, TCF)",  # Exam Preparation (DELF, TCF)
            "Français des affaires",  # Business French
        ],
    },
    {
        "title": "Conversation française",  # French Conversation
        "description": "Améliorez votre aisance à l'oral et pratiquez la conversation en français dans un cadre dynamique.",  # Improve your speaking fluency and practice French conversation in a dynamic setting.
        "instructor_id": 1,
        "students_enrolled": [],
        "modules": [
            "Discussions sur des sujets d'actualité",  # Discussions on Current Events
            "Jeux de rôle et simulations",  # Role-playing and Simulations
            "Débats et présentations",  # Debates and Presentations
            "Expression orale spontanée",  # Spontaneous Speaking
        ],
    },
    {
        "title": "Français sur objectifs spécifiques",  # French for Specific Purposes
        "description": "Apprenez le français adapté à vos besoins professionnels ou personnels.",  # Learn French tailored to your professional or personal needs.
        "instructor_id": 1,
        "students_enrolled": [],
        "modules": [
            "Français du tourisme",  # French for Tourism
            "Français des affaires",  # Business French
            "Français juridique",  # Legal French
            "Français médical",  # Medical French
        ],
    },
    {
        "title": "Français pour voyageurs",  # French for Travelers
        "description": "Préparez-vous pour vos voyages dans les pays francophones.",  # Prepare for your travels in French-speaking countries.
        "instructor_id": 2,
        "students_enrolled": [],
        "modules": [
            "Expressions de voyage essentielles",  # Essential Travel Phrases
            "Navigation et directions",  # Navigation and Directions
            "Interaction dans les restaurants et hôtels",  # Interaction in Restaurants and Hotels
            "Situations d'urgence",  # Emergency Situations
        ],
    },
    {
        "title": "Français pour les affaires",  # French for Business
        "description": "Améliorez vos compétences linguistiques pour le monde des affaires.",  # Improve your language skills for the business world.
        "instructor_id": 2,
        "students_enrolled": [],
        "modules": [
            "Vocabulaire commercial",  # Commercial Vocabulary
            "Correspondance professionnelle",  # Professional Correspondence
            "Négociations et réunions",  # Negotiations and Meetings
            "Culture d'entreprise française",  # French Business Culture
        ],
    },
]


for user_data in users_data:
    user_data['_id'] = generate_userID()  # Generate 5-character ID

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
users_collection.insert_many(users_data)
courses_collection.insert_many(courses_data)
# enrollments_collection.insert_many(enrollments_data)
# assignments_collection.insert_many(assignments_data)
# grades_collection.insert_many(grades_data)

# Confirm data insertion
print("Sample data inserted successfully.")

# Close MongoDB connection
client.close()