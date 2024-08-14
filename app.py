import streamlit as st

def homepage():
    st.title("Empowering Businesses with Automated Data Science Solutions")
    st.subheader("Leverage advanced analytics to unlock the full potential of your data.")
    
    st.write("""
    At our agency, we specialize in delivering tailored data science solutions that help businesses optimize processes, reduce costs, and drive growth. Our expert team uses cutting-edge technology to transform raw data into actionable insights.
    """)
    
    st.image("homepage_image.jpg", caption="Innovative Data Science Solutions", use_column_width=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("Get Started")
    with col2:
        st.button("Schedule a Demo")
    with col3:
        st.button("Learn More")

def services():
    st.title("Our Services & Products")
    
    st.write("""
    - **Automated Data Analysis:** Streamline your data processing with our automated tools that deliver fast and accurate results.
    - **Custom Solutions:** Tailored data science solutions designed to meet the unique needs of your business.
    - **Consulting:** Expert consulting services to guide your business through the complexities of data science.
    """)
    
    st.subheader("Benefits")
    st.write("""
    - Cost Savings: Reduce operational costs with efficient data processing.
    - Scalability: Easily scale your data solutions as your business grows.
    - Improved Decision-Making: Make informed decisions with clear, actionable insights.
    """)
    
    st.subheader("Case Studies")
    st.write("Explore how we've helped businesses achieve their goals with our services.")
    st.image("case_study_image.jpg", caption="Case Study: Optimizing Retail Operations", use_column_width=True)

def how_it_works():
    st.title("How It Works")
    
    st.write("Our process is simple and designed to deliver results efficiently.")
    
    st.subheader("Step-by-Step Process")
    steps = [
        "**Sign-Up:** Start by signing up for our services.",
        "**Data Integration:** We'll integrate your data into our platform.",
        "**Analysis:** Our algorithms analyze your data to extract meaningful insights.",
        "**Report Delivery:** Receive detailed reports and actionable insights."
    ]
    for step in steps:
        st.write(f"- {step}")
    
    st.image("process_diagram.jpg", caption="Client Journey", use_column_width=True)

def about_us():
    st.title("About Us")
    
    st.write("We are a data science agency with a mission to empower businesses through innovative data solutions.")
    
    st.subheader("Meet the Team")
    team_members = [
        ("Youssef Galal", "Cofounder", "Software and Machine Learning Engineer expert with over 5 years of experience."),
        ("Omar Abd Al-hamed", "Cofounder", "Data Scientist, ensuring our solutions are cutting-edge.")
    ]
    for name, role, description in team_members:
        st.write(f"- **{name}, {role}:** {description}")
    
    st.image("team_photo.jpg", caption="Our Team", use_column_width=True)
    
    st.subheader("Why Choose Us?")
    st.write("Our unique technology, combined with our expertise, ensures you get the best results and exceptional customer service.")

def contact_us():
    st.title("Contact Us")
    
    st.write("We'd love to hear from you. Whether you have a question or need assistance, we're here to help.")
    
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Submit")
    
    if submit_button:
        st.success("Thank you for your message. We'll get back to you soon!")
    
    st.write("Or reach us directly at:")
    contacts = [
        ("Phone", "01125580551"),
        ("Email", "eng.youssef.galal@gmail.com"),
        ("Phone", "01551388977"),
        ("Email", "omarmohamed744744@gmail.com")
    ]
    for method, value in contacts:
        st.write(f"**{method}:** {value}")
    
    st.write("Visit us:")
    st.write("Greek Campus., Cairo, Egypt")

def pricing():
    st.title("Pricing")
    
    packages = [
        ("Basic Package", "$999/month", "Includes automated data analysis and standard reports."),
        ("Pro Package", "$1999/month", "Includes all features of the Basic Package, plus custom solutions."),
        ("Enterprise Package", "Custom pricing", "Tailored solutions for large businesses with specific needs.")
    ]
    
    for name, price, description in packages:
        st.write(f"**{name}:** {price} - {description}")
    
    st.button("Contact Us for Custom Pricing")

def faqs():
    st.title("FAQs")
    
    st.subheader("Common Questions")
    st.write("Find answers to common questions about our services, pricing, and process.")
    
    questions = [
        ("What industries do you serve?", "We serve a wide range of industries including finance, retail, healthcare, and more."),
        ("How secure is my data?", "We take data security very seriously and use state-of-the-art encryption and protocols.")
    ]
    
    for question, answer in questions:
        st.write(f"**Q:** {question}")
        st.write(f"**A:** {answer}")
    
    st.text_input("Search FAQs")

def client_login():
    st.title("Client Login")
    
    st.write("Access your dashboard to view reports and manage your account.")
    
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button("Login")
    
    if login_button:
        st.warning("Login functionality not implemented in this demo.")
    
    st.write("Forgot your password? [Click here](#)")

def blog():
    st.title("Blog & Resources")
    
    st.write("Stay up to date with the latest trends in data science and analytics.")
    
    st.subheader("Recent Articles")
    articles = [
        "**Understanding Machine Learning Models** - A guide to different types of machine learning models.",
        "**How to Improve Data Quality** - Tips for ensuring your data is accurate and reliable."
    ]
    for article in articles:
        st.write(article)
    
    st.subheader("Resources")
    st.write("Download our latest eBook on data science best practices.")
    st.button("Download eBook")

def footer():
    st.write("---")
    st.write("© 2024 Data Science Agency - All Rights Reserved.")
    st.write("Follow us on [LinkedIn](#) | [Twitter](#) | [Facebook](#)")
    st.write("Privacy Policy | Terms of Service")




def main():
    st.sidebar.title("Navigation")

    
    # Create a more visually appealing radio button for navigation
    pages = {
        "🏠 Home": homepage,
        "🛠️ Services": services,
        "🔄 How It Works": how_it_works,
        "👥 About Us": about_us,
        "📞 Contact Us": contact_us,
        "💰 Pricing": pricing,
        "❓ FAQs": faqs,
        "🔐 Client Login": client_login,
        "📝 Blog": blog
    }
    
    
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    pages[selection]()
    footer()

if __name__ == "__main__":
    main()