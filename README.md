# Movie Recommendation System using Streamlit

## Description
This project is a Movie Recommendation System that suggests similar movies based on a user's selection. It uses collaborative filtering and the MovieLens dataset to provide movie recommendations. The recommendations are generated using a cosine similarity matrix, and the user interface is built with Streamlit.

## Features
- **Movie Selection**: Users can select a movie from a dropdown menu.
- **Recommendation**: After selecting a movie and clicking the "Recommend" button, the system provides a list of recommended movies along with their posters.
- **Movie Posters**: The system fetches movie posters using the TMDb API to enhance the visual appeal of the recommendations.

## Technologies Used
- Python
- Streamlit: for building the user interface.
- Pandas: for data manipulation.
- Requests: for making API calls to fetch movie posters.
- Pickle: for loading precomputed similarity matrices and movie data.

## Data
The project uses the MovieLens dataset, which contains movie metadata and user ratings. A similarity matrix is precomputed to provide movie recommendations based on user-selected movies.

## How to Run
1. Clone this repository to your local machine.
2. Generate .pkl files by execution of complete *movie-recommender-system.ipynb* file in the same directory where *app.py* is located
3. Install the required Python packages: *pip install streamlit pandas requests*
4. Run the Streamlit app: *streamlit run app.py*
5. Access the web app in your browser by following the link provided in the terminal.

## Usage
1. Select a movie from the dropdown menu.
2. Click the "Recommend" button to get a list of movie recommendations.
3. View the recommended movies along with their posters.

## Acknowledgments
- [MovieLens](https://grouplens.org/datasets/movielens/): The dataset used for this project.

## Future Improvements
- Integration of additional recommendation algorithms for better results.
- User login and rating features to personalize recommendations.
- Enhanced frontend design and user experience improvements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
- Pooja Chaudhary
- poojaa15000@gmail.com

---
