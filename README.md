MID-Tourism ✈️
==============================
by PT. Maju Indonesia Tourism **[google.com "Find your Tourism needs here!"](https://mid-tourism.herokuapp.com)**

###### What are the instructions to build, run, and deploy the app?
1. **Install Prerequisites**
> [Download Git](https://git-scm.com/downloads) <br>
> [Download Python](https://www.python.org/downloads/) <br>
> [Download IDE](https://www.jetbrains.com/pycharm/promo/?source=google&medium=cpc&campaign=14122963570&term=python%20editor&gclid=CjwKCAjw7p6aBhBiEiwA83fGupTYvWpJtZpacu_aDl69BH9haCoiEb1hkr8rq6L15hpDVdDNvn7pPhoCy4cQAvD_BwE) <br>

2. **Initialize your local environment**
> Clone the repository <br>
> `git clone` <br>
> Create and activate python virtual environment <br>
> `python -m venv env` <br>
> `env\Scripts\activate.bat` <br>
> Install dependencies (requirements.txt) <br>
> `pip install -r requirements.txt` <br>

3. **Branch the Repository**
> Create a new branch for each module <br>
> Push into your branch when done working <br>
> `git push` <br>
> Merge into staging when done <br>
> ***Do not push your work directly to main*** <br>

## Workflow
1. **Preliminaries and Planning**
> Brainstorming session to find potentially useful features to-be-included in the final product <br>
> Assigning member roles based on said modules <br>
> Utilizing external tools to track progress of development (i.e. Motion, etc.) <br>
> Creation of Django project titled "MID Tourism" <br>
> Initial deployment of Heroku app <br>

2. **Assuring functionality of each feature**
> Creating a Django app for each module <br>
> Creating a branch for each module in the Django project <br>
> Implementing the models, views, templates, and forms for each module (ala requirements) <br>
> Making dummy data for testing, and Django tests for coverage <br>
> Ensuring that each app works in its own isolated environment <br>
> Utilizing AJAX principles to implement asynchronous programming into each app when possible <br>

3. **Interconnecting the apps**
> Creating a "homepage" that unites every app into one centralized place for easy access <br>
> Coding new views so the homepage can access every app via hyperlink <br>
> Developing 2 users: Customer and Admin; difference being Customer has no authorization beyond viewing, and Admin has various authorizations <br>
> Merging every app into one branch "Staging"; dealing with any merge errors <br>

4. **UI/UX Design**
> Utilizing external apps to design the design for each app and the homepage (i.e. Figma) <br>

5. **UI/UX Implementation**
> Using CSS frameworks such as Tailwind and Bootstrap to implement the design made in the earlier steps <br>
> Merging again into Staging to deal with potential merging errors and fixing every encounter <br>

6. **Deployment**
> Pushing "Staging" to Main
> Deploy to Heroku
> Quality Assurance

**Executive Boards :**
1. Dylan Pribadi 
2. Halomoan Geraldo
3. Kaloosh Falito Verrell
4. Mohammad Attar
5. Nicholas Lexi
6. Raphael Fide Christiano

## FAQ? :
###### What is MID Tourism?
MID Tourism is a **one stop web app** for those who want to take a break and enjoy travelling, yet struggle with the technicalities of obtaining your daily needs when arriving at your location of leisure. We aim to make your trip the easiest it has ever been, while still maintaining the authenticity of the experience you are seeking. <br>
MID Tourism, apart from servicing its users with ease-of-use and convenience, also offers much to the locale's residents. With opportunities for veritable  yet undeservedly unrecognized businesses such as rental transportation, hotels, restaurants, and tourguides, to exposure for the local landmarks, MID Tourism is headstrong in its mission to create a genuine bond between visitor and visitee. 

###### What are the features available on MID Tourism?
MID Tourism provides you many features: ⤵️

1. **Hotels** :
This the feature where you can overview the best recommended hotels in your designated area.

2. **Resto**
This feature helps you to find the best and the most famous restaurants in your designated area.

3. **Rental Transportation** :
This feature helps you to rent transportations safely in your designated area.

4. **Landmarks** :
This feature shows you the nearest and remarkable landmarks to visit in your designated area.

5. **Tourguide** :
This feature helps you to rent tourguides in your designated area.

6. **About** :
This page will show all the information you need in this app and shows our main motive in creating this app.

## Member Roles
1. Dylan Pribadi :
- About Module

2. Halomoan Geraldo :
- Transportations Module

3. Kaloosh Falito Verrell :
- Restaurants Module

4. Mohammad Attar :
- Landmarks Module

5. Nicholas Lexi :
- Hotel Module

6. Raphael Fide :
- Tourguide Module

## Possible User Roles
1. Admins <br>
Manages creation of all objects in all modules<br>
2. Users <br>
Views the objects and makes reservations <br>
