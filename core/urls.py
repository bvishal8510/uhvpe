from django.conf.urls import url
from .views import (IndexView, DirectorMessageView, UHVPESyllabus, GuidelineView, SociallyRelevantProjectView,
                    BookView, FAQView, JourneySoFarView, ImpactView, FuturePlansView, NodalCenterView, PresentationView,
                    NoteView, QuestionPaperView, PracticeSessionView, PosterView, CircularView, VideoLectureView,
                    ContactView, WorkshopRegistrationView, EventRegistrationView, PastWorkshopDetailView,
                    UHVPEProgramView, DeveloperView)

urlpatterns = [
    url(r'^director-message/$', DirectorMessageView.as_view(), name='director-message'),
    url(r'^syllabus/$', UHVPESyllabus.as_view(), name='syllabus'),
    url(r'^guidelines/$', GuidelineView.as_view(), name='guidelines'),
    url(r'^projects/$', SociallyRelevantProjectView.as_view(), name='projects'),
    url(r'^books/$', BookView.as_view(), name='books'),
    url(r'^faq/$', FAQView.as_view(), name='faq'),
    url(r'^journey/$', JourneySoFarView.as_view(), name='journey'),
    url(r'^impact/$', ImpactView.as_view(), name='impact'),
    url(r'^future-plans/$', FuturePlansView.as_view(), name='future'),
    url(r'^nodal-center/$', NodalCenterView.as_view(), name='nodal-center'),
    url(r'^presentation/$', PresentationView.as_view(), name='presentation'),
    url(r'^note/$', NoteView.as_view(), name='note'),
    url(r'^question-paper/$', QuestionPaperView.as_view(), name='question-paper'),
    url(r'^practice-session/$', PracticeSessionView.as_view(), name='practice-session'),
    url(r'^posters/$', PosterView.as_view(), name='poster'),
    url(r'^circulars/$', CircularView.as_view(), name='circular'),
    url(r'^video-lecture/$', VideoLectureView.as_view(), name='video-lecture'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^workshop/$', WorkshopRegistrationView.as_view(), name='workshop'),
    url(r'^event/$', EventRegistrationView.as_view(), name='event'),
    url(r'^past-workshop/$', PastWorkshopDetailView.as_view(), name='past-workshop'),
    url(r'^uhvpe-program/$', UHVPEProgramView.as_view(), name='uhvpe-program'),
    url(r'^developer/$', DeveloperView.as_view(), name='developer'),
    url(r'^$', IndexView.as_view(), name='home'),
]
