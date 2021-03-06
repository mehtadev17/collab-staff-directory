from django.conf.urls import patterns, url

urlpatterns = patterns('staff_directory.views',
                       url(r'^$', 'index', name='index'),
                       url(r'^office/(?P<title>.*)/tags/(?P<tag_slugs>[0-9a-zA-Z/\-]+)/$',
                           'org_group', name='org_group_with_tags'),
                       url(r'^office/(?P<title>.*)/$',
                           'org_group', name='org_group'),
                       url(r'^person/(?P<stub>.*)/thanks/$',
                           'thanks', name='thanks'),
                       url(r'^person/(?P<stub>.*)/$',
                           'person_profile', name='person'),
                       url(r'^thanks/$', 'show_thanks', name='show_thanks'),
                       url(r'^add-person-to-tag/(?P<tag>[^/]+)/', 'add_person_to_tag',
                           name='add_person_to_tag'),
                       url(r'^add/tag/(?P<person_stub>[^/]+)/$', 'add_tag',
                           name='add_tag'),
                       url(r'^add/tag/(?P<person_stub>[^/]+)/(?P<tag>[^/]+)/$',
                           'add_tag', name='add_tag'),
                       url(r'^remove/tag/(?P<person_stub>[^/]+)/(?P<tag_slug>[^/]+)/' +
                           '(?P<tag_category>[^/]+)/$', 'remove_tag',
                           name='remove_tag'),
                       url(r'^tags/(?P<tag_slugs>[0-9a-zA-Z/\-_]+)/$', 'show_by_tag',
                           name='show_by_tag'),
                       url(r'^tags/$', 'show_by_tag',
                           name='show_by_tag'),
                       url(r'^tagged-with-emails/(?P<tag_slugs>[0-9a-zA-Z/\-_, ]+)/$',
                           'show_tag_emails', name='show_tag_emails'),
                       )
