from engine import client

db = client['edu_app_db']


users_collection = db['users']
courses_collection = db['courses']
enrollments_collection = db['enrollments']
assignments_collection = db['assignments']
grades_collection = db['grades']

# Drop collections if they already exist (for testing purposes)
# users_collection.drop()
# courses_collection.drop()
# enrollments_collection.drop()
# assignments_collection.drop()
# grades_collection.drop()


# insertion samples

users_data = [
    {"_id": 3, "username": "student1", "email": "student1@example.com", "password": "hashed_password", "roles": ["student"]},
    {"_id": 4, "username": "instructor1", "email": "instructor1@example.com", "password": "hashed_password", "roles": ["instructor"]}
]

# Sample courses
courses_data = [
    # Add course data here (10 courses)
    {"_id": 103, "title": "Data Science Fundamentals", "description": "Explore data analysis, visualization, and machine learning", "instructor_id": 2, "students_enrolled": [], "modules": ["Introduction", "Data Cleaning", "Exploratory Data Analysis", "Regression Models"]},
    {"_id": 104, "title": "Introduction to Cybersecurity", "description": "Learn about network security, encryption, and ethical hacking", "instructor_id": 2, "students_enrolled": [], "modules": ["Cyber Threats", "Network Defense", "Cryptography Basics"]},
    {"_id": 105, "title": "Mobile App Development with React Native", "description": "Build cross-platform mobile apps using React Native", "instructor_id": 2, "students_enrolled": [], "modules": ["React Basics", "Navigation", "API Integration"]},
    {"_id": 106, "title": "Digital Marketing Strategies", "description": "Understand SEO, social media marketing, and content creation", "instructor_id": 2, "students_enrolled": [], "modules": ["SEO Optimization", "Social Media Campaigns", "Email Marketing"]},
    {"_id": 107, "title": "Cloud Computing Essentials", "description": "Dive into cloud platforms like AWS, Azure, and Google Cloud", "instructor_id": 2, "students_enrolled": [], "modules": ["Cloud Services", "Deployment", "Scalability"]},
    {"_id": 108, "title": "Game Development with Unity", "description": "Create 2D and 3D games using Unity game engine", "instructor_id": 2, "students_enrolled": [], "modules": ["Game Mechanics", "Physics", "Animation"]},
    {"_id": 109, "title": "Blockchain and Cryptocurrencies", "description": "Explore decentralized technologies and cryptocurrencies", "instructor_id": 2, "students_enrolled": [], "modules": ["Blockchain Basics", "Smart Contracts", "Crypto Wallets"]},
    {"_id": 110, "title": "UI/UX Design Principles", "description": "Design user-friendly interfaces and enhance user experiences", "instructor_id": 2, "students_enrolled": [], "modules": ["User Research", "Wireframing", "Prototyping"]},
    {"_id": 111, "title": "Advanced Python Programming", "description": "Level up your Python skills with advanced topics", "instructor_id": 2, "students_enrolled": [], "modules": ["Decorators", "Generators", "Multithreading"]},
    {"_id": 112, "title": "Agile Project Management", "description": "Learn agile methodologies for efficient project delivery", "instructor_id": 2, "students_enrolled": [], "modules": ["Scrum", "Kanban", "Sprint Planning"]},
]

# Sample enrollments
enrollments_data = [
    {"user_id": 2, "course_id": 101, "enrollment_date": "2024-06-18", "completion_status": "in-progress"},
    {"user_id": 2, "course_id": 102, "enrollment_date": "2024-06-18", "completion_status": "completed"}
]

# Sample assignments
assignments_data = [
    {"_id": 203, "course_id": 101, "title": "Module 1 Quiz", "description": "Quiz on MongoDB basics", "due_date": "2024-06-25", "assigned_date": "2024-06-18", "max_score": 10, "submissions": []},
    {"_id": 204, "course_id": 102, "title": "Python Project", "description": "Create a Python project", "due_date": "2024-07-02", "assigned_date": "2024-06-18", "max_score": 20, "submissions": []}
]

# Sample grades
grades_data = [
    {"user_id": 1, "assignment_id": 201, "course_id": 101, "score": 8, "graded_by": 2, "submission_date": "2024-06-25"},
    {"user_id": 1, "assignment_id": 202, "course_id": 102, "score": 18, "graded_by": 2, "submission_date": "2024-07-02"}
]

# Insert data into collections
users_collection.insert_many(users_data)
courses_collection.insert_many(courses_data)
enrollments_collection.insert_many(enrollments_data)
assignments_collection.insert_many(assignments_data)
grades_collection.insert_many(grades_data)

# Confirm data insertion
print("Sample data inserted successfully.")

# Close MongoDB connection
client.close()