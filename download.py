import requests
import os

def download_pdf(url, save_path=None):
    try:
        # Отправляем GET-запрос
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Проверка ошибок HTTP
        
        # Определяем имя файла
        if save_path is None:
            # Извлекаем имя файла из URL
            filename = os.path.basename(url)
            if not filename:
                filename = "downloaded_file.pdf"
            save_path = filename
        
        # Сохраняем файл
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                
        print(f"Файл сохранён как: {save_path}")
        return True
    
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при скачивании: {e}")
        return False

# Пример использования
# download_pdf("https://example.com/document.pdf", "my_file.pdf")