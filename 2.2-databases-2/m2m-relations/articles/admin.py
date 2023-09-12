from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag_name']


class ScopeInlineFormset(BaseInlineFormSet):

    def clean(self):
        is_main_check = 0
        for form in self.forms:

            if form.cleaned_data.get('is_main') is True:
                is_main_check += 1

        if is_main_check > 1:
            raise ValidationError('Основной может быть только одна тематика')

        elif is_main_check == 0:
            raise ValidationError('Укажите основную тематику')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag', 'article']
