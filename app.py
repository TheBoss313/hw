from flask import Flask, render_template, redirect, url_for, request
from config import Config
from forms import MessageForm
from prog import *
from prog_form import *
from static.proj1.atbash import encrypt_atbash
from static.proj1.athens_caesar import encrypt_athens_caesar, decrypt_athens_caesar
from static.proj1.const import *

app = Flask(__name__)
app.config.from_object(Config)

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


@app.route('/')
def main_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
