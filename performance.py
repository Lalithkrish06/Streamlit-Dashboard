def calculate_weighted_score(marks, weights):
    total = 0
    for subject in marks:
        total += marks[subject] * weights.get(subject, 0)
    return round(total, 2)


def predict_improvement(current_mark, improvement):
    new_mark = current_mark + improvement
    if new_mark > 100:
        new_mark = 100
    return new_mark