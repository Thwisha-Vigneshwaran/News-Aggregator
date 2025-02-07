import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Personalized News Aggregator",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS for light theme and animations
st.markdown("""
    <style>
        body {
            background-color: #f8f9fa;
            color: #333;
        }
        .main-title {
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            animation: fadeIn 2s ease-in-out;
        }
        .sub-title{
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            animation: fadeIn 2s ease-in-out;
        }
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(-10px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        
        .stSidebar {
            background-color: #ffffff !important;
            border-right: 2px solid #ddd;
        }
    </style>
""", unsafe_allow_html=True)

# Animated title
st.markdown('<div class="main-title">📰 Personalized News Aggregator</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Done by:THWISHA V G , Guide: Dr R SUJATHA,Principal</div>',unsafe_allow_html=True)
st.markdown("---")

# Sidebar Navigation with Light Theme
with st.sidebar:
    # st.header("Navigation")
    section = option_menu(
        menu_title="Project Description",
        options=[
            "Abstract", "Company Profile", "Domain", "System Analysis",
            "Module Description", "System Design", "Backend"
        ],
        icons=["book", "building", "globe", "bar-chart", "list-task", "diagram-3", "server"],
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#ffffff"},
            "icon": {"color": "#007bff", "font-size": "22px"},
            "nav-link": {"font-size": "18px", "font-weight": "bold", "color": "#333"},
            "nav-link-selected": {"background-color": "#007bff", "color": "white"}
        }
    )

# Load ER Diagram Placeholder
def load_er_diagram():
    try:
        image = Image.open("ER.png")
        st.image(image, caption='ER Diagram of the System')
    except FileNotFoundError:
        st.error("ER Diagram not found!")

# Sections
if section == "Backend":
    st.header("🖥 Backend Setup (Django)")
    
    st.subheader("1️⃣ Install Django")
    st.code("pip install django", language="bash")
    
    st.subheader("2️⃣ Create a New Django Project")
    st.code("django-admin startproject news_aggregator", language="bash")
        
    st.subheader("3️⃣ Start the Development Server")
    st.code("python manage.py runserver", language="bash")
    
    st.subheader("4️⃣ Create a Django App for Backend")
    st.code("python manage.py startapp backend", language="bash")
    
    st.subheader("5️⃣ Configure Installed Apps in `settings.py`")
    st.code("""
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend',  # Add the new app here
]
""", language="python")
    
    st.subheader("6️⃣ Create Models and Migrate Database")
    st.code("""
# Define models in backend/models.py
from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    source = models.CharField(max_length=255)
    published_date = models.DateTimeField()

# Run migrations
python manage.py makemigrations
python manage.py migrate
""", language="python")
    
    st.subheader("7️⃣ Create Django Superuser (for Admin Panel)")
    st.code("python manage.py createsuperuser", language="bash")

    # Display uploaded images at the end
    st.subheader("8️⃣Project Screenshots")
    image_paths = [
        "Screenshot (36).png", "Screenshot (37).png", "Screenshot (38).png",
        "Screenshot (39).png", "Screenshot (40).png", "Screenshot (41).png",
        "Screenshot (42).png", "Screenshot (43).png"
    ]
    
    for image_path in image_paths:
        try:
            image = Image.open(image_path)
            st.image(image, use_container_width=True)
        except FileNotFoundError:
            st.error(f"Image {image_path} not found!")

elif section == "Company Profile":
    st.header("🏢 Company Profile")
    st.write("""
    **Company Name:** Vinsup Infotech(P) Limited  
    **Location:** Madurai, Tamil Nadu, India  
    **Phone:** +91-7418415755  
    **Email:** info@vinsupinfotech.com  
    **Website:** [Vinsup Infotech](https://vinsupinfotech.com)  
    **Mission:** Provide innovative and customized IT solutions.  
    **Vision:** Be a leading provider of IT solutions and training.
    """)

elif section == "Abstract":
    st.header("📖 Abstract")
    st.write("""
    The **Personalized News Aggregator** is a smart web-based application that gathers and presents news articles 
    from multiple sources based on user preferences. Using APIs and web scraping, the system filters and categorizes 
    news, ensuring users stay informed with real-time updates. The platform leverages machine learning for 
    personalized recommendations and offers user-friendly features like bookmarking and article sharing.
    """)

elif section == "Domain":
    st.header("🌐 Domain")
    st.write("""
    **Domain:** Web Development
    
    **Technology Stack:**
    - **Backend:** Python and Django (MVC Framework)
    - **Frontend:** HTML, CSS, JavaScript
    - **Database:** SQlite3 for storing user preferences
    - **APIs:** News APIs like NewsAPI, Bing News Search
    - **Machine Learning:** NLP-based recommendation engine
    """)

elif section == "System Analysis":
    st.header("🔍 System Analysis")
    
    st.subheader("Problem Statement")
    st.write("""
    With an overwhelming amount of online information, users struggle to filter relevant news. 
    This project simplifies the process by delivering personalized news based on user preferences.
    """)
    
    st.subheader("Objectives")
    st.write("""
    - Provide an intuitive platform for aggregated news viewing
    - Allow users to set preferences for specific topics or sources
    - Ensure real-time updates of news articles using APIs
    - Enable users to bookmark and share articles
    - Utilize machine learning to improve article recommendations
    """)
    
    st.subheader("Feasibility Study")
    st.write("""
    - **Technical Feasibility:** Uses Django, MySQL, and APIs for efficient development.
    - **Operational Feasibility:** User-friendly interface ensures accessibility.
    - **Economic Feasibility:** Minimal cost with open-source technologies.
    """)

elif section == "Module Description":
    st.header("🛠 Module Description")
    st.write("""
    The system consists of the following modules:
    - **User Module:** Registration, login/logout, profile management.
    - **News Aggregation Module:** Fetches news from APIs and updates the database.
    - **Recommendation Engine Module:** Suggests articles based on user preferences.
    - **Admin Module:** Manages users, monitors performance, configures news sources.
    - **Bookmark and Sharing Module:** Allows users to save and share articles.
    - **Search and Filter Module:** Implements search and sorting features.
    - **Sentiment Analysis Module:** Provides insights on public opinion about news.
    """)

elif section == "System Design":
    st.header("🛠 System Design")
    st.subheader("Entities")
    st.write("""
    - **Users:** (UserID, Name, Email, Password, Preferences)
    - **Articles:** (ArticleID, Title, Content, Category, Source, PublishedDate)
    - **Bookmarks:** (BookmarkID, UserID, ArticleID)
    - **Categories:** (CategoryID, Name)
    - **User Interactions:** (InteractionID, UserID, ArticleID, ActionType)
    """)
    
    st.subheader("ER Diagram")
    load_er_diagram()
