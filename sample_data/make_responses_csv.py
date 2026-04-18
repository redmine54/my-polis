import csv
import random
n_users=1000
n_feaures=10
with open(f"responses_{n_users}x{n_feaures}.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["user_id", "question_id", "answer"])
    for i in range(1, n_users+1):
        for q in range(1, n_feaures+1):
            writer.writerow([f"u{i}", f"Q{q}", random.choice([1, 0, -1])])
