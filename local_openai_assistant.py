import openai
import json
import os

# Получаем ключ API из переменной окружения
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("Необходимо установить переменную окружения OPENAI_API_KEY")

openai.api_key = api_key

# Функция для вызова модели ChatGPT
def call_chatgpt(prompt, model="text-davinci-003", temperature=0.5, max_tokens=150):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        timeout=10,
    )
    return response.choices[0].text.strip()

# Функция для сохранения данных локально
def save_to_file(data, filename="responses.json"):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            existing_data = json.load(file)
    else:
        existing_data = []

    existing_data.append(data)

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)

# Пример использования
if __name__ == "__main__":
    prompt = "Привет! Как я могу помочь вам сегодня?"
    response = call_chatgpt(prompt)
    print(response)
    
    data_to_save = {
        "prompt": prompt,
        "response": response
    }
    
    save_to_file(data_to_save)
