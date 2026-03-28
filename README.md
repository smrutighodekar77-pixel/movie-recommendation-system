# 🎬 Movie Recommendation System

A **content-based movie recommendation system** built using multiple NLP and machine learning techniques. This project compares different algorithms and selects the best-performing model to generate accurate movie recommendations.

---

## 📌 Overview

This project focuses on recommending movies based on their **content similarity** such as:

* Genres
* Keywords
* Cast
* Director
* Overview (plot summary)

Three different approaches are implemented and compared:

1. **CountVectorizer + Cosine Similarity**
2. **TF-IDF + Cosine Similarity**
3. **K-Nearest Neighbors (KNN)**

After evaluation, the best model is selected for final deployment.

---

## 🧠 How It Works

1. **Data Preprocessing**

   * Handles missing values
   * Extracts relevant features
   * Converts JSON-like strings into lists
   * Combines features into a single "tags" column
   * Applies text normalization (lowercasing + stemming)

2. **Feature Engineering**

   * Text vectorization using:

     * CountVectorizer
     * TF-IDF Vectorizer

3. **Similarity Calculation**

   * Cosine similarity used to measure similarity between movies

4. **Model Comparison**

   * Recommendations generated using all three methods
   * Performance compared based on relevance

---

## 📂 Dataset

* File: `movie_dataset.csv`
* Features used:

  * `title`
  * `genres`
  * `keywords`
  * `cast`
  * `director`
  * `overview`

---

## ⚙️ Technologies Used

* Python 🐍
* Pandas & NumPy
* Scikit-learn
* NLTK (for stemming)
* Pickle (for model saving)

---

## 🚀 Models Implemented

### 1. CountVectorizer + Cosine Similarity

* Converts text into frequency vectors
* Simple and fast
* Less effective at capturing importance of words

---

### 2. TF-IDF + Cosine Similarity ✅ (Selected Model)

* Assigns importance to words
* Reduces impact of common words
* Produces more meaningful recommendations

---

### 3. K-Nearest Neighbors (KNN)

* Uses distance-based similarity
* Works well but computationally heavier

---

## 🏆 Final Model Selection

**Selected Model:** TF-IDF + Cosine Similarity

### ✅ Why?

* Better semantic understanding
* Handles word importance effectively
* Produces more relevant recommendations

---

## 📦 Project Structure

```
project/
│
├── data/
│   └── movie_dataset.csv
│
├── notebooks/
│   └── movie_recommendation_system.ipynb
│
├── outputs/
│   ├── movies.pkl
│   └── similarity.pkl
│
└── README.md
```

---

## 🔍 Example Usage

```python
recommend("Avatar")
```

### Sample Output:

```
['Titanic', 'Guardians of the Galaxy', 'John Carter', ...]
```

---

## 💾 Model Saving

The final model and processed data are saved using pickle:

```python
pickle.dump(new_df, open("../outputs/movies.pkl", "wb"))
pickle.dump(similarity_tfidf, open("../outputs/similarity.pkl", "wb"))
```

---

## 🧪 Testing Multiple Movies

You can test recommendations like this:

```python
test_movies = ["Avatar", "Batman Begins", "Interstellar"]

for movie in test_movies:
    print(recommend(movie))
```

---

## ⚠️ Limitations

* Only uses metadata (no user preferences)
* No collaborative filtering
* Dependent on dataset quality

---

## 🔮 Future Improvements

* Add collaborative filtering
* Build a web app (Streamlit / Flask)
* Use deep learning (e.g., embeddings)
* Incorporate user ratings

---

## 👨‍💻 Author

Developed as part of a machine learning/NLP project to explore recommendation systems.

---

## ⭐ If You Like This Project

Give it a ⭐ on GitHub and feel free to contribute!

---
