
print("================================")
print("       SMART STUDY PLANNER")
print("================================")

name = input("What is your name? ")
subject = input("Which subject do you want to study? ")
chapter = input("Which chapter do you want to study? ")
print("\nChoose the difficulty level:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

difficulty = input("Enter your choice (1/2/3): ")

if difficulty == "1":
    priority = "Low"
    study_time = 30
elif difficulty == "2":
    priority = "Medium"
    study_time = 60
elif difficulty == "3":
    priority = "High"
    study_time = 90
else:
    priority = "Invalid choice"
    study_time = 0

print("\n========== YOUR STUDY PLAN ==========")
print("Student:", name)
print("Subject:", subject)
print("Chapter:", chapter)
print("Priority:", priority)
print("Suggested study time:", study_time, "minutes")
print("=====================================")
