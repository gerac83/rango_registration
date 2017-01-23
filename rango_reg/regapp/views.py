from django.shortcuts import render
from regapp.forms import UserForm, GithubForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from regapp.models import UserProfile, GitHub

mail_domain = "@gmail.com"

def send_email(to_id, subject, message):
    import smtplib
    from email.mime.text import MIMEText

    msg = MIMEText(message)

    me = 'itech.msc@gmail.com'
    your = to_id+mail_domain
    msg['Subject'] = subject
    msg['From'] = 'itech.msc@gmail.com'
    msg['To'] = to_id+mail_domain

    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    s.login("itech.msc@gmail.com", "xxxxx")
    s.sendmail(me, [you], msg.as_string())
    s.close()
    print 'successfully sent the mail'

def index(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()
    return render(request, 'regapp/index.html',
        {'user_form': user_form, 'registered': registered})

@login_required
def thanks(request, context_dict):
    return HttpResponse("Thanks! You should receive shortly a confirmation e-mail!")

@login_required
def github(request):
    form = GithubForm()
    current_user = request.user.username
    githubQ = False
    if request.method == 'POST':
        form = GithubForm(request.POST)
        if form.is_valid():
            githubQ = True
            page = form.save(commit=False)
            ghobj = GitHub.objects.filter(userid=current_user)
            if ghobj:
                print current_user
                savemodel = GitHub(pk=ghobj[0].pk, userid=current_user, url=page.url)
                # ghobj.url = page.url
                savemodel.save()
                # E-mail update here
                # try:
                #     send_email(current_user, "[RangoApp] Update!", "Your GitHub URL has been updated with: "+page.url)
                # except:
                #     pass
            else:
                page.userid = current_user
                page.save()
                # Send e-mail here
                # try:
                #     send_email(current_user, "[RangoApp] Success!", "Your GitHub URL has been added to our database. URL: "+page.url)
                # except:
                #     pass
        else:
            print form.errors

    ghobj = GitHub.objects.filter(userid=current_user)
    if len(ghobj) == 0:
        giturl = 'None'
    else:
        giturl = ghobj[0].url
    context_dict = {'form':form, 'gitadded': githubQ, 'github_url': giturl}
    return render(request, 'regapp/github.html', context_dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('github'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'regapp/login.html', {})
