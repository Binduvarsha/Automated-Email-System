import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
import os


my_email = input("enter your mail id: ")
password_key = input("enter password: ")


gmail_server = "smtp.gmail.com"
gmail_port = 587

my_server = smtplib.SMTP(gmail_server, gmail_port)
my_server.ehlo()
my_server.starttls()
my_server.login(my_email, password_key)

with open("job_contacts.csv") as csv_file:
    jobs = csv.reader(csv_file)
    next(jobs)  # Skip header row

    for recruiter_name, recruiter_email, organization, organization_sector, job_role in jobs:
        # Create a new MIMEMultipart object for each email
        message = MIMEMultipart("alternative")

        # Personalized text content

     



        text_content = f"""
        Hello {recruiter_name}, I hope you are doing well. I'm bindu varsha, an engineering graduate with an Mtech in Computer Science and a specialization in Artificial Intelligence.

        I am writing to inquire regarding open roles in {job_role} at {organization}. I have experience performing data analysis and modeling through my internships and research projects. I'm excited to have an opportunity to apply my skills and learn more in the {organization_sector}.

        I have attached my grade card and résumé below. Looking forward to hearing from you.

        Thanks,
        …… """

        # Attach the personalized text to the message
        message.attach(MIMEText(text_content))

        #attaching images

        


        # define your location
        grade_card_path = 'python_image.jpg'

        # Read the image from location
        grade_card_img = open(grade_card_path, 'rb').read()


        # Attach your image
        message.attach(MIMEImage(grade_card_img, name=os.path.basename(grade_card_path)))


        #attach resume file

        resume_file = 'Resume file.pdf'


        # Read the file from location
        with open(resume_file, 'rb') as f:
            file = MIMEApplication(
                f.read(),
                name=os.path.basename(resume_file)
            )
            file['Content-Disposition'] = f'attachment; filename="{os.path.basename(resume_file)}"'
            message.attach(file)



        my_server.sendmail(
            from_addr=my_email,
            to_addrs=recruiter_email,
            msg=message.as_string()  # Convert the message to a string for sending
        )

        print("Successfully email sent to all accounts")

my_server.quit()
