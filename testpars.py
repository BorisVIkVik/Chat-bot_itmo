from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# 1. Настройка параметров скачивания
download_dir = os.path.join(os.getcwd(), "pdf_downloads")  # Папка для скачивания
os.makedirs(download_dir, exist_ok=True)  # Создаем папку, если её нет

# 2. Конфигурация Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Работа в фоновом режиме
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True,  # Важно для автоматического скачивания PDF
    "pdfjs.disabled": True  # Отключаем встроенный просмотрщик PDF
})

# 3. Укажите путь к chromedriver
service = Service(executable_path='/path/to/chromedriver')  # Замените на свой путь

# 4. Запуск браузера
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()  # На всякий случай разворачиваем окно

try:
    # 5. Переход на целевую страницу
    driver.get("https://abit.itmo.ru/program/master/ai")  # Замените на реальный URL
    
    # 6. Поиск кнопки по классу и ожидание её кликабельности
    button_class = "ButtonSimple_button_masterProgram__JK8b_"
    button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CLASS_NAME, button_class))
    )
    
    # 7. Прокрутка к кнопке (на всякий случай)
    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    time.sleep(1)  # Небольшая пауза для стабилизации
    
    # 8. Нажатие кнопки
    button.click()
    print("Кнопка найдена и нажата!")
    
    # 9. Ожидание загрузки файла (до 60 секунд)
    print("Ожидание загрузки PDF...")
    downloaded = False
    for _ in range(60):
        files = os.listdir(download_dir)
        pdf_files = [f for f in files if f.lower().endswith('.pdf')]
        
        if pdf_files:
            print(f"Найден PDF файл: {pdf_files[0]}")
            downloaded = True
            break
        
        time.sleep(1)
    
    if not downloaded:
        print("PDF не скачался в течение 60 секунд")
        # Дополнительные действия при ошибке

except Exception as e:
    print(f"Произошла ошибка: {str(e)}")
    # Скриншот для диагностики
    driver.save_screenshot("error_screenshot.png")

finally:
    # 10. Закрытие браузера
    driver.quit()
    print("Браузер закрыт")