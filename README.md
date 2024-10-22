# Customer Service Chatbot for Marr Labs 🤖

## Project Overview

The **Customer Service Chatbot** is a prototype developed to assist users, specifically executives at an Internet Service Company, with various tasks and inquiries. This project emphasizes functionality over aesthetics, focusing on effectively solving user problems through natural language processing (NLP) and task automation. The chatbot is designed to enhance productivity by streamlining common workplace activities such as scheduling, information retrieval, and task management.

## Live Demo 🌐

You can test the chatbot live at the following link: [Customer Service Chatbot](https://customer-service-chatbot-marr-labs.streamlit.app/)

## Objectives 🎯

The primary objectives of this project are:

- **Understanding User Queries:** Utilize NLP capabilities to accurately interpret and categorize user inquiries into predefined categories such as scheduling, reminders, information retrieval, task management, and general assistance.
  
- **Implementing Core Functionalities:** Develop features that enable the chatbot to perform tasks such as setting reminders, scheduling events, providing information, managing to-do lists, offering recommendations, and facilitating basic communication tasks.
  
- **Integration with Existing Platforms:** Seamlessly integrate with tools like calendars, email, and task management applications to enhance user experience.
  
- **Human Escalation Mechanism:** Establish a clear process for the chatbot to escalate issues to human agents when necessary, ensuring that users receive timely assistance.

## Functionalities 🛠️

1. **User Query Understanding:**  
   The chatbot employs NLP algorithms to parse user queries and classify them into relevant categories, allowing appropriate responses based on the type of request.

2. **Information Retrieval 📚:**  
   Users can ask the chatbot for:
   - **Weather Updates:** Current weather conditions based on user location.
   - **News Updates:** The latest headlines and summaries from various news sources.
   - **General Knowledge:** Responses to trivia or fact-based inquiries.

3. **Task Management ✅:**  
   The chatbot provides robust task management features, including:
   - **To-Do List Management:** Users can add, remove, or update tasks in their to-do lists, helping them stay organized.
   - **Reminders:** Users can set reminders for specific tasks or events.

4. **Scheduling Events 📅:**  
   Users can schedule events directly through the chatbot by providing necessary details such as the event title, date, and time. The chatbot interfaces with calendar APIs to create events efficiently.

5. **Recommendations 🍽️:**  
   The chatbot can provide personalized recommendations based on user preferences, such as:
   - **Restaurants:** Suggestions for dining options based on location and cuisine preferences.
   - **Entertainment:** Recommendations for movies or shows.

6. **Email Communication ✉️:**  
   Users can send emails directly through the chatbot by specifying the recipient, subject, and body of the email.

7. **Holiday Information 🎉:**  
   Users can check public holidays and important dates, facilitating better scheduling of events and meetings.

8. **Escalation to Human Agents 🚨:**  
   If the chatbot encounters an issue it cannot resolve, it can escalate the query to a human agent, including:
   - **Transfer of Context:** The chatbot summarizes the user’s query and context for the human agent.
   - **Seamless Transition:** Ensures users do not need to repeat themselves when transitioning from the chatbot to a human agent.

9. **Financial Planning 💼:**  
   The chatbot includes a Financial Planning section with features such as:
   - **Personalized Financial Plan:** Users can input their risk tolerance, financial goals, and investment preferences.
   - **Tax Optimization Strategy:** Recommendations on optimizing taxes based on current savings and investment preferences.
   - **Financial News Summary:** Concise summaries of financial news articles.
   - **Sentiment Intensity Analyzer:** Analyze the sentiment of a financial news URL.

## Large Language Model (LLM) Integration with GPT-3.5 Turbo ⚡

The chatbot utilizes OpenAI's **GPT-3.5 Turbo**, a state-of-the-art large language model (LLM), to enhance its conversational capabilities. Key aspects of the LLM integration include:

- **Natural Language Understanding:** GPT-3.5 Turbo leverages advanced NLP techniques to comprehend user intents.
- **Response Generation:** Produces human-like responses for engaging interactions.
- **Context Awareness:** Retains context across conversations for consistent responses.
- **Scalability:** Handles numerous user queries simultaneously, suitable for high-demand environments.

This integration improves user experience and opens opportunities for advanced features, such as deeper financial insights and personalized advice.

## Technical Stack 🖥️

- **Frontend:** Developed using Streamlit, enabling rapid web application creation.
- **Backend:** Implemented in Python, leveraging various libraries for NLP and API interactions.
- **APIs Used:**
  - OpenAI API: For NLP capabilities to interpret user queries.
  - Weather API: To retrieve current weather information.
  - News API: For fetching the latest news articles.
  - Yelp API: To provide restaurant recommendations.
  - SMTP Service: For sending emails on behalf of users.
  - Calendarific API: To retrieve information about public holidays.

## KPI Tracking 📊
The project includes a KPI Tracker to monitor and analyze chatbot performance. The KPI Tracker tracks key metrics, including:

- Total Interactions: The total number of interactions logged.
- Active Users: The number of unique users interacting with the chatbot.
- Average Satisfaction Score: The average user satisfaction score collected from feedback.
- Average First Response Time: The average time taken for the chatbot to respond to user queries.
- Resolution Rate: The percentage of user queries successfully resolved by the chatbot.

## Installation and Setup ⚙️

To run the chatbot locally, follow these steps:

1. Clone the Repository:
   ```bash
   git clone https://github.com/Ashishlathkar77/Customer-Service-Chatbot.git
   cd Customer-Service-Chatbot
