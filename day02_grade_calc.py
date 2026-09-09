name = input("Enter your name ")
score1 = input("Enter your score in English:")
score2 = input("Enter your score in Nepali:")
score3 = input("Enter your score in Science:")

print(f"""
student : {name}
scores: {score1}, {score2}, {score3}
Average: {(float(score1) + float(score2) + float(score3)) / 3:.1f}
""")