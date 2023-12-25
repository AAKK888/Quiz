import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (67, 160, 71)  # Dark green
RED = (198, 40, 40)  # Dark red

# Quiz questions
questions = [
    {
        "question": "What causes earthquakes?",
        "options": ["Volcanic activity", "Tectonic plate movement", "Heavy rainfall"],
        "correct_answer": "Tectonic plate movement"
    },
    {
        "question": "Which scale measures the magnitude of earthquakes?",
        "options": ["Fahrenheit scale", "Richter scale", "Kelvin scale"],
        "correct_answer": "Richter scale"
    },
    {
        "question": "What is the imaginary line where most earthquakes occur called?",
        "options": ["Seismic zone", "Tectonic boundary", "Fault line"],
        "correct_answer": "Fault line"
    },
    {
        "question": "What is the capital city of France?",
        "options": ["Berlin", "Paris", "London"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "options": ["Mars", "Venus", "Jupiter"],
        "correct_answer": "Mars"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh"],
        "correct_answer": "Leonardo da Vinci"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Blue whale", "Giraffe"],
        "correct_answer": "Blue whale"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["William Shakespeare", "Charles Dickens", "Mark Twain"],
        "correct_answer": "William Shakespeare"
    },
    {
        "question": "What is the smallest country in the world?",
        "options": ["Monaco", "Vatican City", "San Marino"],
        "correct_answer": "Vatican City"
    },
    {
        "question": "Who painted the 'Starry Night'?",
        "options": ["Pablo Picasso", "Vincent van Gogh", "Claude Monet"],
        "correct_answer": "Vincent van Gogh"
    },
    {
        "question": "Which planet is known as the 'Morning Star' or 'Evening Star'?",
        "options": ["Mercury", "Venus", "Mars"],
        "correct_answer": "Venus"
    },
    {
        "question": "What is the largest desert in the world?",
        "options": ["Sahara Desert", "Arabian Desert", "Gobi Desert"],
        "correct_answer": "Sahara Desert"
    },
    {
        "question": "Who discovered penicillin?",
        "options": ["Marie Curie", "Alexander Fleming", "Louis Pasteur"],
        "correct_answer": "Alexander Fleming"
    },
    {
        "question": "What is the national animal of Australia?",
        "options": ["Kangaroo", "Koala", "Emu"],
        "correct_answer": "Kangaroo"
    },
    {
        "question": "What is the primary gas that makes up the Earth's atmosphere?",
        "options": ["Nitrogen", "Oxygen", "Carbon dioxide"],
        "correct_answer": "Nitrogen"
    },
    {
        "question": "Who developed the theory of general relativity?",
        "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking"],
        "correct_answer": "Albert Einstein"
    },
    {
        "question": "Which country is known as the 'Land of the Rising Sun'?",
        "options": ["China", "Japan", "South Korea"],
        "correct_answer": "Japan"
    },
    {
        "question": "What is the largest organ in the human body?",
        "options": ["Heart", "Skin", "Liver"],
        "correct_answer": "Skin"
    },
    {
        "question": "Which gas do plants primarily respire?",
        "options": ["Oxygen", "Carbon dioxide", "Nitrogen"],
        "correct_answer": "Carbon dioxide"
    },
    {
        "question": "Who is the author of 'To Kill a Mockingbird'?",
        "options": ["J.K. Rowling", "Harper Lee", "George Orwell"],
        "correct_answer": "Harper Lee"
    },
    # Add more questions in a similar format
]

# Variables
current_question = 0
score = 0
font = pygame.font.Font(None, 36)
timer_font = pygame.font.Font(None, 48)
feedback_font = pygame.font.Font(None, 24)

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Earthquake Quiz")

# Timer variables
TIMER_EVENT = pygame.USEREVENT + 1
TIMER_INTERVAL = 1000
time_remaining = 30

pygame.time.set_timer(TIMER_EVENT, TIMER_INTERVAL)


def display_question(question_num):
    screen.fill(WHITE)
    text = font.render("Question:", True, BLACK)
    screen.blit(text, (50, 50))

    question_text = font.render(questions[question_num]["question"], True, BLACK)
    screen.blit(question_text, (50, 100))

    options = questions[question_num]["options"]
    y = 200
    for option in options:
        option_text = font.render(option, True, BLACK)
        screen.blit(option_text, (100, y))
        y += 50


def check_answer(question_num, selected):
    correct_answer = questions[question_num]["correct_answer"]
    if selected == correct_answer:
        return True
    else:
        return False


def show_feedback(is_correct):
    feedback_text = "Correct!" if is_correct else "Incorrect!"
    text = feedback_font.render(feedback_text, True, GREEN if is_correct else RED)
    screen.blit(text, (50, 500))
    pygame.display.flip()
    pygame.time.delay(2000)  # Display feedback for 2 seconds


def update_timer():
    global time_remaining, current_question
    if time_remaining > 0:
        time_remaining -= 1
    else:
        pygame.time.set_timer(TIMER_EVENT, 0)
        if current_question < len(questions) - 1:
            current_question += 1
            time_remaining = 30
        else:
            current_question = 0  # Cycle back to the first question after completing all
            time_remaining = 30
            score = 0


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            selected = None
            y = 200
            for i in range(len(questions[current_question]["options"])):
                if 100 <= mouse_pos[0] <= 700 and y <= mouse_pos[1] <= y + 40:
                    selected = questions[current_question]["options"][i]
                    break
                y += 50

            if selected is not None:
                if check_answer(current_question, selected):
                    score += 1
                    show_feedback(True)
                else:
                    show_feedback(False)

                if current_question < len(questions) - 1:
                    current_question += 1
                    time_remaining = 30
                else:
                    current_question = 0  # Cycle back to the first question after completing all
                    time_remaining = 30
                    score = 0
        if event.type == TIMER_EVENT:
            update_timer()

    screen.fill(WHITE)
    display_question(current_question)

    pygame.draw.rect(screen, GRAY, (50, 550, 700, 30))
    progress_width = (time_remaining / 30) * 700
    pygame.draw.rect(screen, GREEN, (50, 550, progress_width, 30))

    timer_text = timer_font.render(f"Time: {time_remaining}", True, BLACK)
    screen.blit(timer_text, (600, 50))

    pygame.display.flip()
