# Cricket Match Outcome Prediction System

[Live Demo](https://cricket-minor-major-prediction-system.streamlit.app/)

## Table of Contents
- [Project Overview](#project-overview)
- [Business Objective](#business-objective)
- [Model Importance](#model-importance)
- [Accuracy and Performance](#accuracy-and-performance)
- [Future Objectives](#future-objectives)
- [Outcome and Impact](#outcome-and-impact)
- [How to Use the App](#how-to-use-the-app)
- [Acknowledgements](#acknowledgements)

## Project Overview
This project is a **Cricket Match Outcome Prediction System** that utilizes a Random Forest model to predict the outcome of a cricket match based on real-time match data. The system allows users to input parameters related to the batting team, bowling team, match location, runs left, balls left, wickets, target score, and other relevant statistics. With this information, the model calculates the probability of the batting team winning or losing the match.

## Business Objective
The aim of this model is to:
- **Enhance fan engagement** by allowing viewers to simulate possible outcomes based on the current match conditions.
- **Support betting platforms** by providing real-time probability scores, enhancing decision-making during live matches.
- **Assist sports analysts** with predictive insights that add value to their commentary and analysis during cricket matches.

## Model Importance
This model leverages match data, including team performance, city-specific conditions, and other live parameters, to provide an accurate prediction of match outcomes. The insights it provides are valuable for:
- **Sports fans** who want to engage deeper with the game.
- **Analysts and commentators** who require real-time analytics to supplement live commentary.
- **Data-driven decisions** in betting and sports media.

## Accuracy and Performance
The model was trained using historical cricket match data and achieved an impressive accuracy of **99.68%**, indicating highly reliable predictions.
![Screenshot 2024-11-06 222232](https://github.com/user-attachments/assets/56773ecf-ed66-4ecc-a708-8b0c46deee58)

![Screenshot 2024-11-06 222221](https://github.com/user-attachments/assets/b47ac2cb-d67f-4ae8-abbd-0c0b3cce3784)

## Future Objectives
- **Real-time Data Integration**: Integrate with APIs to update match data in real-time.
- **Improved Models**: Experiment with additional ensemble models or deep learning architectures.
- **Mobile Compatibility**: Develop a mobile app to extend accessibility and reach more users.
- **Interactive Visualization**: Incorporate data visualizations to better showcase winning and losing probabilities.

## Outcome and Impact
By accurately predicting match outcomes, this system provides:
- A **predictive tool** for cricket enthusiasts and analysts.
- **Increased fan engagement** through interactive, data-driven content.
- **Enhanced decision-making** capabilities in sports media and betting platforms.

## How to Use the App
1. **Select the Batting Team** and **Bowling Team** from the dropdown options.
2. **Choose the City** where the match is taking place.
3. Enter the match conditions such as:
   - **Runs Left**: Total runs remaining for the batting team to win.
   - **Balls Left**: Number of balls left to reach the target.
   - **Wickets in Hand**: Wickets remaining with the batting team.
   - **Target Score**: Target score to be achieved.
   - **Current Run Rate (CRR)** and **Required Run Rate (RRR)**.
4. Click **Predict Outcome** to get the **Win Probability** and **Lose Probability** for the batting team.
![Screenshot 2024-11-06 222356](https://github.com/user-attachments/assets/04600713-4084-494f-9817-8cdf0a19eb73)
![Screenshot 2024-11-06 222436](https://github.com/user-attachments/assets/8aa9acd9-089f-488d-abe4-2c673e9a7daa)

1. **Clone the Repository**:  
   Open your terminal and use the following command:
   ```bash
   git clone https://github.com/SUMIT2001GO/Cricket-Minor-Major-Prediction-System.git

## Acknowledgements
We would like to acknowledge the following libraries and tools used in this project:

- **Scikit-learn**: For implementing the Random Forest model and data preprocessing.
- **Pandas**: For data manipulation and handling large datasets.
- **NumPy**: For numerical operations during data processing.
- **Streamlit**: For providing a framework to create the interactive web application.
- **Joblib**: For saving and loading the trained machine learning models.
- **Seaborn and Matplotlib**: For data visualization and analysis.
- **GitHub**: For hosting the project, version control, and collaboration.

---
