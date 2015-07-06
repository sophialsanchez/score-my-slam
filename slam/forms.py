from django.forms import ModelForm
from slam.models import Slam_session, Judges_scores


class SlamForm(ModelForm):
	class Meta:
		model = Slam_session
		fields = ['slam_name', 'number_of_rounds', 'number_of_judges', 'poet_1', 'poet_2', 'poet_3']

class JudgesForm(ModelForm):
	class Meta:
		model = Judges_scores
		fields = ['score_1', 'score_2', 'score_3', 'score_4', 'score_5']

# class ResponseForm(forms.Form):
# 	response = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'autofocus'}), label='Slam Name', max_length=150, error_messages={'required': 'Hmm...that doesn\'t look quite right. Try a different answer.'})
