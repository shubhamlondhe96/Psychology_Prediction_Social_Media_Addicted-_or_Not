import streamlit as st
import joblib
import pandas as pd
import os
os.getcwd()


model = joblib.load("Catboost_new.pkl")



#st.markdown(f'''<center><h2>AIS Solutions Pvt. Ltd, Pune</h2></center>''', unsafe_allow_html = True)

#st.markdown(f'''<center><h1>Psychology Prediction Social Media Addicted or Not</h1></center>''', unsafe_allow_html = True)


st.markdown(f'''<center><h1 style="font-family:cursive;color:rgb(0,250,200);text-decoration-line:overline underline;text-decoration-style:double ;">AIS Solutions Pvt Ltd.</h1></center>''',unsafe_allow_html=True)
st.markdown(f'''<center><h1 style="background-color:DodgerBlue ;">Psychology Prediction Social Media Addicted or Not</h1><center>''',unsafe_allow_html=True)
# upload file where you have to test 




Age = st.slider("Age", 0, 44,40)


Gender = st.slider("Gender", 0, 2,1)


data = pd.read_csv("C:\\Users\\Shubham\\Desktop\\AIS Solution Pvt Ltd. Pune\\Project 3\\dataset.csv")


C = data['Country'].unique()

C1 = st.sidebar.selectbox("Select Country", C.tolist())


Country = C.tolist().index(C1)




work_interfere = st.slider("work_interfere", 0, 4,4)



no_employees = st.slider("no_employees", 0, 5,4)



benefits = st.slider("benefits", 0, 2,2)




care_options = st.slider("care_options", 0, 2,2)





leave = st.slider("leave", 0, 4,3)



mental_health_consequence = st.slider("mental_health_consequence", 0, 2,2)



phys_health_consequence = st.slider("phys_health_consequence", 0, 2,2)




coworkers = st.slider("coworkers", 0, 2,2)



supervisor = st.slider("supervisor", 0, 2,2)








phys_health_interview = st.slider("phys_health_interview", 0, 2,2)








st.write("Select below option if response is Yes (or 1) ")






a2 = st.checkbox("family_history")

if a2:
	family_history = 1
else:
	family_history = 0





























lst = [work_interfere,
 Age,
 Country,
 no_employees,
 leave,
 family_history,
 coworkers,
 care_options,
 benefits,
 phys_health_interview,
 mental_health_consequence,
 supervisor]







if st.button("Predict"):
	x = model.predict([lst])[0]
	if x==1:
		st.header('ADDICTED')
	else:
		st.header('NOT ADDICTED')
