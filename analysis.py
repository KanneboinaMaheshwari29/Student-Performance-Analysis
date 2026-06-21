import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/StudentsPerformance.csv")

print("\n===== DATASET OVERVIEW =====")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

# Average scores
math_avg = df["math score"].mean()
reading_avg = df["reading score"].mean()
writing_avg = df["writing score"].mean()

print("\n===== AVERAGE SCORES =====")
print(f"Math Average: {math_avg:.2f}")
print(f"Reading Average: {reading_avg:.2f}")
print(f"Writing Average: {writing_avg:.2f}")

# Gender-wise average scores
gender_scores = df.groupby("gender")[["math score", "reading score", "writing score"]].mean()

print("\n===== GENDER WISE PERFORMANCE =====")
print(gender_scores)

# Test preparation impact
test_prep = df.groupby("test preparation course")[["math score", "reading score", "writing score"]].mean()

print("\n===== TEST PREPARATION IMPACT =====")
print(test_prep)

# Chart 1: Subject Average Scores
subject_avg = [math_avg, reading_avg, writing_avg]
subjects = ["Math", "Reading", "Writing"]

plt.figure(figsize=(6,4))
plt.bar(subjects, subject_avg)
plt.title("Average Scores by Subject")
plt.ylabel("Average Marks")
plt.savefig("charts/subject_average.png")
plt.show()

# Chart 2: Gender Performance
gender_scores.plot(kind="bar", figsize=(8,5))
plt.title("Gender-wise Average Scores")
plt.ylabel("Average Marks")
plt.savefig("charts/gender_performance.png")
plt.show()

# Chart 3: Test Preparation Impact
test_prep.plot(kind="bar", figsize=(8,5))
plt.title("Impact of Test Preparation Course")
plt.ylabel("Average Marks")
plt.savefig("charts/test_prep_impact.png")
plt.show()

# Chart 4: Math Score Distribution
plt.figure(figsize=(7,4))
plt.hist(df["math score"], bins=10)
plt.title("Math Score Distribution")
plt.xlabel("Math Score")
plt.ylabel("Number of Students")
plt.savefig("charts/math_distribution.png")
plt.show()

print("\nProject Completed Successfully!")