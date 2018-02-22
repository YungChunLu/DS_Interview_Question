# Q1: Write a function to calculate all possible assignment vectors of 2n users,
# where n users are assigned to group 0 (control),
# and n users are assigned to group 1 (treatment).
def make_choices(n, k, choices=[""]):
    if k == 0:
        return [choice + "0" * n for choice in choices]
    elif n == k:
        return [choice + "1" * n for choice in choices]
    else:
        return make_choices(n-1, k, [choice+"0" for choice in choices]) + make_choices(n-1, k-1, [choice+"1" for choice in choices])

def complement(assignment):
    return "".join("1" if b == "0" else "0" for b in assignment)

def make_assignments(n):
    choices_cached = {}
    assignments = []
    for k in range(n):
        for first_choice in make_choices(n-1, k):
            if k not in choices_cached:
                choices_cached[k] = make_choices(n, n-k)
            for second_choice in choices_cached[k]:
                assignments.append("0"+first_choice+second_choice)
    return assignments + [complement(assignment) for assignment in assignments]

if __name__ == "__main__":
    for n in range(1, 10):
        print(len(make_assignments(n)))