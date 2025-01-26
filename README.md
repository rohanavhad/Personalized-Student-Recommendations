# 📊 Personalized Student Quiz Performance Analysis

## 📌 Project Overview
This project analyzes **student quiz performance** using **historical quiz data** and **latest quiz attempts** to generate **personalized recommendations** for improvement. The system tracks **accuracy trends, weak topics, difficulty-based performance, and time management** to help students focus on areas that need improvement.

## 🎯 Features
- **📈 Analyze Performance Trends**: Tracks accuracy, score trends, and mistakes over multiple quizzes.
- **📚 Identify Weak & Strong Topics**: Detects subjects where the student performs well or struggles.
- **⏳ Time Management Analysis**: Determines if the student is rushing or taking too long.
- **🎯 Difficulty Level Performance**: Assesses performance on easy, medium, and hard questions.
- **🤖 Personalized Recommendations**: Provides **study plans and improvement strategies** based on data.


---

## 🗂 Dataset Information
This project uses **three datasets**:

1. **Current Quiz Data (`QuizEndpoint.json`)**
   - Contains the latest quiz submission.
   - Includes **questions, topics, and student responses**.

2. **Historical Quiz Data (`APIEndpoint.json`)**
   - Stores **past 5 quiz performances** per user.
   - Includes **score, accuracy, correct/incorrect answers**.

3. **User-Specific Quiz Data (`user_quiz_data.json`)**
   - Represents **a single quiz attempt** with **detailed mistake tracking**.

---
**Performance Over Time**


![image](https://github.com/user-attachments/assets/c5452626-0d86-41d9-8050-e03998b3b822)




📌 Performance by Difficulty Level:
   quiz  correct_answers  incorrect_answers  total_attempts  accuracy
0  Hard              20                 15              35      57.1%
1  Medium            40                 10              50      80.0%
2  Easy              50                  5              55      90.9%

⚠ Struggling with hard questions - focus on difficult practice sets!


