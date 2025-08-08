from recomendation import recommend_courses

courses_db = [
    {
        "id": 1,
        "title": "Введение в Python",
        "category": "IT",
        "required_skills": ["базовые алгоритмы"],
        "difficulty": "начальный",
        "workload_hours": 4,
        "career_relevance": ["data scientist", "ML engineer"]
    },
    {
        "id": 2,
        "title": "Основы нейросетей",
        "category": "искусственный интеллект",
        "required_skills": ["Python", "линейная алгебра"],
        "difficulty": "средний",
        "workload_hours": 6,
        "career_relevance": ["ML engineer"]
    }
]

# Вводные данные абитуриента
user_input = {
    "interests": ["IT", "искусственный интеллект"],
    "skills": ["Python"],
    "goals": "ML engineer",
    "difficulty_preference": "начальный",
    "weekly_hours": 5
}

# Запуск рекомендательной системы
recommendations = recommend_courses(user_input, courses_db)

# Вывод результата
print("Рекомендуемые курсы:")
for course in recommendations:
    print(f"- {course['title']} ({course['workload_hours']} ч/нед)")