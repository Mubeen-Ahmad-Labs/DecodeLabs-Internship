AI Recommendation Logic

A content-based AI recommendation system developed using Python as part of my Artificial Intelligence Internship at DecodeLabs.

📌 Description

This project recommends the Top 3 career paths based on the skills and interests entered by the user.

The system compares the user's skills with the skills associated with different career roles in the dataset. It uses TF-IDF Vectorization and Cosine Similarity to calculate how closely the user's skills match each career path.

🚀 Features
Accepts 3 skills/interests from the user
Loads career and skill information from a CSV dataset
Converts text skills into numerical vectors using TF-IDF
Calculates similarity using Cosine Similarity
Ranks career paths based on similarity scores
Displays the Top 3 career recommendations
Displays a match percentage for each recommendation
🛠️ Technologies Used
Python
Pandas
Scikit-learn
TF-IDF Vectorization
Cosine Similarity
📂 Files
recommender.py
raw_skills.csv
README.md
recommender.py

Contains the complete recommendation system.

raw_skills.csv

Contains career roles and their associated technical skills.

The dataset uses two columns:

Job_Role
Skills
⚙️ How It Works
User enters 3 skills
        ↓
Load career dataset
        ↓
TF-IDF Vectorization
        ↓
Convert skills into numerical vectors
        ↓
Calculate Cosine Similarity
        ↓
Calculate similarity scores
        ↓
Sort career paths
        ↓
Select Top 3
        ↓
Display recommendations
🧮 Recommendation Logic
1. TF-IDF

TF-IDF is used to convert the text-based skills into numerical representations that can be compared.

2. Cosine Similarity

Cosine Similarity compares the user's skill vector with the skill vector of each career path.

A higher similarity score means the career path has a stronger match with the user's entered skills.

3. Ranking

After calculating the similarity scores, the career paths are sorted from highest to lowest score.

The system then selects the Top 3 recommendations.

▶️ How to Run

Install the required libraries:

pip install pandas scikit-learn

Make sure both files are in the same folder:

Project-3-AI-Recommendation-Logic/
│
├── recommender.py
├── raw_skills.csv
└── README.md

Run the program:

python recommender.py
💻 Example Input
Skill 1: Python
Skill 2: Machine Learning
Skill 3: Deep Learning
📊 Example Output
============================================================
                TOP 3 RECOMMENDATIONS
============================================================

1. AI Engineer
   Match Score: XX.XX%

2. NLP Engineer
   Match Score: XX.XX%

3. Machine Learning Engineer
   Match Score: XX.XX%

============================================================
Recommendation process completed!
============================================================

The actual match scores depend on the skills entered by the user.

📚 Learning Outcomes

Through this project, I gained practical experience with:

Content-based recommendation systems
TF-IDF Vectorization
Cosine Similarity
Data processing with Pandas
Working with CSV datasets
Ranking and filtering recommendations
Applying machine learning concepts to a practical problem
👨‍💻 Internship

Artificial Intelligence Internship — DecodeLabs

This project was developed as part of my practical learning journey during my AI internship.

⭐ More improvements and projects will be added as I continue learning and developing my AI skills.
