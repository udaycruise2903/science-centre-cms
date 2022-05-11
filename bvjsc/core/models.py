#from django.core.exceptions import ValidationError
from django.db import models
#from django.http import HttpResponseRedirect
#from django.shortcuts import redirect
#from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel, PageChooserPanel
#from wagtail.contrib.forms.models import AbstractFormField
#from wagtail.core.blocks import ListBlock
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
#from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
#from wagtailcaptcha.models import WagtailCaptchaEmailForm


from bvjsc.core.blocks import HeadingBlock, PictureLinkBlock, SliderBlock, SupporterBlock, TeamMemberBlock
#from bvjsc.events.models import Event
from .blocks import ContentStreamBlock
from .models_abstract import Attachable, MenuTitleable, SendMailMixin, PageDesignMixin


class ContentPage(Page, MenuTitleable, Attachable, PageDesignMixin):
    body = StreamField(ContentStreamBlock(), verbose_name="Page body", blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    subpage_types = []

    content_panels = [
        FieldPanel('title'),
        StreamFieldPanel('body'),
        StreamFieldPanel('attachments'),
    ] + PageDesignMixin.content_panels

    promote_panels = Page.promote_panels + [FieldPanel('menu_title')]

    def title_size(self):
        if len(self.title) > 50:
            return 'small'
        if len(self.title) > 30:
            return 'medium'
        return 'large'

    class Meta:
        verbose_name = 'General Content Page'



class HomePage(Page):
    slider = StreamField([
        ('slider_item', SliderBlock())
    ], blank=True)

    events_photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='This image MUST BE EXACTLY 1400px by 530px',
    )

    parent_page_types = ['wagtailcore.Page']

    search_fields = Page.search_fields + [
    ]

    content_panels = [
        FieldPanel('title'),
        StreamFieldPanel('slider'),
        ImageChooserPanel('events_photo')
    ]

    class Meta:
        verbose_name = 'Home Page'

    def get_context(self, request, *args, **kwargs):
        # Update template context
        context = super(HomePage, self).get_context(request, args, kwargs)
        #context['events'] = Event.objects.future(4)
        #context['news'] = News.objects.news(3)
        return context

    @property
    def has_multiple_slides(self):
        active_slides = 0;
        for slide in self.slider:
            if slide.value['active']:
                active_slides += 1
            if active_slides > 1:
                return True
        return False
