import streamlit as st

# Function to check password strength
def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.isupper() for char in password) and any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in "!@#$%^&*" for char in password):
        score += 1

    return score

# Main function for the app
def main():
    st.title("Password Strength Checker")
    st.write("Enter your password to check its strength.")
    
    password = st.text_input("Password:", type="password")
    
    if password:
        score = check_strength(password)
        
        if score == 4:
            st.success("Strong Password! 👍")
        elif score == 3:
            st.warning("Moderate Password. Can be improved. ⚠️")
        else:
            st.error("Weak Password. Try adding more variety! ❌")
        
        st.write(f"Score: {score}/4")

if __name__ == "__main__":
    main()
