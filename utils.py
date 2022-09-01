import json


def load_candidates():
    with open('candidates.json', encoding='utf-8') as file:
        candidates = json.load(file)
    return candidates


def get_all():
    load_candidates()
    everyone = ""
    for candidate in load_candidates():
        c_name = candidate['name']
        c_position = candidate['position']
        c_skills = candidate['skills']
        everyone += f"<pre>Имя кандидата - {c_name}\n" \
                    f"Позиция кандидата - {c_position}\n" \
                    f"Навыки через запятую - {c_skills}\n </pre>"
    return everyone


def get_by_pk(pk):
    load_candidates()
    candidate_ = "Not Found"
    for candidate in load_candidates():
        c_name = candidate['name']
        c_position = candidate['position']
        c_skills = candidate['skills']
        url = candidate['picture']
        if pk == candidate['pk']:
            candidate_ = ""
            candidate_ += f"<img src='{url}'>" \
                          f"<pre>Имя кандидата - {c_name}\n" \
                          f"Позиция кандидата - {c_position}\n" \
                          f"Навыки через запятую - {c_skills}\n </pre>"
    return candidate_


def get_by_skill(skill_name):
    load_candidates()
    candidates_ = ""
    for candidate in load_candidates():
        c_name = candidate['name']
        c_position = candidate['position']
        c_skills = candidate['skills']
        split_skills = candidate['skills'].lower().split(', ')
        if skill_name in split_skills:
            candidates_ += f"<pre>Имя кандидата - {c_name}\n" \
                           f"Позиция кандидата - {c_position}\n" \
                           f"Навыки через запятую - {c_skills}\n </pre>"
    return candidates_

