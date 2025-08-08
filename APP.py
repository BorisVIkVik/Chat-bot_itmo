from dialog_window import TextDialog
from download import download_pdf
class App:
    def __init__(self):
        # self.win = Window()
        download_pdf("https://api.itmo.su/constructor-ep/api/v1/static/programs/10033/plan/abit/pdf", "ai.pdf")
        download_pdf("https://api.itmo.su/constructor-ep/api/v1/static/programs/10130/plan/abit/pdf", "ai_product.pdf") 
        self.dialog = TextDialog("Текстовый диалог")
        self.dialog._display_message("Система: Добро пожаловать!")
        self.dialog._display_message("Система: Что вас интересует ")
        self.dialog._display_message("Система: Используйте Ctrl+Enter для отправки")
        
        pass
    def process_message(self):
        pup = 0
    def run(self):
        self.dialog.run()
