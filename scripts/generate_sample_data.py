import csv
import random

# Closed questions and answers
closed_questions = [
    "Did you enjoy the course?",
    "Was the material clear?",
    "Did you feel challenged?",
    "At the beginning of the course the instructor explained its objectives and requirements.",
    "The course was well organized and systematic.",
    "The content of the course did not overlap with other courses.",
    "The instructor presented the course topics in an understandable way.",
    "The course was intellectually stimulating and encouraged interest.",
    "The instructor provided feedback on my performance.",
    "The instructor's attitude toward students was respectful and accommodating.",
    "I would gladly attend another course with this instructor.",
]

closed_answers = [
    "Completely disagree",
    "Disagree",
    "Somewhat disagree",
    "Neither agree nor disagree",
    "Somewhat agree",
    "Agree",
    "Completely agree"
]

# Open-ended questions
open_questions = [
    "What did you like the most in this course?",
    "What could be improved?"
]

# Sample course data
courses = [
    {"course_name": "Introduction to Python", "instructor": "Dr. Code"},
    {"course_name": "Advanced Machine Learning", "instructor": "Prof. AI"},
    {"course_name": "Data Visualization Basics", "instructor": "Dr. Charts"},
]

# Sample open-ended answers (to randomize)
sample_open_answers = [
    "The hands-on assignments were great!",
    "The instructor explained concepts really well.",
    "I wish there were more examples.",
    "The pacing of the course could be improved.",
    "Loved the group projects!",
    "The lectures were engaging and interactive.",
    "Would have liked more real-world case studies.",
    "The materials provided were excellent.",
]

# Generate CSV
def generate_csv(filename="sample_data.csv", num_responses=100):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["course_name", "instructor", "question_text", "answer"])

        # Generate closed-ended responses
        for _ in range(num_responses):
            course = random.choice(courses)
            question = random.choice(closed_questions)
            answer = random.choice(closed_answers)
            writer.writerow([course["course_name"], course["instructor"], question, answer])

        # Generate open-ended responses
        for course in courses:
            for question in open_questions:
                answer = random.choice(sample_open_answers)
                writer.writerow([course["course_name"], course["instructor"], question, answer])

# Run the script to generate the CSV
generate_csv()
print("Sample data CSV generated successfully!")
