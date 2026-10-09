# 🧠 Personality Quest

A machine-learning-powered personality prediction web app built with
**Python, Scikit-learn, Logistic Regression, and Streamlit**. Users
answer a set of questions about their habits and preferences, and the
app predicts one of three personality categories.

```{=html}
<p align="center">
```
`<a href="https://personality-quest.streamlit.app/">`{=html}`<strong>`{=html}🚀
Try Personality Quest Live`</strong>`{=html}`</a>`{=html}
```{=html}
</p>
```
## 🔗 Project Links

-   **Live app:** https://personality-quest.streamlit.app/
-   **GitHub repository:**
    https://github.com/Mr-shivam-001/personality-quest

## ✨ Features

-   Interactive questionnaire built with Streamlit.
-   Predicts one of three personality categories: **Ambivert, Extrovert,
    or Introvert**.
-   Uses a trained Logistic Regression model.
-   Applies the saved scaler before making predictions.
-   Displays prediction results and personality information.
-   Deployed on Streamlit Community Cloud.

## 🧠 Machine Learning Model

  -----------------------------------------------------------------------
  Item                                Details
  ----------------------------------- -----------------------------------
  Problem type                        Multi-class classification

  Algorithm                           Logistic Regression

  Model library                       Scikit-learn

  Input preprocessing                 Saved scaler, applied before
                                      prediction

  Output classes                      Ambivert, Extrovert, Introvert

  Reported accuracy                   **99.75%** (as measured in the
                                      project's local evaluation;
                                      evaluation setup should be
                                      documented in the training
                                      notebook)

  Saved artifact                      `personality_model.joblib`
  -----------------------------------------------------------------------

### How prediction works

1.  The app collects the user's questionnaire answers.
2.  Answers are arranged into a DataFrame using the same feature order
    used during model training.
3.  The saved scaler transforms the inputs.
4.  The trained Logistic Regression model predicts a class.
5.  The app maps the predicted class to a personality label and presents
    the result.

**Important:** The scaler and feature order are part of the model
pipeline. Inputs must use the same 26 features, in the same order, as
the trained model.

### Model input features

The app uses these 26 features:

1.  `social_energy`
2.  `alone_time_preference`
3.  `talkativeness`
4.  `deep_reflection`
5.  `group_comfort`
6.  `party_liking`
7.  `listening_skill`
8.  `empathy`
9.  `organization`
10. `leadership`
11. `risk_taking`
12. `public_speaking_comfort`
13. `curiosity`
14. `routine_preference`
15. `excitement_seeking`
16. `friendliness`
17. `planning`
18. `spontaneity`
19. `adventurousness`
20. `reading_habit`
21. `sports_interest`
22. `online_social_usage`
23. `travel_desire`
24. `gadget_usage`
25. `work_style_collaborative`
26. `decision_speed`

The target column is `personality_type`. The training features excluded
`creativity`, `emotional_stability`, and `stress_handling`, along with
the target column.

### Personality categories

-   **⚖️ Ambivert --- The Balance Seeker:** may enjoy social
    interactions while also valuing alone time.
-   **🎉 Extrovert --- The Social Energizer:** tends to enjoy social
    interaction and group activities.
-   **🌙 Introvert --- The Quiet Thinker:** tends to appreciate quieter
    environments and time to reflect.

These descriptions are general summaries, not psychological assessments
or diagnoses.

## 🗂️ Project Structure

The deployed app uses the following core files:

``` text
personality-quest/
├── app.py
├── requirements.txt
├── personality_model.joblib
├── README.md
└── notebooks/
    ├── personality_model_training.ipynb
    └── requirements.txt
```

The `notebooks/personality_model_training.ipynb` file is a suggested
location/name. Add your actual model-training notebook there; it is not
included automatically just because the saved model artifact is in the
repository.

## 🛠️ Tech Stack

-   Python
-   Streamlit
-   Scikit-learn
-   Pandas
-   Joblib
-   Jupyter Notebook

## ▶️ Run Locally

### 1. Clone the repository

``` bash
git clone https://github.com/Mr-shivam-001/personality-quest.git
cd personality-quest
```

### 2. Create and activate a virtual environment (recommended)

**Windows PowerShell:**

``` powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

``` bash
python -m pip install -r requirements.txt
```

### 4. Run the Streamlit app

``` bash
python -m streamlit run app.py
```

Streamlit will print a local URL in the terminal, usually
`http://localhost:8501`.

## 📓 Add the Model Training Notebook

To include the original `.ipynb` file that contains your training
workflow:

1.  Find the notebook you used to train and evaluate the Logistic
    Regression model.
2.  In the project folder, create a folder named `notebooks` if it does
    not already exist.
3.  Copy your original notebook into it and name it
    `personality_model_training.ipynb` (or update the filename in this
    README).
4.  Open the notebook and remove private information, local absolute
    paths, credentials, and unnecessary output cells before publishing.
5.  Save it, then run:

``` powershell
git add README.md notebooks/personality_model_training.ipynb
git commit -m "Add project documentation and ML notebook"
git push
```

If you add the notebook in a different location or use a different
filename, update the path in this README accordingly.

## 📦 Dependencies

The exact package versions should remain compatible with the saved model
artifact. Check `requirements.txt` for the versions used by the deployed
app. Loading a Joblib model trained with a different Scikit-learn
version can cause compatibility warnings or errors.

## ⚠️ Notes and Limitations

-   The reported accuracy of 99.775% comes from the project's local
    evaluation. Check the training notebook for the dataset split,
    evaluation method, and whether the test set was kept separate from
    training.
-   Model predictions depend on the dataset, feature definitions,
    preprocessing, and training process.
-   This project is for learning and demonstration; it should not be
    treated as a validated psychological test.
-   Only load `.joblib` files from trusted sources. Joblib-based model
    files can execute code when loaded.
-   If the GitHub repository is public, the code and saved model
    artifact are publicly accessible.

## 👤 Author

**Shivam Kumar**

Built as a machine-learning project to practice model training,
preprocessing, prediction, and deployment with Streamlit.

------------------------------------------------------------------------

⭐ If you find this project useful, feel free to explore the code and
try the live app.
