from flask import Flask, request, make_response, redirect, render_template, url_for

# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Устанавливаем секретный ключ для шифрования cookie
app.secret_key = 'supersecretkey'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получаем значения из формы
        name = request.form.get('name')
        email = request.form.get('email')
        
        # Создаем cookie-файл с данными пользователя
        response = make_response(redirect(url_for('welcome')))
        response.set_cookie('name', name)
        response.set_cookie('email', email)
        return response
        
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    # Получаем значения из cookie-файла
    name = request.cookies.get('name')
    email = request.cookies.get('email')
    
    # Проверяем, есть ли данные пользователя в cookie
    if name and email:
        return f'''
        <h1>Привет, {name}!</h1>
        <p>Добро пожаловать на страницу приветствия.</p>
        <form action="/logout" method="POST">
            <input type="submit" value="Выйти">
        </form>
        '''
    else:
        return redirect(url_for('index'))

@app.route('/logout', methods=['POST'])
def logout():
    # Удаляем cookie-файлы с данными пользователя
    response = make_response(redirect(url_for('index')))
    response.delete_cookie('name')
    response.delete_cookie('email')
    return response

if __name__ == '__main__':
    app.run(debug=True)