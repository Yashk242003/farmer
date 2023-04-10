import streamlit as st
from streamlit_option_menu import option_menu

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://static.horiba.com/fileadmin/_processed_/6/e/csm_header-agriculture-and-crop-science_3113abbbc6.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

selected = option_menu(
      menu_title=None,
      options=["Home","About","Contact"],
      icons=["house","book","envelope"],
      orientation="horizontal",
)

if selected == "Home":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if selected == "About":
     with st.expander("Project Description"):
        st.write("This is a Streamlit app that demonstrates how to show project description when a button is clicked.")
        st.write("<font color='white' p style='font-family: Arial, Helvetica, sans-serif'>The aim of a project to predict the health of crops using machine learning is to develop an accurate and reliable system that can automatically identify and classify the health status of crops based on input images. The goal is to provide farmers and other stakeholders with a tool that can help them monitor the health of crops and detect early signs of diseases, pests, or other stressors that can affect crop yields and quality.The project involves collecting a large dataset of labeled crop images, which are used to train and validate machine learning models. The images are preprocessed to normalize the pixel values and ensure that they are of the same size and resolution. Various computer vision techniques are then used to extract features from the images, which can be used to classify the health status of the crops. These features may include color histograms, texture features, and shape descriptors.Several machine learning algorithms can be used for crop health prediction, including support vector machines (SVMs), decision trees, random forests, and deep neural networks. The models are trained and evaluated using techniques such as cross-validation and hyperparameter tuning to optimize their performance.Once the model is trained and validated, it can be deployed to predict the health status of new crops based on input images. The system can be integrated with other crop monitoring technologies, such as drones or sensors, to provide a comprehensive and efficient solution for crop health management.Overall, the goal of this project is to improve the accuracy and efficiency of crop health monitoring and management, leading to improved crop yields, better food security, and reduced environmental impact.</p>", unsafe_allow_html=True)

        image_list = ['https://www.hobbyfarms.com/timthumb.php?src=https://img.hobbyfarms.com/wp-content/uploads/2019/03/22190424/sugarbeets-vegetable-crops-KWS-Group-Flickr-600x347.jpg&h=347&w=600&zc=0',
                      'https://actu.epfl.ch/image/39732/1108x622.jpg',
                      'https://www.tinygardenhabit.com/wp-content/uploads/2022/01/phytophthora-infestans-on-potato-leaves-1536x1024.jpg',
                      'https://miro.medium.com/v2/resize:fit:828/0*A-La06BnLM1u_i3R.',]
        num_columns = 2
        num_rows = len(image_list) // num_columns + (len(image_list) % num_columns > 0)
        for i in range(num_rows):
            cols = st.columns(num_columns)
            for j in range(num_columns):
                index = i * num_columns + j
                if index < len(image_list):
                    cols[j].image(image_list[index])
        st.write("Project Menbers are Sudhanshu Yadav, Suyash Dagour,Sakshi Wanode,Yash Kushwah,Yash Soni")
        st.write("To show contact details, use the 'Contact Us' button.")


if selected == "Contact":
     with st.expander("Contact Details"):
        st.write("<font color='white' span style='font-size:36px'>Please feel free to contact us with any questions or feedback!</span>", unsafe_allow_html=True)
        st.write("<font color='white'>Email: sakshiwanode9@gmail.com</font>",unsafe_allow_html=True)
        st.write("<font color='white'>Phone number: +91 ",unsafe_allow_html=True)
        st.write("<font color='white'>Github: https://github.com/login>",unsafe_allow_html=True)
        st.write("<font color='white'>Linkedin:  ",unsafe_allow_html=True)










#https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg