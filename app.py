from flask import Flask, jsonify, request
import pickle
import pandas as pd

# --- Create the Flask App ---
app = Flask(__name__)

# --- Load Model and Data ---
print("Loading the recommendation model and data...")

# Load the saved SVD model
with open('music_recommender_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the dataset to get a list of all songs and users
column_names = ['user_id', 'song_id', 'play_count']
df = pd.read_csv('train_triplets.txt', 
                 sep='\t', 
                 header=None, 
                 names=column_names, 
                 nrows=1000000)

# Create a set of all unique song IDs for generating recommendations
all_song_ids = set(df['song_id'].unique())
print("Model and data loaded successfully.")


# --- Define the API Endpoint ---
@app.route("/recommend/<string:user_id>", methods=['GET'])
def get_recommendations(user_id):
    print(f"Received request for user_id: {user_id}")

    try:
        # Get the list of songs the user has already listened to
        listened_song_ids = set(df[df['user_id'] == user_id]['song_id'])
        
        # Create a list of songs the user has NOT listened to
        unheard_songs = all_song_ids - listened_song_ids
        
        # Predict scores for the unheard songs
        predictions = []
        for song_id in unheard_songs:
            predicted_score = model.predict(uid=user_id, iid=song_id).est
            predictions.append((song_id, predicted_score))
            
        # Sort the predictions and get the top 10
        recommendations_df = pd.DataFrame(predictions, columns=['song_id', 'predicted_score'])
        top_10_recommendations = recommendations_df.sort_values(by='predicted_score', ascending=False).head(10)
        
        # Get just the list of song IDs
        recommended_songs = top_10_recommendations['song_id'].tolist()
        
        # Return the recommendations as a JSON response
        return jsonify({"user_id": user_id, "recommended_songs": recommended_songs})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- Run the App ---
if __name__ == '__main__':
    app.run(debug=True, port=8080)