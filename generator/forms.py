from django import forms

GRID_SIZE_CHOICE = (
    ('3', '3x3'),
    ('4', '4x4'),
    ('5', '5x5'),
)

TIME_RANGE_CHOICE = (
    ('long_term', 'Overall'),
    ('medium_term', 'Past 6 months'),
    ('short_term', 'Past 4 weeks'),
)

class TokenForm(forms.Form):
    code = forms.CharField(label='', max_length=500)

class ParamForm(forms.Form):

    grid_size = forms.CharField(label='Dimension:', max_length=6,
        widget=forms.Select(choices=GRID_SIZE_CHOICE))
    time_range = forms.CharField(label='Time:', max_length=20,
        widget=forms.Select(choices=TIME_RANGE_CHOICE))

class DownloadForm(forms.Form):
    pass
