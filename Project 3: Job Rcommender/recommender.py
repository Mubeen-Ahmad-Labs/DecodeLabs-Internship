import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ==========================================
# AI TECH STACK RECOMMENDER
# DecodeLabs Internship - Project 3
# ==========================================


# ------------------------------------------
# STEP 1: Load Dataset
# ------------------------------------------

data = pd.read_csv("raw_skills.csv")


# ------------------------------------------
# STEP 2: Welcome Screen
# ------------------------------------------

print("=" * 60)
print("              AI TECH STACK RECOMMENDER")
print("=" * 60)

print("\nDataset loaded successfully!")
print(f"Total Job Roles: {len(data)}")


# ------------------------------------------
# STEP 3: Show Available Job Roles
# ------------------------------------------

print("\nAvailable Career Paths:")

for role in data["Job_Role"]:
    print(" -", role)


# ------------------------------------------
# STEP 4: Take User Skills
# ------------------------------------------

print("\n" + "=" * 60)
print("Enter your 3 skills or interests")
print("=" * 60)

skill1 = input("Skill 1: ").strip()
skill2 = input("Skill 2: ").strip()
skill3 = input("Skill 3: ").strip()


# Combine the user's skills
user_skills = f"{skill1}, {skill2}, {skill3}"


print("\nAnalyzing your skills...")


# ------------------------------------------
# STEP 5: Prepare Text
# ------------------------------------------

# Get skills of all job roles
job_skills = data["Skills"].fillna("").astype(str)

# Add user skills to the job skills temporarily
all_skills = list(job_skills) + [user_skills]


# ------------------------------------------
# STEP 6: TF-IDF Vectorization
# ------------------------------------------

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(all_skills)


# Job vectors
job_vectors = tfidf_matrix[:-1]

# User vector
user_vector = tfidf_matrix[-1]


# ------------------------------------------
# STEP 7: Cosine Similarity
# ------------------------------------------

similarity_scores = cosine_similarity(
    user_vector,
    job_vectors
).flatten()


# ------------------------------------------
# STEP 8: Add Similarity Scores
# ------------------------------------------

data["Similarity"] = similarity_scores


# ------------------------------------------
# STEP 9: Sort Recommendations
# ------------------------------------------

data = data.sort_values(
    by="Similarity",
    ascending=False
)


# ------------------------------------------
# STEP 10: Get Top 3
# ------------------------------------------

top_3 = data.head(3)


# ------------------------------------------
# STEP 11: Display Recommendations
# ------------------------------------------

print("\n")
print("=" * 60)
print("                TOP 3 RECOMMENDATIONS")
print("=" * 60)

for position, (_, row) in enumerate(top_3.iterrows(), start=1):

    role = row["Job_Role"]
    score = row["Similarity"] * 100

    print(f"\n{position}. {role}")
    print(f"   Match Score: {score:.2f}%")
    print(f"   Required Skills: {row['Skills']}")
    print("-" * 60)


# ------------------------------------------
# STEP 12: Finish
# ------------------------------------------

print("\nRecommendation process completed!")
print("=" * 60)