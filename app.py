import streamlit as st
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import openai
import os
from dotenv import load_dotenv
import time
from kpi_tracker import kpi_tracker

# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = openai.OpenAI(api_key=OPENAI_API_KEY)
analyzer = SentimentIntensityAnalyzer()

# Accessing the environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
YELP_API_KEY = os.getenv("YELP_API_KEY")
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
CALENDARIFIC_API_KEY = os.getenv("CALENDARIFIC_API_KEY")

# Import your utility functions (assuming they are defined in separate files)
from utils.openai_utils import categorize_query
from utils.weather import get_weather
from utils.news import get_news
from utils.todo import manage_todo_list
from utils.email_utils import send_email
from utils.recommendations import get_recommendations, get_movie_recommendations, get_restaurant_recommendations
from utils.meetings import schedule_meeting
from utils.holidays import fetch_holidays
from utils.escalation import escalate_to_human
from utils.general_knowledge import get_general_knowledge_response

def generate_financial_plan(risk_tolerance, financial_goal, investment_preferences, goal_amount, current_savings):
    prompt = f"""
    Given the following information:
    - Risk Tolerance: {risk_tolerance}
    - Financial Goal: {financial_goal}
    - Investment Preferences: {investment_preferences}
    - Goal Amount: {goal_amount}
    - Current Savings: {current_savings}

    Provide a detailed, step-by-step plan on how the user can achieve their financial goal. Include investment strategies, saving plans, and timelines.
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a financial expert."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content.strip()

def generate_tax_optimization_strategy(current_savings, investment_preferences):
    prompt = f"""
    Given the following investment preferences: {investment_preferences} and current savings: {current_savings}, provide a tax optimization strategy. Include suggestions like tax-loss harvesting, retirement account optimization, or other tax-saving tips.
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a tax optimization expert."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content.strip()

def summarize_financial_news(news_url):
    try:
        response = requests.get(news_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        article_text = ' '.join([p.text for p in soup.find_all('p')])

        prompt = f"""
        Summarize the following financial news article in a few sentences: {article_text}
        """
        
        ai_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a financial news summarizer."},
                {"role": "user", "content": prompt}
            ]
        )
        
        return ai_response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error in summarizing the news: {str(e)}"

def analyze_sentiment(news_url):
    try:
        response = requests.get(news_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        article_text = ' '.join([p.text for p in soup.find_all('p')])

        sentiment = analyzer.polarity_scores(article_text)
        return sentiment
    except Exception as e:
        return f"Error in analyzing sentiment: {str(e)}"

# Streamlit sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Go to",
    ["Home", "General Queries", "Weather", "News", "To-Do List", 
     "Recommendations", "Email", "Meetings", "Holidays", "Escalation", "Financial Planning", "Chatbot KPI's"]
)

st.title("🤖 Customer Service Chatbot - Marr Labs")

# Home page with general instructions
if page == "Home":
    st.write("👋 Welcome to the Customer Service Chatbot!")
    st.write("Use the navigation bar on the left to access different features.")
    st.write("This bot can assist with retrieving information, managing tasks, scheduling meetings, and more.")

# Page for general queries
elif page == "General Queries":
    st.header("🔍 General Queries")
    st.write("Ask questions about weather, news, or general knowledge.")
    
    user_input = st.text_input("💬 Enter your query:")
    if st.button("Ask"):
        if user_input:
            category = categorize_query(user_input)
            st.write(f"📂 Category detected: **{category}**")
            
            if category == "information retrieval":
                # Detect if it's weather-related
                if "weather" in user_input.lower():
                    city = user_input.lower().split("weather in")[-1].strip()  # Extract city from user input
                    if city:
                        weather_info = get_weather(city)
                        st.text_area("🌤️ Weather Information", value=weather_info, height=200)
                elif "news" in user_input.lower():
                    news_info = get_news()
                    st.text_area("📰 Top News", value=news_info, height=400)
                else:
                    st.write("🔎 For general information retrieval, please refine your query.")
            elif category == "general knowledge":
                st.write("📖 The query pertains to general knowledge.")
                answer = get_general_knowledge_response(user_input)
                st.text_area("📚 Answer", value=answer, height=200)
            else:
                st.error(f"Unsupported query category: {category}")

# Page for weather information
elif page == "Weather":
    st.header("🌦️ Weather Information")
    st.write("Get current weather updates for any city.")
    
    city = st.text_input("🌇 Enter city:")
    if st.button("Get Weather"):
        response = get_weather(city)
        st.text_area("🌈 Weather Information", value=response, height=200)

# Page for news
elif page == "News":
    st.header("📰 Top News")
    st.write("Fetch the latest news headlines.")
    
    if st.button("Get News"):
        response = get_news()
        st.text_area("📰 Top Headlines", value=response, height=400)

# Page for managing the to-do list
elif page == "To-Do List":
    st.header("📝 To-Do List Manager")
    st.write("Add, view, remove, or update tasks from your to-do list.")
    
    action = st.selectbox("🛠️ Action", ["Add Task", "View Tasks", "Remove Task", "Update Task"])
    
    task = st.text_input("✏️ Task description:")
    
    if action == "Update Task":
        task_to_update = st.text_input("✏️ New Task description:")
    else:
        task_to_update = None

    if st.button("Submit"):
        # Ensure the action matches the expected string in lowercase
        if action == "Update Task" and task and task_to_update:
            response = manage_todo_list("update task", task, task_to_update)
        elif action == "Add Task" and task:
            response = manage_todo_list("add task", task)
        elif action == "View Tasks":
            response = manage_todo_list("view tasks")
        elif action == "Remove Task" and task:
            response = manage_todo_list("remove task", task)
        else:
            response = "Please provide the necessary inputs."
        
        st.text_area("📋 Response", value=response, height=200)

# Page for recommendations (movies, restaurants)
elif page == "Recommendations":
    st.header("🍽️ Recommendations")
    st.write("Get personalized recommendations for restaurants or movies.")
    
    recommendation_type = st.selectbox("🔍 Choose a recommendation type:", ["Restaurants", "Movies"])
    if recommendation_type == "Restaurants":
        city = st.text_input("🏙️ Enter city for restaurant recommendations:")
        if st.button("Get Recommendations"):
            recommendations = get_restaurant_recommendations(city)
            st.text_area("🍽️ Restaurant Recommendations", value=recommendations, height=300)
    elif recommendation_type == "Movies":
        genre = st.selectbox("🎬 Select a genre:", ["Any", "Action", "Comedy", "Drama", "Horror", "Science Fiction", "Romance", "Thriller"])
        year_filter = st.selectbox("📅 Select time period:", ["Any", "After 2000", "Before 2000"])
        if st.button("Get Movie Recommendations"):
            recommendations = get_movie_recommendations(genre if genre != "Any" else None, year_filter if year_filter != "Any" else None)
            st.text_area("🎥 Movie Recommendations", value=recommendations, height=300)

# Page for sending emails
elif page == "Email":
    st.header("📧 Email Service")
    st.write("Send an email with a subject and message.")
    
    recipient_email = st.text_input("✉️ Recipient Email")
    subject = st.text_input("📝 Subject")
    message_body = st.text_area("🖋️ Message")
    if st.button("Send Email"):
        response = send_email(recipient_email, subject, message_body)
        st.success(response)

# Page for scheduling meetings
elif page == "Meetings":
    st.header("📅 Meeting Scheduler")
    st.write("Schedule a meeting by providing your email and the desired date and time.")
    
    user_email = st.text_input("📮 Your Email:")
    meeting_date = st.date_input("📆 Select Date:")
    meeting_time = st.time_input("⏰ Select Time:")
    if st.button("Schedule Meeting"):
        meeting_datetime = datetime.combine(meeting_date, meeting_time)
        success, result = schedule_meeting(user_email, meeting_datetime)
        if success:
            st.success("✅ Meeting scheduled successfully!")
        else:
            st.error(f"❌ Failed to schedule meeting: {result}")

# Page for checking holidays and scheduling events
elif page == "Holidays":
    st.header("🎉 Holiday Checker")
    st.write("Check if there are public holidays on a given date and schedule an event.")
    
    event_title = st.text_input("🎊 Event Title")
    event_description = st.text_area("📜 Event Description")
    event_date = st.date_input("📅 Event Date")
    event_time = st.time_input("⏰ Event Time")
    country_code = st.text_input("🌎 Country Code (e.g., US for United States)", max_chars=2).upper()
    recipient_email = st.text_input("✉️ Recipient Email")
    
    # Submit button
    if st.button("Check Holiday and Schedule Event"):
        if not recipient_email:
            st.error("Please enter a valid email address.")

        # Parse the date input
        event_year = event_date.year
        event_month = event_date.month
        event_day = event_date.day

        # Fetch holidays for the provided country and date
        holidays = fetch_holidays(CALENDARIFIC_API_KEY, country_code, event_year, event_month, event_day)

        # Display holidays or schedule event
        if isinstance(holidays, str):
            st.error(holidays)  # If there's an error with the API call
        elif holidays:
            # If holidays are found
            st.warning(f"Public Holidays on {event_date}:")
            for holiday in holidays:
                st.write(f"- {holiday['name']}: {holiday['description']}")
            st.write("Consider rescheduling your event if it conflicts with a holiday.")
        else:
            # No holidays found, allow the user to proceed with scheduling the event
            st.success("No public holidays on this date. You can proceed with your event.")
            st.write(f"Event '{event_title}' scheduled on {event_date} at {event_time}.")

            # Prepare the email content
            subject = f"Event Reminder: {event_title}"
            message_body = (
                f"Hello,\n\nYour event '{event_title}' is scheduled on {event_date} at {event_time}.\n\n"
                f"Event Details:\nDescription: {event_description}\nDate: {event_date}\nTime: {event_time}\n\n"
                f"Thank you!"
            )

            # Send confirmation email
            email_status = send_email(recipient_email, subject, message_body)
            if "successfully" in email_status:
                st.success("Confirmation email sent successfully!")
            else:
                st.error(f"Failed to send email: {email_status}")

# Page for issue escalation
elif page == "Escalation":
    st.header("⚠️ Issue Escalation")
    st.write("Describe your issue and escalate it to a human for further assistance.")
    
    issue_description = st.text_area("📝 Describe your issue:")
    user_email = st.text_input("📧 Your Email:")
    user_contact = st.text_input("📞 Your Contact:")
    issue_intensity = st.selectbox("🔴 Issue Intensity", ["Low", "Medium", "High"])
    if st.button("Escalate Issue"):
        response = escalate_to_human(issue_description, user_email, user_contact, issue_intensity)
        st.success("Your issue has been escalated. You will be contacted soon!")

# Financial Planning Section
elif page == "Financial Planning":
    st.header("💼 Financial Planning")
    option = st.sidebar.selectbox(
        "Choose a feature", 
        ["Personalized Financial Plan", "Tax Optimization Strategy", "Financial News Summary", "Sentiment Intensity Analyzer"]
    )

    if option == "Personalized Financial Plan":
        st.header("Personalized Financial Plan 💼")

        risk_tolerance = st.selectbox("Risk Tolerance", ["Low", "Medium", "High"])
        financial_goal = st.selectbox(
            "Financial Goal", 
            ["Save for retirement", "Buy a house", "Save for education", "Build an emergency fund", "Custom"]
        )

        if financial_goal == "Custom":
            goal_name = st.text_input("Custom Goal Name", "e.g., Start a business")
        else:
            goal_name = financial_goal

        investment_preferences = st.multiselect(
            "Investment Preferences", 
            ["Stocks", "Bonds", "Index Funds", "Mutual Funds", "Real Estate", "Cryptocurrency", "ETFs"]
        )

        goal_amount = st.number_input("Goal Amount", min_value=0, step=1000)
        current_savings = st.number_input("Current Savings", min_value=0, step=1000)

        if st.button("Generate Financial Plan"):
            financial_plan = generate_financial_plan(risk_tolerance, goal_name, investment_preferences, goal_amount, current_savings)
            st.subheader("Your Financial Plan 📈")
            st.write(financial_plan)

    elif option == "Tax Optimization Strategy":
        st.header("Tax Optimization Strategy 🧾")

        current_savings = st.number_input("Current Savings", min_value=0, step=1000)
        investment_preferences = st.multiselect(
            "Investment Preferences", 
            ["Stocks", "Bonds", "Index Funds", "Mutual Funds", "Real Estate", "Cryptocurrency", "ETFs"]
        )

        if st.button("Generate Tax Optimization Strategy"):
            tax_strategy = generate_tax_optimization_strategy(current_savings, investment_preferences)
            st.subheader("Your Tax Optimization Strategy 💡")
            st.write(tax_strategy)

    elif option == "Financial News Summary":
        st.header("Financial News Summary 📰")
        news_url = st.text_input("Enter Financial News URL")

        if st.button("Get Article Summary"):
            summary = summarize_financial_news(news_url)
            st.subheader("Article Summary 📝")
            st.write(summary)

    elif option == "Sentiment Intensity Analyzer":
        st.header("Sentiment Intensity Analyzer 📊")
        news_url = st.text_input("Enter Financial News URL")

        if st.button("Analyze Sentiment"):
            sentiment = analyze_sentiment(news_url)
            if isinstance(sentiment, dict):
                st.subheader("Sentiment Analysis Results 🧮")
                st.write("Positive: ", sentiment['pos'])
                st.write("Neutral: ", sentiment['neu'])
                st.write("Negative: ", sentiment['neg'])
                st.write("Compound: ", sentiment['compound'])
            else:
                st.write(sentiment)
                
elif page == "Chatbot KPI's":
    st.header("Chatbot Interaction")
    user_id = st.text_input("Enter User ID:")
    user_input = st.text_input("Your message:")
    
    if st.button("Send"):
        start_time = time.time()  # Start timing the response
        kpi_tracker.log_interaction(user_id)  # Log interaction
        
        # Call your chatbot logic here
        response = chatbot.get_response(user_input)  # Placeholder for your chatbot response logic
        
        # Log response time
        kpi_tracker.log_response_time(start_time)

        # Display response
        st.write(response)
        
        # Example: Log satisfaction score (you could implement a feedback mechanism)
        satisfaction_score = st.slider("Rate your satisfaction:", 1, 5)
        kpi_tracker.log_satisfaction(satisfaction_score)
        
        # Example: Log resolution status (for demonstration)
        resolved = st.checkbox("Was your issue resolved?")
        kpi_tracker.log_resolution(resolved)

# Display KPIs
if st.button("Show KPIs"):
    metrics = kpi_tracker.get_metrics()
    st.write(metrics)


# Footer
st.sidebar.title("About")
st.sidebar.write("This is a customer service chatbot application powered by AI. *Developer: [Ashish Lathkar]")
