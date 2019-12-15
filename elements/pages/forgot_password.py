from selene.support.jquery_style_selectors import s


class ForgotPassword:
    # UI elements
    def __init__(self):
        self.forgot_password_input = s("input[id='email']")
        self.forgot_password_button = s("button[id='form_submit']")

    # Methods
    def input_email(self, mail):
        self.forgot_password_input.send_keys(mail)

    def click_button(self):
        self.forgot_password_button.click()

