import tkinter as tk
from tkinter import scrolledtext, font, ttk

class TextDialog:
    def __init__(self, app, title="Диалоговое окно"):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry("500x500")
        self.root.minsize(400, 300)
        self.root.configure(bg="#f0f0f0")
        self.app = app
        # Создаем главный разделитель (PanedWindow)
        self.main_pane = ttk.PanedWindow(self.root, orient=tk.VERTICAL)
        self.main_pane.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Стили
        self.font = font.Font(family="Arial", size=10)
        self.input_font = font.Font(family="Arial", size=12)
        
        # 1. Верхняя панель - история диалога
        chat_frame = ttk.Frame(self.main_pane)
        self.main_pane.add(chat_frame, weight=3)  # 3/4 пространства
        
        self.chat_area = scrolledtext.ScrolledText(
            chat_frame, 
            wrap=tk.WORD,
            font=self.font,
            bg="white",
            padx=10,
            pady=10
        )
        self.chat_area.pack(fill=tk.BOTH, expand=True)
        self.chat_area.config(state=tk.DISABLED)
        
        # 2. Нижняя панель - ввод сообщения
        input_frame = ttk.Frame(self.main_pane)
        self.main_pane.add(input_frame, weight=1)  # 1/4 пространства
        
        # Создаем фрейм для элементов ввода
        input_container = ttk.Frame(input_frame)
        input_container.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        
        # Поле ввода с подсказкой
        self.input_var = tk.StringVar()
        self.input_field = tk.Text(
            input_container,
            height=4,  # 4 строки высотой
            font=self.input_font,
            bg="white",
            fg="#333333",
            relief=tk.SOLID,
            borderwidth=1,
            wrap=tk.WORD  # перенос слов
        )
        self.input_field.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        self.input_field.insert("1.0", "Введите ваше сообщение здесь...")
        self.input_field.bind("<FocusIn>", self._clear_placeholder)
        self.input_field.bind("<Control-Return>", self._send_message)  # Ctrl+Enter для отправки
        
        # Кнопка отправки
        send_button = tk.Button(
            input_container,
            text="Отправить",
            command=self._send_message,
            bg="#4CAF50",
            fg="white",
            font=self.font,
            relief=tk.FLAT,
            padx=15
        )
        send_button.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Информационная метка
        info_label = ttk.Label(
            input_container, 
            text="Ctrl+Enter для отправки",
            font=("Arial", 8),
            foreground="#666666"
        )
        info_label.pack(side=tk.BOTTOM, anchor=tk.E)
        
        # Фокус на поле ввода
        self.input_field.focus_set()

    def _clear_placeholder(self, event):
        """Очищает подсказку при фокусе"""
        if self.input_field.get("1.0", "end-1c") == "Введите ваше сообщение здесь...":
            self.input_field.delete("1.0", tk.END)
            self.input_field.config(fg="black")

    def _send_message(self, event=None):
        """Отправка сообщения"""
        message = self.input_field.get("1.0", "end-1c").strip()
        
        if message and message != "Введите ваше сообщение здесь...":
            self._display_message(f"Вы: {message}")
            self.input_field.delete("1.0", tk.END)
            # Здесь можно добавить обработку сообщения
            self.app.process_message(message)

    def _display_message(self, message):
        """Отображение сообщения в чате"""
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, message + "\n\n")
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.see(tk.END)

    def run(self):
        self.root.mainloop()

# Пример использования
# if __name__ == "__main__":,
# dialog = TextDialog("Текстовый диалог")
# dialog._display_message("Система: Добро пожаловать!")
# dialog._display_message("Система: Что вас интересует ")
# dialog._display_message("Система: Используйте Ctrl+Enter для отправки")
# dialog.run()