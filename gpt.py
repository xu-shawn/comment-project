from openai import OpenAI


def generate_comment(
    subject: str,
    teacher: str,
    student: str,
    grade: str,
    class_participation_grade: str,
    homework_performance_grade: str,
    strength: str,
    weakness: str,
    class_habit: str,
    tardy: str,
    absence: str,
) -> str:
    with open("key") as keyFile:
        client = OpenAI(api_key=keyFile.readline())

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are helping a teacher write comments for students\n"
                "For this, you would need:\n"
                "1. A short description of the course\n"
                "2. A description of student attributes (work ethic, collaboration, humor, perseverance through difficulty, seeks out extra help, etc.)\n"
                "3. A summary of some key exam grades or essay excerpts.\n"
                "4. Progress toward specific learning outcomes\n"
                "5. A suggestion for what to improve on or what to do for extra enrichment.\n"
                "6. A summary of the semester grade and a closing sentence.\n"
                "Here is an example of a teacher's comment:\n"
                "This semester in AP AB Calculus, we covered the topics of limits, continuity, and differentiation and began the study of integration, which we will continue into the second semester. In addition to daily homework and frequent quizzes, we had three in-class unit tests, a cumulative final exam, and two projects, one on predicting stock prices using derivatives and one on modeling fluid flow using related rates and Torricelli’s Law."
                "Migo, you have a stellar work ethic and student habits. You faithfully complete the nightly homework and are fully engaged in class discussions. You are not really comfortable asking questions during the larger class discussion but you work well in small groups with your peers. Migo, you have not needed to come to see me outside of class for extra help, and you seem to grasp the content easily."
                "Migo, your performance in the course this semester has been phenomenal; you have received A’s on all tests, including a 97% of your cumulative final exam. I know you could use more challenges in the course so I would encourage you to start reading the proofs in the textbook and stopping by during my office hours to chat about them. You have significant potential to go further in mathematics in college, and proofs will be a major aspect of those courses."
                "Migo, the jump in difficulty level from precalculus to AP Calculus is significant, and you have excelled with this increased challenge. You have earned an A for the semester and I look forward to your continued success during the remainder of the year.\n"
                "The user will provide you the detail of the student.",
            },
            {
                "role": "user",
                "content": f"Subject: {subject}, "
                f"Teacher name: {teacher}, "
                f"Student name: {student}, "
                f"Grade: {grade}, "
                f"Class Participation Grade: {class_participation_grade}, "
                f"Homework Performance Grade: {homework_performance_grade}, "
                f"Strength: {strength}, "
                f"Weakness: {weakness}, "
                f"Class Habit: {class_habit}, "
                f"Times Tardy: {tardy}, "
                f"Times Absent: {absence}",
            },
        ],
    )

    return completion.choices[0].message.content
