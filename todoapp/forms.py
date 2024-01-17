class TodoForm(forms.ModelForm):

    class Meta:

        model = Todo

        fields = "_all_"