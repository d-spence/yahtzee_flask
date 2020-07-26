from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length


class CategoryForm(FlaskForm):
    """Form for selecting a scoring category during the game"""

    category = SelectField('Select Category', validators=[DataRequired()])
    submit = SubmitField('Submit Category')

    def update_categories(self, cats=[('none', 'No Category')]):
        """Get available categories; cats is a list"""

        self.category.choices = cats #[(cats[0], cats[1]) for ]


# TODO -> Add form class to choose number of players for game or use buttons (1-4 players)