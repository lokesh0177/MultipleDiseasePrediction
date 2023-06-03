import pickle
import streamlit as st
from streamlit_option_menu import option_menu
#loading the saved model 

diabetes_model = pickle.load(open('C:/Users/lokes/OneDrive/Desktop/Multiple disease prediction system/Model/diabates_model.sav','rb'))
heart_disease_model = pickle.load(open('C:/Users/lokes/OneDrive/Desktop/Multiple disease prediction system/Model/heart_model.sav','rb'))
breast_cancer_model = pickle.load(open('C:/Users/lokes/OneDrive/Desktop/Multiple disease prediction system/Model/breast_cancer.sav','rb'))

#sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple disease Prediction system', 
                           ['Diabetes prediction',
                             'Heart Disease Prediction',
                             'Breast Cancer'
                            
                            ],
                           default_index=0,
                           icons=['activity']
                           
                        )
    
    
#Diabetes Prediction Page

if (selected == 'Diabetes prediction'):
    
    
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
  
    with col2:
        Glucose = st.text_input('Glucose Level')
  
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
  
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
  
    with col2:
        Insulin = st.text_input('Insulin Level')
  
    with col3:
        BMI = st.text_input('BMI value')
  
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
  
    with col2:
        Age = st.text_input('Age of the Person')
        
        
        #code for prediction
        
        diab_dignosis = ''
        
        # creating a button for prediction 
        
        if st.button('Diabetes test Result'):
            diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
            
            if diab_prediction[0] == 1:
                diab_dignosis = 'The person is Diabetic'
            else:
                diab_dignosis = 'The person is Not Diabetic'
                
        st.success(diab_dignosis)
        
        
if (selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction using ML')
    
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("Age")
        
    with col2:
        sex = st.number_input("Sex")
        
    with col3:
        cp = st.number_input("Chest Pain Types")
        
    with col1:
        trestbps = st.number_input("Resting Blood Pressure")
        
    with col2:
        chol = st.number_input("Serum Cholestoral in mg/dl")
        
    with col3:
        fbs = st.number_input("Fasting Blood Sugar > 120 mg/dl")
        
    with col1:
        restecg = st.number_input("Resting Electrocardiographic Results")
        
    with col2:
        thalach = st.number_input("Maximum Heart Rate Achieved")
        
    with col3:
        exang = st.number_input("Exercise Induced Angina")
        
    with col1:
        oldpeak = st.number_input("ST Depression induced by Exercise")
        
    with col2:
        slope = st.number_input("Slope of the peak exercise ST Segment")
        
    with col3:
        ca = st.number_input("Major vessels colored by Flourosopy")
        
    with col1:
        thal = st.number_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect")
        
        
     
     
    # code for Prediction
    heart_diagnosis = " "
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 0):
          heart_diagnosis = "Hurrah! Your Heart is Good."
        else:
          heart_diagnosis = "Sorry! You have Heart Problem."
        
    st.success(heart_diagnosis)
        

if(selected == 'Breast Cancer'):  
    st.title('Breast Cancer Prediction using ML')
    # getting the input data from the user
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        radius_mean = st.number_input('Radius_mean')
       
        
    with col2:
        texture_mean = st.number_input('Texture_mean')
       
    
    with col3:
        perimeter_mean = st.number_input('Perimeter_mean')
        

    with col4:
        area_mean = st.number_input('Area_mean')
    
    
    with col5:
        smoothness_mean = st.number_input('Smoothness_mean')
        
        
    with col1:
        compactness_mean = st.number_input('Compactness_mean')
        
        
    with col2:
        concavity_mean = st.number_input('concavity_mean')
        
        
    with col3:
        concave_points_mean=st.number_input('Concave points')
        
        
    with col4:
        symmetry_mean=st.number_input('Symmetry_mean')
        
        
    with col5:
        fractal_dimension_mean=st.number_input('Fractal_dimension')
        
        
    with col1:
        radius_se=st.number_input('Radius_se')
        
        
    with col2:
        texture_se=st.number_input('Texture_se')
        
        
    with col3:
        perimeter_se=st.number_input('Perimeter_se')
    
        
    with col4:
        area_se=st.number_input('Area_se')
        
        
    with col5:
        smoothness_se=st.number_input('Smoothness_se')
        
        
    with col1:
        compactness_se=st.number_input('Compactness_se')
        
        
    with col2:
        concavity_se=st.number_input('Concavity_se')
        
        
    with col3:
        concave_points_se=st.number_input('Concave points_se')
    
        
    with col4:
        symmetry_se=st.number_input('Symmetry_se')
        
        
    with col5:
        fractal_dimension_se=st.number_input('Fractaldimension_se')
        
        
    with col1:
        radius_worst=st.number_input('Radius_worst')
        
        
    with col2:
        texture_worst=st.number_input('Texture_worst')
        
        
    with col3:
        perimeter_worst=st.number_input('Perimeter_worst')
        
        
    with col4:
        area_worst=st.number_input('Area_worst')

        
    with col5:
        smoothness_worst=st.number_input('Smoothness_worst')

        
    with col1:
        compactness_worst=st.number_input('Compactness_worst')
        
        
    with col2:
        concavity_worst=st.number_input('Concavity_worst')
        
        
    with col3:
        concave_points_worst=st.number_input('Concave points_w')
        
        
    with col4:
        symmetry_worst=st.number_input('Symmetry_worst')
        
        
    with col5:
        fractal_dimension_worst=st.number_input('fractal_dimension_w')
        
        
        
    
    breast_diagnosis = ""
    
    if st.button('Breast Cancer Test Result'):
        breast_prediction = breast_cancer_model.predict([[radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst]])        
        if (breast_prediction[0] == 0):
          breast_diagnosis = "the breast cancer is malignant"
        else:
          breast_diagnosis = "the Breast cancer is Benign"
        
    st.success(breast_diagnosis)
    
    


        
        
    
            
    
    