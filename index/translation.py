from modeltranslation.translator import TranslationOptions, register
from . import models

@register(models.About)
class AboutTranslate(TranslationOptions):
    fields=['firstname','lastname','biography','address']

@register(models.Experience)
class ExperienceTranslate(TranslationOptions):
    fields=['title','company','description']

@register(models.Education)
class EducationTranslate(TranslationOptions):
    fields=['title','orientation','description',]

@register(models.Workflow)
class WorkflowTranslate(TranslationOptions):
    fields=['title']

@register(models.Interests)
class InterestsTranslate(TranslationOptions):
    fields=['description']

@register(models.Awards)
class AwardsTranslate(TranslationOptions):
    fields=['description']