from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer, PasswordResetSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "full_name",
            "university",
            "faculty",
            "department",
            "year",
            "email",
            "is_volunteer",
        ]


class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        model = User
        fields = [
            "id",
            "full_name",
            "university",
            "faculty",
            "department",
            "year",
            "email",
            "is_volunteer",
            "is_staff",
        ]


class CustomPasswordResetSerializer(PasswordResetSerializer):
    @property
    def password_reset_form_class(self):
        return PasswordResetForm

    def get_email_options(self):
        return {
            "domain_override": settings.ALLOWED_HOSTS[1],
            # "extra_email_context":{
            #     "domain": "domain nigga"
            # },
        }

    def save(self):
        request = self.context.get("request")
        # Set some values to trigger the send_email method.
        opts = {
            "use_https": request.is_secure(),
            "from_email": "curlyzik@gmail.com",
            "request": request,
            "html_email_template_name": "registration/password_reset_key_message.txt",
            "email_template_name": "registration/password_reset_key_message.txt",
        }

        opts.update(self.get_email_options())
        self.reset_form.save(**opts)
