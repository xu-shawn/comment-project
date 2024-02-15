from openai import OpenAI


def generate_comment(
    client: OpenAI,
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
    outcomes: str,
    memorable_moments: str,
    sample: str,
) -> str:
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
                + sample
                + "The user will provide you the detail of the student.",
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
                f"Times Absent: {absence}, "
                f"Target Learning Outcomes: {outcomes}, "
                f"Memorable Moments: {memorable_moments}",
            },
        ],
    )

    return completion.choices[0].message.content
