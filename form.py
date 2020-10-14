from flask_wtf import FlaskForm
from wtforms import SelectField, RadioField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class EncoderForm(FlaskForm):
    type_cipher = SelectField('Cipher type', coerce=int, choices=[(0, 'Affine Caesar'), (1, 'Atbash')])
    en_de = RadioField('Encode or Decode', coerce=int, choices=[(0, 'Encode'), (1, 'Decode')])
    field1 = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField()
