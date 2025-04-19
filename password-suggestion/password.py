import streamlit as st
import re

# Function to evaluate password strength
def password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    if score == 4:
        score += 1
    return score

# Function to generate feedback
def feedback(password, score):
    feedback_messages = []
    if score <= 2:
        feedback_messages.append("Password Strength: Weak")
        if len(password) < 8:
            feedback_messages.append("- Increase the length to at least 8 characters.")
        if not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password):
            feedback_messages.append("- Add both uppercase and lowercase letters.")
        if not re.search(r"\d", password):
            feedback_messages.append("- Include at least one digit (0-9).")
        if not re.search(r"[!@#$%^&*]", password):
            feedback_messages.append("- Include at least one special character (!@#$%^&*).")
    elif score == 3 or score == 4:
        feedback_messages.append("Password Strength: Moderate")
        if len(password) < 8:
            feedback_messages.append("- Increase the length to at least 8 characters.")
        if not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password):
            feedback_messages.append("- Add both uppercase and lowercase letters.")
        if not re.search(r"\d", password):
            feedback_messages.append("- Include at least one digit (0-9).")
        if not re.search(r"[!@#$%^&*]", password):
            feedback_messages.append("- Include at least one special character (!@#$%^&*).")
    else:
        feedback_messages.append("Password Strength: Strong")
        feedback_messages.append("Great job! Your password meets all security criteria.")
    return feedback_messages

# Streamlit App
def main():
    st.title("🔐 Password Strength Meter")
    st.write("Analyze the strength of your password and get feedback to improve it.")
    
    password = st.text_input("Enter your password:", type="password")
    
    if password:
        score = password_strength(password)
        feedback_messages = feedback(password, score)
        
        st.subheader("Password Analysis")
        for message in feedback_messages:
            st.write(message)

if __name__ == "__main__":
    main()
