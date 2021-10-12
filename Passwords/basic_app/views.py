from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from basic_app.forms import UserProfileInfoForm
from basic_app.forms import UserProfileForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(req):
    return render(req, 'basic_app/index.html')


# @login_required        # this decorator will impose the "login" to be necesary before visiting logout() view
def user_special(req):
    # logout(req, user)
    return HttpResponse("Special Page")

# this decorator will impose the "login" to be necesary before visiting logout() view
@login_required       
def user_logout(req):
    logout(req)
    return HttpResponseRedirect(reverse('index'))
    # return HttpResponse("Logged out.")






def user_login(req):

    if req.method == 'POST':
        # get username and password from the login.html
        username = req.POST.get('username')
        password = req.POST.get('password')
        
        # this will automatically authenticate this user if it exists in our DB
        user = authenticate(username = username, password = password)

        # if user present in the DB
        if user:
            # if the user is currently active
            if user.is_active:
                # login the user to the site
                login(req, user)
                # redirect the to index..html
                return HttpResponseRedirect(reverse('index'))
            else:
                # user is not active
                return HttpResponse("Account not active!")
        else:
            # user not found in the DB
            print("Failed login. Username: ", username, "password: ", password)
            return HttpResponse("Account not found in te DB!!!")
    else:
        # the method is not POST i.e, the form isnt submitted yet
        return render(req, 'basic_app/login.html',{})
    # now lets see how we can impose that some pages will require login before visiting, using the logout() view
    # then, we'll seup the urls in project and then app




def register(req):

    registered = False

    if req.method == 'POST':

        # get data that UserProfileForm posted
        user_form = UserProfileInfoForm(data = req.POST)
        # get data that UserProfileInfoForm posted
        profile_form = UserProfileForm(data = req.POST)

        # check if the posted data in both forms is valid
        if user_form.is_valid() and profile_form.is_valid():

            # save data from the user_form form
            user = user_form.save()
            # encrypt the password
            user.set_password(user.password)
            # save data again
            user.save()
            
            # save the data from profile_form form but don't commit to DB            
            profile = profile_form.save(commit = False)
            # save 'user' data from the data saved though user_form
            profile.user = user 
            # check if the form has a profile_pic attached and save
            if 'profile_pic' in req.FILES:
                profile.profile_pic = req.FILES['profile_pic']
            profile.save()
            # flag the page to registered so that 
                # the "Tq for registering" page cacn show up
            registered = True
        else:
            # if forms POST data not valid
            print(user_form.errors, profile_form.errors)
    else:
        # if not a POST req:
                # make instances of the forms to display on the webPage
        user_form = UserProfileInfoForm()
        profile_form = UserProfileForm()
        print(user_form)

    return render(req, 'basic_app/registration.html', {
                                    'user_form': user_form,
                                     'profile_form':profile_form,
                                     'registered':registered
                                    })

