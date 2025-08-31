# Music Recommendation System Project 🎵

## Project Overview

This repository contains the implementation of a Music Recommendation System. The project aims to predict songs a user might enjoy by analyzing their historical listening data. The core of the system is a **Collaborative Filtering** model built using the **Singular Value Decomposition (SVD)** algorithm.

The final product is a simple but functional real-time web API built with **Flask** that serves song recommendations on demand.

---

## Features

-   **Data Processing:** Loads and processes a subset of the Million Song Dataset.
-   **Model Training:** Implements the SVD algorithm using the `scikit-surprise` library to learn user and song patterns.
-   **Model Persistence:** The trained model is saved to a file (`.pkl`) so it can be loaded instantly without retraining.
-   **Real-Time API:** A Flask web server loads the model and provides song recommendations for any user ID via a simple API endpoint.

---

## Technology Stack

-   **Language:** Python 3
-   **Libraries:**
    -   **Pandas:** For data manipulation and analysis.
    -   **Scikit-Surprise:** For building and evaluating the recommendation algorithm.
    -   **Flask:** For creating and serving the web API.
-   **Environment:** Conda and Jupyter Notebook

---

## How It Works

1.  **Data Loading:** The system starts with the 'Echo Nest Taste Profile Subset' from the Million Song Dataset, which contains `user_id`, `song_id`, and `play_count`.
2.  **Model Training:** An SVD model is trained on this data. SVD is a matrix factorization technique that uncovers latent factors connecting users and songs, allowing it to predict a user's affinity for a song they've never heard.
3.  **API Deployment:** The trained model is saved and then loaded by a Flask application. The app exposes an API endpoint `/recommend/<user_id>` that, when called, uses the model to generate the top 10 song recommendations for the specified user and returns them in a clean JSON format.

---

## Setup and Usage

Follow these steps to set up and run the project locally.

### Prerequisites

-   Anaconda or Miniconda installed.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
    cd YOUR_REPOSITORY_NAME
    ```

2.  **Create and activate the Conda environment:**
    ```bash
    conda create -n music-rec python=3.11
    conda activate music-rec
    ```

3.  **Install the required libraries:**
    ```bash
    conda install -c conda-forge scikit-surprise pandas jupyter flask
    ```

4.  **Download the Data:**
    This repository does not include the large data files. You will need to download them and place them in the project's root folder.
    -   `train_triplets.txt`: Download from [The Echo Nest Taste Profile Subset](https://labrosa.ee.columbia.edu/millionsong/tasteprofile).

### Running the API

1.  Make sure you are in the project's root directory and your `music-rec` conda environment is active.
2.  Start the Flask server with the following command:
    ```bash
    python app.py
    ```
3.  The server will start and run on `http://127.0.0.1:8080`.

### Getting Recommendations

-   Open your web browser and go to the following URL to get recommendations for a sample user:
    ```
    [http://127.0.0.1:8080/recommend/00014a7610283ee9c340f7b99708919a278ba2f3](http://127.0.0.1:8080/recommend/00014a7610283ee9c340f7b99708919a278ba2f3)
    ```
-   You will receive a JSON response containing the top 10 recommended `song_id`s.
