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
    {"_id": 1, "username": "student1", "email": "student1@example.com", "password": "hashed_password", "roles": ["student"]},
    {"_id": 2, "username": "instructor1", "email": "instructor1@example.com", "password": "hashed_password", "roles": ["instructor"]}
]

# Sample courses
courses_data = [
    {"_id": 101, "title": "Introduction to MongoDB", "description": "Learn the basics of MongoDB", "instructor_id": 2, "students_enrolled": [], "modules": ["Module 1", "Module 2"]},
    {"_id": 102, "title": "Python Programming", "description": "Learn Python programming language", "instructor_id": 2, "students_enrolled": [], "modules": ["Module 1", "Module 2", "Module 3"]}
]

# Sample enrollments
enrollments_data = [
    {"user_id": 1, "course_id": 101, "enrollment_date": "2024-06-18", "completion_status": "in-progress"},
    {"user_id": 1, "course_id": 102, "enrollment_date": "2024-06-18", "completion_status": "completed"}
]

# Sample assignments
assignments_data = [
    {"_id": 201, "course_id": 101, "title": "Module 1 Quiz", "description": "Quiz on MongoDB basics", "due_date": "2024-06-25", "assigned_date": "2024-06-18", "max_score": 10, "submissions": []},
    {"_id": 202, "course_id": 102, "title": "Python Project", "description": "Create a Python project", "due_date": "2024-07-02", "assigned_date": "2024-06-18", "max_score": 20, "submissions": []}
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