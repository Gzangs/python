def calculate_final_grade(scores) -> float:
    """
    Calculates the final grade as the mean
    """
    total_score = sum(scores)
    num_assignments = len(scores)
    mean_percentage = (total_score / (num_assignments * 100)) * 100
    return round(mean_percentage, 2)




