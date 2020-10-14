from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField


def test(questions, answers):
    class TestForm(FlaskForm):
        pass
    for i in range(len(questions)):
        question = RadioField(questions[i],
                              choices=[(points, answer) for answer, points in answers[i].items()],
                              coerce=int)
        setattr(TestForm, 'question'+str(i), question)
    setattr(TestForm, 'submit', SubmitField('Get Results.'))
    return TestForm
