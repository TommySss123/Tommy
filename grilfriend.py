import streamlit as st

st.title("Slecet the racial of your grilfriend")
name=st.text_input("What is your name?")
racial=st.text_input("What is your racial?")
#Step 2
grilfirend=st.selectbox("Which racial for your grilfriend?",['China','The United States','Japan','South Korea'])
#Step 3
if st.button("Now select the racial !!!!"):
    if grilfirend =='China':
        st.write(f"Yo {name}.For {racial}'s people, this will be a good choice! 😂" )
    elif grilfirend =='The United States':
        st.write(f"Yo {name}.For {racial}'s people, it's hard for me to say that American girls are hard to satisfy. 🤏🏻")
    elif grilfirend =='Japan':
        st.write(f"Yo {name}. Are you sure you haven't met her before seeing her? 😶")
    elif grilfirend =="South Korea":
        st.write(f"{name},不是老弟你选上韩圈啦？真的逆天")
else:
    st.write("Please click the button to select your grilfriend!!!")