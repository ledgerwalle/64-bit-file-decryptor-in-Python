import base64
import sys
import os

def decode_and_save(input_file):
    try:
        # Открываем файл с закодированным текстом для чтения
        with open(input_file, 'r', encoding='utf-8-sig') as file:
            encoded_lines = file.readlines()

        # Декодируем Base64 для каждой строки
        decoded_lines = [base64.b64decode(line.encode()).decode('utf-8') for line in encoded_lines]

        # Создаем имя для выходного файла
        output_file = os.path.splitext(os.path.basename(input_file))[0] + '_decoded.txt'

        # Сохраняем раскодированный текст в выходной файл
        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(decoded_lines)

        print(f"Раскодированный текст сохранен в файле: {output_file}")

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        input_file_path = 'nvram.bak'
    elif len(sys.argv) == 2:
        input_file_path = sys.argv[1]
    else:
        print("Использование: python decode_script.py [путь_к_файлу]")
        sys.exit(1)

    decode_and_save(input_file_path)
