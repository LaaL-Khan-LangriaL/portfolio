from adminPanel.models import About, Experience, Education, LangSkill, Portfolios, Recommendations, SocialMedia,\
userBlog
from adminPanel.forms import AboutForm, ExperienceForm, EducationForm, LangSkillForm, PortfoliosForm,\
    RecommendationsForm, SocialMediaForm, UserForm, BlogForm

from django.contrib.auth import authenticate,  login as auth_login, logout
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from adminPanel.decorators import unauthenticated_user, allowed_users
from django.contrib import messages

# Create your views her


@login_required(login_url='/user_login')
# @allowed_users(allowed_roles=[])
def adminHome(request):
    return render(request, 'HomeAdmin.html')


@unauthenticated_user
def UserRegister(request):
    if request.method == 'POST':
        URFM = UserForm(request.POST, request.FILES)
        if URFM.is_valid():
            URFM.save()
            user = URFM.cleaned_data.get('username')
            messages.success(request, f'Hey !  {user} your account created successfully')
            return redirect('/user_login')
    else:
        URFM = UserForm()
    return render(request, 'User_Register.html',{'form': URFM})


@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.info(request, f'Welcome to your portfolio {user}')
            return redirect('/admin')
        else:
            messages.error(request, 'Username or password is incorrect')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    messages.info(request, 'You are logged out !')
    return redirect('/user_login')


def adminAbout(request):
    if request.method == 'POST':
        ABFM = AboutForm(request.POST, request.FILES)
        if ABFM.is_valid():
            FN = ABFM.cleaned_data['fullName']
            DSG = ABFM.cleaned_data['Designation']
            STR = ABFM.cleaned_data['street']
            AOR = ABFM.cleaned_data['areaofResearch']
            PJ = ABFM.cleaned_data['previousJob']
            SCH = ABFM.cleaned_data['School']
            NAT = ABFM.cleaned_data['Nationality']
            MS = ABFM.cleaned_data['meritalStatus']
            BD = ABFM.cleaned_data['Birthday']
            SK = ABFM.cleaned_data['Skype']
            EM = ABFM.cleaned_data['Email']
            PH = ABFM.cleaned_data['Phone']
            DSC = ABFM.cleaned_data['description']
            RSM = ABFM.cleaned_data['resume']
            PR = ABFM.cleaned_data['profile']
            reg = About(fullName=FN, Designation=DSG, street=STR, areaofResearch=AOR, previousJob=PJ,
                        School=SCH, Nationality=NAT, meritalStatus=MS, Birthday=BD, Skype=SK,
                        Email=EM, Phone=PH, description=DSC, resume=RSM, profile=PR)
            reg.save()
            ABFM = AboutForm()
    else:
        ABFM = AboutForm()
    ABTMD = About.objects.all()
    return render(request, 'adminAbout.html', {'form': ABFM, 'ABTMD': ABTMD})


def adminExperience(request):
    if request.method == 'POST':
        EXPFM = ExperienceForm(request.POST, request.FILES)
        if EXPFM.is_valid():
            DSG = EXPFM.cleaned_data['Designation']
            FRM = EXPFM.cleaned_data['From']
            TO = EXPFM.cleaned_data['To']
            CMP = EXPFM.cleaned_data['Company']
            STR = EXPFM.cleaned_data['Street']
            DESC = EXPFM.cleaned_data['Description']
            reg = Experience(Designation=DSG, From=FRM, To=TO, Company=CMP, Street=STR,
                             Description=DESC)
            reg.save()
            EXPFM = ExperienceForm()
    else:
        EXPFM = ExperienceForm()
    data = Experience.objects.all()
    return render(request, 'adminExperience.html', {'form': EXPFM, 'EXPdata': data})


def adminEducation(request):
    if request.method == 'POST':
        EDUFM = EducationForm(request.POST, request.FILES)
        if EDUFM.is_valid():
            SC = EDUFM.cleaned_data['School']
            SA = EDUFM.cleaned_data['StudyArea']
            FRM = EDUFM.cleaned_data['From']
            TO = EDUFM.cleaned_data['To']
            EI = EDUFM.cleaned_data['Icon']
            reg = Education(School=SC, From=FRM, To=TO, StudyArea=SA, Icon=EI)
            reg.save()
            EDUFM = EducationForm()
    else:
        EDUFM = EducationForm()
    data = Education.objects.all()
    return render(request, 'adminEducation.html', {'form': EDUFM, 'EDUdata': data})


def SkillsLang(request):
    if request.method == 'POST':
        SLFM = LangSkillForm(request.POST, request.FILES)
        if SLFM.is_valid():
            SK1 = SLFM.cleaned_data['skill1']
            EXPRT1 = SLFM.cleaned_data['expert1']
            SK2 = SLFM.cleaned_data['skill2']
            EXPRT2 = SLFM.cleaned_data['expert2']
            SK3 = SLFM.cleaned_data['skill3']
            EXPRT3 = SLFM.cleaned_data['expert3']
            SK4 = SLFM.cleaned_data['skill4']
            EXPRT4 = SLFM.cleaned_data['expert4']
            SK5 = SLFM.cleaned_data['skill5']
            EXPRT5 = SLFM.cleaned_data['expert5']
            SK6 = SLFM.cleaned_data['skill6']
            EXPRT6 = SLFM.cleaned_data['expert6']
            SK7 = SLFM.cleaned_data['skill7']
            EXPRT7 = SLFM.cleaned_data['expert7']
            SK8 = SLFM.cleaned_data['skill8']
            EXPRT8 = SLFM.cleaned_data['expert8']
            LANG1 = SLFM.cleaned_data['lang1']
            STR1 = SLFM.cleaned_data['str1']
            LANG2 = SLFM.cleaned_data['lang2']
            STR2 = SLFM.cleaned_data['str2']
            LANG3 = SLFM.cleaned_data['lang3']
            STR3 = SLFM.cleaned_data['str3']
            icon1  = SLFM.cleaned_data['Icon1']
            icon2  = SLFM.cleaned_data['Icon2']
            icon3  = SLFM.cleaned_data['Icon3']
            reg = LangSkill(skill1=SK1, skill2=SK2, skill3=SK3, skill4=SK4, skill5=SK5, skill6=SK6, skill7=SK7,
                            skill8=SK8, lang1=LANG1, lang2=LANG2, lang3=LANG3, Icon1=icon1, Icon2=icon2, Icon3=icon3,
                            expert1=EXPRT1, expert2=EXPRT2, expert3=EXPRT3, expert4=EXPRT4, expert5=EXPRT5,
                            expert6=EXPRT6, expert7=EXPRT7, expert8=EXPRT8, str1=STR1, str2=STR2, str3=STR3)
            reg.save()
            SLFM = LangSkillForm()
    else:
        SLFM = LangSkillForm()
    SLdata = LangSkill.objects.all()
    return render(request, 'adminLanguageSkills.html', {'form': SLFM, 'SLdata': SLdata})


def portfolios(request):
    if request.method == 'POST':
        PFFM = PortfoliosForm(request.POST, request.FILES)
        if PFFM.is_valid():
            LNK = PFFM.cleaned_data['link']
            THMBNL = PFFM.cleaned_data['thumbnail']
            reg = Portfolios(link=LNK, thumbnail=THMBNL)
            reg.save()
            PFFM = PortfoliosForm()
    else:
        PFFM = PortfoliosForm()
    PFdata = Portfolios.objects.all()
    return render(request, 'adminPortfolios.html', {'form': PFFM, 'PFdata': PFdata})


def recommendation(request):
    if request.method == 'POST':
        RECFM = RecommendationsForm(request.POST, request.FILES)
        if RECFM.is_valid():
            PER = RECFM.cleaned_data['person']
            DESG = RECFM.cleaned_data['designation']
            DESC = RECFM.cleaned_data['description']
            reg = Recommendations(person=PER, designation=DESG, description=DESC)
            reg.save()
            RECFM = RecommendationsForm()
    else:
        RECFM = RecommendationsForm()
    RECdata = Recommendations.objects.all()
    return render(request, 'adminRecommendations.html', {'form': RECFM, 'RECdata': RECdata})


def user_blog(request):
    if request.method == 'POST':
        BLGFM = BlogForm(request.POST, request.FILES)
        if BLGFM.is_valid():
            TIT = BLGFM.cleaned_data['title']
            HD = BLGFM.cleaned_data['heading']
            Icn = BLGFM.cleaned_data['Icon']
            DSC = BLGFM.cleaned_data['description']
            CRA = BLGFM.cleaned_data['created_at']
            reg = userBlog(title=TIT, heading=HD, Icon=Icn, description=DSC, created_at=CRA)
            reg.save()
            BLGFM = BlogForm()
    else:
        BLGFM = BlogForm()
    BLGdata = userBlog.objects.all()
    return render(request, 'adminBlog.html', {'form': BLGFM, 'BLGdata': BLGdata})


def social_media(request):
    if request.method == 'POST':
        SMFM = SocialMediaForm(request.POST, request.FILES)
        if SMFM.is_valid():
            EM = SMFM.cleaned_data['email']
            SK = SMFM.cleaned_data['skype']
            PH = SMFM.cleaned_data['phone']
            GIT = SMFM.cleaned_data['github']
            LIK = SMFM.cleaned_data['linkedin']
            GP = SMFM.cleaned_data['google_plus']
            YTB = SMFM.cleaned_data['youtube']
            WEB = SMFM.cleaned_data['website']
            reg = SocialMedia(email=EM, skype=SK, phone=PH, github=GIT, linkedin=LIK, google_plus=GP, youtube=YTB,
                              website=WEB)
            reg.save()
            SMFM = SocialMediaForm()
    else:
        SMFM = SocialMediaForm()
    SMdata = SocialMedia.objects.all()
    return render(request, 'adminSocialmedia.html', {'form': SMFM, 'SMdata': SMdata})


def Delete(request, id, type):
    if type == 'about':
        DELLABT = About.objects.get(id=id)
        DELLABT.delete()
        return redirect('/about')

    if type == 'experience':
        DELLEXP = Experience.objects.get(id=id)
        DELLEXP.delete()
        return redirect('/experience')

    if type == 'education':
        DELLEDU = Education.objects.get(id=id)
        DELLEDU.delete()
        return redirect('/education')

    if type == 'language_skills':
        DELLLNSK = LangSkill.objects.get(id=id)
        DELLLNSK.delete()
        return redirect('/languageskills')

    if type == 'portfolios':
        DELLPF = Portfolios.objects.get(id=id)
        DELLPF.delete()
        return redirect('/portfolios')

    if type == 'recommendation':
        DELLREC = Recommendations.objects.get(id=id)
        DELLREC.delete()
        return redirect('/recommendation')

    if type == 'blog':
        DELLBLG = userBlog.objects.get(id=id)
        DELLBLG.delete()
        return redirect('/user_blog')

    if type == 'socialMedia':
        DELLSM = SocialMedia.objects.get(id=id)
        DELLSM.delete()
        return redirect('/socialmedia')


def Update(request, id, type):
    if type == 'about':
        if request.method =='POST':
            UPABT = About.objects.get(id=id)
            ABTFM = AboutForm(request.POST, request.FILES, instance=UPABT)
            if ABTFM.is_valid():
                ABTFM.save()
                ABTFM = AboutForm()
                return redirect('/about')
        else:
            UPABT = About.objects.get(id=id)
            ABTFM = AboutForm(instance=UPABT)
        return render(request, 'Update/updateAbout.html', {'form': ABTFM})

    if type == 'experience':
        if request.method =='POST':
            UPEXP = Experience.objects.get(id=id)
            EXPFM = ExperienceForm(request.POST, request.FILES, instance=UPEXP)
            if EXPFM.is_valid():
                EXPFM.save()
                EXPFM = ExperienceForm()
                return redirect('/experience')
        else:
            UPEXP = Experience.objects.get(id=id)
            EXPFM = ExperienceForm(instance=UPEXP)
        return render(request, 'Update/updateExperience.html', {'form': EXPFM})

    if type == 'education':
        if request.method =='POST':
            UPEDU = Education.objects.get(id=id)
            EDUFM = EducationForm(request.POST, request.FILES, instance=UPEDU)
            if EDUFM.is_valid():
                EDUFM.save()
                EDUFM = EducationForm()
                return redirect('/education')
        else:
            UPEDU = Education.objects.get(id=id)
            EDUFM = EducationForm(instance=UPEDU)
        return render(request, 'Update/updateEducation.html', {'form': EDUFM})

    if type == 'language_skills':
        if request.method =='POST':
            UPLNSK = LangSkill.objects.get(id=id)
            LNSKFM = LangSkillForm(request.POST, request.FILES, instance=UPLNSK)
            if LNSKFM.is_valid():
                LNSKFM.save()
                LNSKFM = EducationForm()
                return redirect('/languageskills')
        else:
            UPLNSK = LangSkill.objects.get(id=id)
            LNSKFM = LangSkillForm(instance=UPLNSK)
        return render(request, 'Update/updateLanguage_Skills.html', {'form': LNSKFM})

    if type == 'portfolios':
        if request.method =='POST':
            UPPF = Portfolios.objects.get(id=id)
            PFFM = PortfoliosForm(request.POST, request.FILES, instance=UPPF)
            if PFFM.is_valid():
                PFFM.save()
                PFFM = PortfoliosForm()
                return redirect('/portfolios')
        else:
            UPPF = Portfolios.objects.get(id=id)
            PFFM = PortfoliosForm(instance=UPPF)
        return render(request, 'Update/updatePortfolios.html', {'form': PFFM})

    if type == 'recommendation':
        if request.method == 'POST':
            UPREC = Recommendations.objects.get(id=id)
            RECFM = RecommendationsForm(request.POST, request.FILES, instance=UPREC)
            if RECFM.is_valid():
                RECFM.save()
                RECFM = RecommendationsForm()
                return redirect('/recommendation')
        else:
            UPREC = Recommendations.objects.get(id=id)
            RECFM = RecommendationsForm(instance=UPREC)
        return render(request, 'Update/updateRecommendations.html', {'form': RECFM})

    if type == 'blog':
        if request.method == 'POST':
            BLGREC = userBlog.objects.get(id=id)
            BLGFM = BlogForm(request.POST, request.FILES, instance=BLGREC)
            if BLGFM.is_valid():
                BLGFM.save()
                BLGFM = BlogForm()
                return redirect('/user_blog')
        else:
            BLGREC = userBlog.objects.get(id=id)
            BLGFM = BlogForm(instance=BLGREC)
        return render(request, 'Update/updateBlog.html', {'form': BLGFM})

    if type == 'socialMedia':
        if request.method == 'POST':
            UPSM = SocialMedia.objects.get(id=id)
            SMFM = SocialMediaForm(request.POST, request.FILES, instance=UPSM)
            if SMFM.is_valid():
                SMFM.save()
                SMFM = SocialMedia()
                return redirect('/socialmedia')
        else:
            UPSM = SocialMedia.objects.get(id=id)
            SMFM = SocialMediaForm(instance=UPSM)
        return render(request, 'Update/updateSocialMedia.html', {'form': SMFM})