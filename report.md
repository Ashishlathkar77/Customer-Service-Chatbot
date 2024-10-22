# Customer Service Chatbot for Marr Labs 🤖

## Project Overview

The **Customer Service Chatbot** is a prototype developed to assist users, specifically executives at an Internet Service Company, with various tasks and inquiries. This project emphasizes functionality over aesthetics, focusing on effectively solving user problems through natural language processing (NLP) and task automation. The chatbot is designed to enhance productivity by streamlining common workplace activities such as scheduling, information retrieval, and task management.

### Live Demo 🌐
You can test the chatbot live at the following link: [Customer Service Chatbot](https://customer-service-chatbot-marr-labs.streamlit.app/)

## Objectives 🎯
The primary objectives of this project are:
- **Understanding User Queries**: Utilize NLP capabilities to accurately interpret and categorize user inquiries into predefined categories such as scheduling, reminders, information retrieval, task management, and general assistance.
- **Implementing Core Functionalities**: Develop features that enable the chatbot to perform tasks such as setting reminders, scheduling events, providing information, managing to-do lists, offering recommendations, and facilitating basic communication tasks.
- **Integration with Existing Platforms**: Seamlessly integrate with tools like calendars, email, and task management applications to enhance user experience.
- **Human Escalation Mechanism**: Establish a clear process for the chatbot to escalate issues to human agents when necessary, ensuring that users receive timely assistance.

## Functionalities 🛠️
### 1. User Query Understanding
The chatbot employs NLP algorithms to parse user queries and classify them into relevant categories. This understanding allows the chatbot to respond appropriately based on the type of request, whether it be related to scheduling or general inquiries.

### 2. Information Retrieval 📚
Users can ask the chatbot for:
- **Weather Updates**: Current weather conditions based on user location.
- **News Updates**: The latest headlines and summaries from various news sources.
- **General Knowledge**: Responses to trivia or fact-based inquiries.

### 3. Task Management ✅
The chatbot provides robust task management features, including:
- **To-Do List Management**: Users can add, remove, or update tasks in their to-do lists, helping them stay organized.
- **Reminders**: Users can set reminders for specific tasks or events, which will prompt them at designated times.

### 4. Scheduling Events 📅
Users can schedule events directly through the chatbot by providing necessary details such as the event title, date, and time. The chatbot interfaces with calendar APIs to create events efficiently.

### 5. Recommendations 🍽️
The chatbot can provide personalized recommendations based on user preferences, such as:
- **Restaurants**: Suggestions for dining options based on location and cuisine preferences.
- **Entertainment**: Recommendations for movies or shows.

### 6. Email Communication ✉️
Users can send emails directly through the chatbot. They can specify the recipient, subject, and body of the email, which the chatbot will send using an email service.

### 7. Holiday Information 🎉
Users can check public holidays and important dates, facilitating better scheduling of events and meetings.

### 8. Escalation to Human Agents 🚨
If the chatbot encounters an issue it cannot resolve, it can escalate the query to a human agent. This process includes:
- **Transfer of Context**: The chatbot summarizes the user’s query and context to provide the human agent with relevant information.
- **Seamless Transition**: Ensures users do not need to repeat themselves when transitioning from the chatbot to a human agent.

### 9. Financial Planning 💼
The chatbot also includes a **Financial Planning** section, where users can access various features:
- **Personalized Financial Plan**: Users can input their risk tolerance, financial goals, investment preferences, goal amounts, and current savings to generate a customized financial plan.
- **Tax Optimization Strategy**: Users can receive recommendations on how to optimize their taxes based on their current savings and investment preferences.
- **Financial News Summary**: Users can input a URL of a financial news article to receive a concise summary.
- **Sentiment Intensity Analyzer**: The chatbot can analyze the sentiment of a provided financial news URL, breaking down positive, neutral, negative, and compound sentiments.

## Large Language Model (LLM) Integration with GPT-3.5 Turbo ⚡
The chatbot utilizes **OpenAI's GPT-3.5 Turbo**, a state-of-the-art large language model (LLM), to enhance its conversational capabilities. This model excels in understanding context, generating coherent responses, and managing a wide range of queries effectively. Here are some key aspects of the LLM integration:

- **Natural Language Understanding**: GPT-3.5 Turbo leverages advanced NLP techniques to comprehend user intents, allowing for accurate interpretation of queries.
- **Response Generation**: The model is designed to produce human-like responses, ensuring that interactions feel natural and engaging.
- **Context Awareness**: With its ability to retain context across turns in conversation, the model provides consistent and relevant responses based on prior interactions.
- **Scalability**: The integration of GPT-3.5 Turbo enables the chatbot to handle numerous user queries simultaneously, making it suitable for deployment in high-demand environments.

This integration improves user experience and opens up opportunities for advanced features, such as deeper financial insights and personalized advice based on user behavior and preferences.

## Technical Stack 🖥️
- **Frontend**: Developed using Streamlit, which allows for rapid creation of web applications with minimal setup.
- **Backend**: Implemented in Python, leveraging various libraries for natural language processing and API interactions.
- **APIs Used**:
  - **OpenAI API**: For NLP capabilities to interpret user queries.
  - **Weather API**: To retrieve current weather information based on user input.
  - **News API**: For fetching the latest news articles.
  - **Yelp API**: To provide restaurant recommendations.
  - **SMTP Service**: For sending emails on behalf of users.
  - **Calendarific API**: To retrieve information about public holidays.

## Installation and Setup ⚙️
To run the chatbot locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ashishlathkar77/Customer-Service-Chatbot.git
   cd Customer-Service-Chatbot
