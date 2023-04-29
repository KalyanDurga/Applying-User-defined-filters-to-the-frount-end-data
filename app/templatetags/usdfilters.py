from django import template

register=template.Library()

def vowel(value):
    v='AEIOUaeiou'
    n=0
    for i in value:
        if i in v:
            n+=1
    return n
@register.filter()
def remove(v,n):
    return v.replace(n,'')


@register.filter()
def counting(v,n):
    c=0
    for i in range(len(v)):
        if v[i:i+len(n)]==n:
            c+=1
    return c


register.filter('vowel',vowel)