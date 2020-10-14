from flask import Flask, render_template, redirect, url_for, request
import random
import math
from datetime import datetime
from static.oracle import *
from config import Config
from forms import MessageForm
from prog import *
from prog_form import *
from static.proj1.atbash import encrypt_atbash
from static.proj1.athens_caesar import encrypt_athens_caesar, decrypt_athens_caesar
from static.proj1.const import *

app = Flask(__name__)
app.config.from_object(Config)
a = 2
b = 3
r = 5
pi = math.pi
books = {}


def get_dif(*args):
    d = args[0]
    for v in range(1, len(args)):
        d -= args[v]
    return d


def roll():
    return random.randint(1, 6)


def eval1(to_eval: str, c: int, d: int):
    to_eval.replace('a', str(a)).replace('b', str(b))
    return eval(to_eval)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f'Name: {self.name}, age: {self.age}.'


p1 = Person('Ivan', '23')


def shrodinger1(a: int, b: int, c):
    if c == '/' and b == 0:
        return 'Mistake'
    else:
        if c == 'cat':
            return 'Schrödinger\'s'
        elif 'cat' in c:
            if b == 0:
                return 'Can divide by zero, meow.'
            else:
                return 'Simple calculation.'


def time_sir():
    curr_time = datetime.now()
    c = int(curr_time.strftime("%H"))
    d = int(curr_time.strftime("%M"))
    c += d // 60
    d = d % 60
    c = c % 12
    if d == 15:
        minutes = 'Пятнадцать минут '
        hours = f'{c+1}'
    elif d == 45:
        minutes = 'Без пятнадцати '
        hours = f'{c + 1}'
    elif d == 0:
        minutes = 'Ровно '
        hours = f'{c}'
    elif d == 30:
        minutes = 'Половина '
        hours = f'{c+1}'
    elif d < 15:
        minutes = 'Начало '
        hours = f'{c+1}'
    else:
        minutes = f'{c} час(а/ов) {d} минут(а/ы)'
        hours = ''
    text = minutes + hours
    return text


@app.route('/cipher', methods=['GET', 'POST'])
def cipher():
    form = EncoderForm()
    if form.validate_on_submit():
        received_text = ''
        text = form.field1.data.lower()
        try:
            if form.type_cipher.data == 0:
                received_text = encrypt_atbash(text)
            elif form.type_cipher.data == 1:
                if form.en_de.data == 0:
                    received_text = encrypt_athens_caesar(text, 3, 5)
                elif form.en_de.data == 1:
                    received_text = decrypt_athens_caesar(text, 3, 5)
        except IndexError:
            received_text = 'Incorrect Symbols. Use A-Z'
        return render_template('cipher.html', form=form, recieved=received_text)
    return render_template('cipher.html', form=form)


@app.route('/<test_type>_test/', methods=['GET', 'POST'])
def prog_test(test_type):
    if test_type == 'programmer':
        desc = test_d
        form = test(test_q, test_a)
        number_pts = 0
        result = ''
        if request.method == 'POST':
            for i in range(len(test_q)):
                number_pts += form['question' + str(i)].data
            for title, points in test_r.items():
                if number_pts >= points:
                    result = f'Wow, you got {number_pts}. You are a real {title}.'
                    break
        return render_template('test.html', description=desc, form=form, result=result)
    else:
        return redirect(url_for('main_page'))


@app.route('/form2', methods=['get', 'post'])
def form2():
    form = MessageForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        print(name)
        print(email)
        print(message)
        print('\nInfo recieved, now redirecting...')
        return redirect(url_for('form2'))
    return render_template('message.html', form=form)


@app.route('/form1', methods=['get', 'post'])
def form1():
    global books
    name = ''
    desc = ''
    if request.method == 'POST':
        name = request.form.get('name')
        desc = request.form.get('desc')
        books[name] = desc
    message = books

    return render_template('form1.html', message=message)


@app.route('/crystal')
def crystal():
    oracle1 = oracle()
    color_oracle = oracle_color(oracle1)
    return render_template('crystall.html', oracle=oracle1, color1=color_oracle)


@app.route('/403')
def a403():
    return render_template('403404.html')


@app.route('/404')
def a404():
    return render_template('404.html')


@app.route('/404b')
def b404():
    return render_template('404b.html', time_sir=time_sir, cat=lambda a, b, c: shrodinger1(a, b, c))


@app.route('/extending')
def extends1():
    return render_template('extends.html')


@app.route('/401402')
def a401402():
    return render_template('401402.html', roll=roll, eval1=lambda ela='5*a-(3+b**3)/4': eval1(to_eval=ela, c=a, d=b),
                           get_dif=lambda: get_dif(a, b, 5), pi=pi, r=r, person=p1, a=a, b=b)


@app.route('/quest/')
def quest_index():
    global history
    history = {}
    return render_template('quest_main.html')


@app.route('/quest/<int:step>:<int:choice>')
def quest_part(step, choice):
    global history
    message = ''
    if step == 0:
        message = "There are 2 roads before you. "\
                  "Go left - you will find gold, go right - you will lose your horse. " \
                  "Shall we go left?"
    elif step == 1:
        if choice == 1:
            message = 'You found a gold coin. Apparently, someone has already managed to steal the rest. ' \
                      'Are you going on a chase?'
        else:
            message = 'It\'s a good thing you are without a horse. ' \
                      'But here one grazes, so now you\'re on horseback. ' \
                      'Shall we start again?'
        history['1'] = choice
    elif step == 2:
        if history['1'] == 0:
            if choice == 1:
                return redirect(url_for('quest_index'))
            else:
                return redirect(url_for('quest_part', step=1, choice=0))
        else:
            if choice == 1:
                message = 'Three days and three nights you relentlessly followed the tracks. ' \
                          'In the morning, exhausted by thirst, you came to Baba-Yaga\'s swamps. ' \
                          'She gave you a drink, fattened you up and married you to Vasilisa the Beautiful. ' \
                          'Finally, she shared her loot, so you are now a member of the fairytale mafia. ' \
                          'Shall we start again?'
            else:
                message = 'Leaving the horizon you came across a village of dwarves. ' \
                          'Looking at the coin you were flipping, they thought you were a robber. ' \
                          'Now you are going to be enslaved at gold mines, but you will literally live in gold. ' \
                          'Shall we start again?'
        history['2'] = choice
    elif step == 3:
        if choice == 0 and history['2'] == 0:
            return redirect(url_for('quest_part', step=2, choice=0))
        elif choice == 0 and history['2'] == 1:
            return redirect(url_for('quest_part', step=2, choice=1))
        else:
            return redirect(url_for('quest_index'))
    step += 1
    return render_template('quest_part.html', step=step, message=message)


@app.route('/translit/')
def translit():
    return render_template('translit.html')


@app.route('/')
def main_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
