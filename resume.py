from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "main.css"
resume_file = current_dir / "Resume[Alya_Aminuddin].pdf"
profile_pic = current_dir / "dp.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Alya Aminuddin"
PAGE_ICON = ":wave:"
NAME = "Alya Nabihah Amrina Binti Aminuddin"
DESCRIPTION = """
Aspired Data Scientist, with a passion for solving complex problems and uncovering insights through data analysis.
"""
EMAIL = "alyaamrina@gmail.com"
PHONE_NUMBER = "+6013 804-7240"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/alya-aminuddin-11700917a/",
    "GitHub": "https://github.com/alyaaminuddin"
}
# PROJECTS = {
#     "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
#     "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
#     "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
#     "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
# }


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write("📱", PHONE_NUMBER)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    if platform in ["LinkedIn", "GitHub"]:
        cols[index].write(f"<p align='center'><a href='{link}'>{platform}</a></p>", unsafe_allow_html=True)
    else:
        cols[index].write(f"[{platform}]({link})")


# NAVIGATION TOOLBAR


st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #E29FC2;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Alya Aminuddin</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#Skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#Leadership And Affiliations">Leadership And Affiliations</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)








# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 2 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👩🏻‍💻 Programming: Python, SQL, R
- 📈 Data Manipulation: Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn
- 📊 Data Visulization: Matplotlib, IBM Cognos Dashboard, Microsoft Excel, Power BI
- 📚 Modeling: Supervised and Unsupervised Machine Learning
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)

# --- EDUCATION ---
st.write('\n')
st.subheader("Education")
st.write("---")

# --- Education 1
st.write("🎓", "**B.Sc Mathematical Statistics and Probability | Purdue University**")
st.write("Spring 2020")
st.write(
    """
- ► Completed model selection and regression analysis project using R programming language.
- ► Focused on statistical quality control and specialized in six sigma methodology.
""")

# --- Education 2
st.write("🎓", "**As Mathematics | Northampton Community College**")
st.write("Fall 2018")
st.write(
    """
- ► Completed mathematics courses such as calculus and differential equation with High Distinction.
""")

# --- WORK EXPERIENCE ---
st.write('\n')
st.subheader("Work Experience")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Scientist | Invoke Malaysia**")
st.write("10/2022 - Present")
st.write(
    """
- ► Analyze large data sets using Python, R, and Excel to identify patterns and trends, and communicate insights to management and stakeholders.
- ► Create and maintain dashboards and reports using Mongo DB and Power BI, ensuring accurate and timely reporting of key performance indicators (KPIs).
- ► Collaborate with cross-functional teams to identify business problems and design solutions, utilizing statistical analysis and machine learning techniques.
- ► Develop and implement data-driven solutions to improve business processes, resulting in a 10% increase in revenue.
- ► Automate data collection and analysis processes using scripting languages such as Python, reducing analysis time by 50%.
- ► Provide training and support to junior analysts, enabling them to improve their technical skills and enhance their contributions to the team.
""")

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Admin | DCT Inc**")
st.write("12/2020 - 04/2022")
st.write(
    """
- ► Identified and documented detailed business rules and use cases based on requirements analysis.
- ► Updated spreadsheets and databases to track, analyze and report on performance and sales data, increased profit by 15%.
- ► Implemented new ideas constantly to increase productivity and efficiency of workflow by 8%.
"""
)

# --- LEADERSHIP AND AFFILIATIONS ---
st.write('\n')
st.subheader("Leadership and Affiliations")
st.write("---")

# --- Leadership 1
st.write("🚧", "**Cultural Director | Purdue University Malaysian Student Association (PUMSA)**")
st.write("01/2019 - 12/2019")
st.write(
    """
- ► Collaborated and build relationships with 2 other organization to hold cultural events like Chinese New Year and Aidul-Fitri.
- ► Directed and designed cultural events for students throughout the semester.
""")

# --- Leadership 2
st.write('\n')
st.write("🚧", "**Director of Malaysian Graduation Night 2019  | Purdue University Malaysian Student Association (PUMSA)**")
st.write("01/2019 - 05/2019")
st.write(
    """
- ► Organized weekly meeting to brainstorm ideas and budgets 12 weeks before the event took place.
- ► Oversee and helped teammates with tasks assigned.
- ► Managed event set-up on the day and making sure event flows smoothly.
"""
)

# --- Leadership 3
st.write('\n')
st.write("🚧", "**Event Organizer of PUMSA Night 2018   | Purdue University Malaysian Student Association (PUMSA)**")
st.write("08/2018 - 12/2018")
st.write(
    """
- ► Planned meetings with members weekly to discussed time flow and organization.
- ► Gathered 200 students from other universities across Midwest.
- ► Arranged the time management of logistics for food setup.
"""
)


# --- Projects & Accomplishments ---
# st.write('\n')
# st.subheader("Projects & Accomplishments")
# st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")