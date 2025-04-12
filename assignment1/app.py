import streamlit as st
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Streamlit interface
def rock_paper_scissors():
    st.title("Rock, Paper, Scissors Game")
    
    # Instructions
    st.write("Choose Rock, Paper, or Scissors to play against the computer.")
    
    # User choice
    user_choice = st.radio("Choose your move", ('rock', 'paper', 'scissors'), index=0)  
    
    # Button to submit the choice
    if st.button("Play"):
        # Computer choice
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        
        # Display choices
        st.write(f"You chose: {user_choice}")
        st.write(f"Computer chose: {computer_choice}")
        
        # Determine winner
        result = determine_winner(user_choice, computer_choice)
        st.write(result)

# Run the game
rock_paper_scissors()
