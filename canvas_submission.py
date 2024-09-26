import os
import requests
import csv

# Base URL for Canvas API
BASE_URL = "https://<your_canvas_instance>.instructure.com/api/v1"

# Get the API token from environment variable
API_TOKEN = os.getenv("CANVAS_API_TOKEN")

# Headers for the API request
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def get_courses():
    """Fetch the list of courses."""
    response = requests.get(f"{BASE_URL}/courses", headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_students(course_id):
    """Fetch the list of students for a given course."""
    response = requests.get(f"{BASE_URL}/courses/{course_id}/students", headers=HEADERS)
    response.raise_for_status()
    return response.json()

def create_csv():
    """Create a CSV file with the list of students and their email addresses."""
    courses = get_courses()
    with open('students_list.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Course Name', 'Student Name', 'Email'])

        for course in courses:
            course_name = course['name']
            students = get_students(course['id'])
            for student in students:
                writer.writerow([course_name, student['name'], student['email']])

if __name__ == "__main__":
    create_csv()
