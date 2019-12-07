from flask import Flask, session, request, render_template, escape
app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'dfh_sgawy2L"F4Q8z\n\xec]/'

@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':

        if request.form['login'] == session['username']:
            return {"status": "error", "inf": "logged in"}

        login = request.form['login']
        password = request.form['password']

        if check_login(login):
            return {"status": "error", "inf": "login is in the system"}

        database = login, password
        session['username'] = request.form['login']
        return {"status": "ok"}

    # else: return render_template('registration.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['login'] == session['username']:
            return {"status": "error", "inf": "logged in"}

        if request.form['login'] == request.form['password']:
            session['username'] = request.form['login']
            return {"status": "error", "inf": "logged in"}

    # else: return render_template('login.html')


@app.route('/votings/<int:voting_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def votings(voting_id):
    # Получение информации
    if request.method == 'GET':
        pass

    # Создание голосования
    if request.method == 'POST':
        return creat_voting()

    # Изменение информации
    if request.method == 'PUT':
        pass

    # Удаление запроса
    if request.method == 'DELETE':
        pass

    return request('')


@app.route('/votings/<int:voting_id>/answers/<int:ansver_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def answers(voting_id, ansver_id):
    # Получение информации ответа
    if request.method == 'GET':
        pass

    # Создание ответа
    if request.method == 'POST':
        pass

    # Изменение информации ответа
    if request.method == 'PUT':
        pass

    # Удаление ответа
    if request.method == 'DELETE':
        pass

    return request('')