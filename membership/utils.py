from django.core.mail import send_mail
from django.core.mail import BadHeaderError
from django.conf import settings

def send_confirmation_email(user_email, plan, end_date):
    try:
        subject = f"Your {plan.name} Membership Confirmation"
        message = f"Dear {user_email},\n\n" \
                  f"Thank you for purchasing the {plan.name} membership.\n\n" \
                  f"Your membership is valid until {end_date.strftime('%Y-%m-%d')}.\n\n" \
                  f"Best regards,\nThe Ulinzi  Team"
        from_email = settings.EMAIL_HOST_USER

        send_mail(subject, message, from_email, [user_email], fail_silently=False)
    except BadHeaderError:
        print("Invalid header found.")
    except Exception as e:
        print(f"Error sending email: {e}")
