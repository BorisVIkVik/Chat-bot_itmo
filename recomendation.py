def recommend_courses(user_profile, courses_db):
    recommended = []
    
    for course in courses_db:
        # Проверка совпадения интересов
        interest_match = any(interest in course["category"] for interest in user_profile["interests"])
        
        # Проверка навыков
        skill_match = all(skill in user_profile["skills"] for skill in course["required_skills"])
        
        # Проверка уровня сложности
        difficulty_ok = (course["difficulty"] == user_profile["difficulty_preference"])
        
        # Проверка карьерных целей
        career_match = (user_profile["goals"] in course["career_relevance"])
        
        if interest_match and skill_match and difficulty_ok and career_match:
            recommended.append(course)
    
    # Фильтр по нагрузке
    recommended = [c for c in recommended if c["workload_hours"] <= user_profile["weekly_hours"]]
    
    # Сортировка по релевантности
    recommended.sort(key=lambda x: len(
        set(user_profile["interests"]) & set(x["category"].split(";"))
    , reverse=True))
    
    return recommended[:3]  # Топ-3 рекомендации