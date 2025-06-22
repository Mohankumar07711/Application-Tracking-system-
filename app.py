import streamlit as st
import resume_validation

def main():
    st.title("Job Selection & Validation System")
    
    st.subheader("Select a Company")
    companies = {
        "TCS": ["Fulstack Developer", "Tester", "Manager","Python developer"],
        "Zoho": ["Developer", "Designer", "HR"],
        "Cognizant": ["Developer", "Analyst", "Consultant"],
        "HCL": ["Developer", "Engineer", "Tutor"]
    }
    
    selected_company = st.selectbox("Choose a company:", list(companies.keys()))
    
    st.subheader("Select Your Role")
    available_roles = companies[selected_company]
    role = st.selectbox("Choose a role:", available_roles)

    st.subheader("Upload Your Resume")
    uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
    
    if uploaded_file is not None:
        st.success("Resume uploaded successfully!")
        
        validation_result = resume_validation.validate_resume(uploaded_file, role)
        
        
        st.subheader("Validation Result")
        st.write(f"Company: {selected_company}")
        st.write(f"Role: {role}")
        st.write(validation_result)
    

    st.subheader("Search for Jobs")
    if st.button("Click Here"):
        st.write("Redirecting to job listings...")

if __name__ == "__main__":
    main()