from dotenv import dotenv_values


env = dotenv_values('.env')
email_sender = env["EMAIL_SENDER"]
