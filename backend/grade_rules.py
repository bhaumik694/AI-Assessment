grade_rules = {
    "1-3": "Use very simple words, basic concepts, no abstract thinking.",
    "4-5": "Introduce basic concepts with simple examples. Avoid complex reasoning.",
    "6-7": "Moderate complexity. Include reasoning but keep it simple.",
    "8-9": "More abstract thinking. Include problem solving and multi-step reasoning.",
    "10": "Advanced explanations, deeper concepts, real-world applications."
}


def get_grade_rule(grade):
    if grade <= 3:
        return grade_rules["1-3"]
    elif grade <= 5:
        return grade_rules["4-5"]
    elif grade <= 7:
        return grade_rules["6-7"]
    elif grade <= 9:
        return grade_rules["8-9"]
    else:
        return grade_rules["10"]