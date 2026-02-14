# Filename: 02_elif_letter_grades.py
# Python101 - Week 3: if / elif / else (multiple choices)

print("=== Letter Grade Calculator ===")

score = int(input("Enter a score from 0 to 100: "))

if score < 0 or score > 100:
    print("Invalid score. It must be between 0 and 100.")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

print()
print("Done.")

# Teaching notes:
# - elif means "else if" (check another condition)
# - Order matters: we check biggest scores first
# - 'or' means either condition can be True
