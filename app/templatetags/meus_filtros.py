from django import template

register = template.Library()


@register.filter(name='addclass')
def addclass(value, arg):
    # método que recebe uma classe como parâmetro e aplica a classe na tag html
    return value.as_widget(attrs={'class': arg})
