import utils.email_utils

# Function to escalate issues to human agents
def escalate_to_human(user_input, user_email, user_contact, issue_intensity):
    subject = "Escalation Request from Chatbot"
    
    # Create message body with user details
    message_body = (
        f"User Inquiry: {user_input}\n"
        f"User Email: {user_email}\n"
        f"User Contact No: {user_contact}\n"
        f"Issue Intensity: {issue_intensity}\n"
        "Please assist with the above inquiry."
    )
    
    # Send the email using the send_email function
    utils.email_utils.send_email("ashishlathkar7@gmail.com", subject, message_body)
    
    return "Your request has been escalated to a human agent. You will be contacted shortly."
