from selene.support.jquery_style_selectors import s


class EmailSent:
    # UI elements
    def __init__(self):
        self.email_confirmation = s("div[id='content']")
