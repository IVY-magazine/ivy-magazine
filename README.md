# IVY web magazine 
* CSE 416 team project


## Team members
Role | Name | Email
---|---|---|
Project Manager | Seonghoon Park | seonghoon.park@stonybrook.edu <br>
Lead Programmer | Hyunsoo Kim  | hyunsoo.kim@stonybrook.edu 
Product Owner | Junghun Park | junghun.park@stonybrook.edu <br>
Designer | Hamin Lim | hamin.lim@stonybrook.edu <br>

### Problem statement

Currently, **I Visualize You (a.k.a IVY)**'s contents are being managed in their blog and Instagram platforms. Users directly access the blog, Instagram, or a hardcopy magazine to see **IVY**’s activities. Each platform has different types of content. Since individual platforms have unique content, users have to visit separate platforms to go through all of IVY’s activities which can be inconvenient. The biggest problem with **IVY**’s current content management system is that it is fractured into various platforms, making it hard for our users to be engaged with the content. <br><br>
The primary users involved in the operation of this web application will be the administrators and visitors. The administrators of the application will have to be an authorized member of **IVY**, responsible for updating and maintaining contents created by **IVY**. The users are those that either make casual visits to the website, or those that visit the web page to view the magazines they purchased. <br><br>
This web application will provide **IVY** four major features. The administrators will be able to upload their new projects into the Portfolio page, accessible to all users. Administrators will be able to track where the users came from through the traffic analysis feature. An administrator can manage user information through the user management feature. Online virtual magazines will be uploaded by the administrators and will only be accessible by authenticated users.


### IVY Magazine Connection

#### Set up
1. In order to set the envionment, users must intall Python: https://www.python.org/downloads/
2. After the installation, user must intall Django: https://docs.djangoproject.com/en/3.1/topics/install/
3. Download the file from the Github page: https://github.com/IVY-magazine/ivy-magazine

#### Connect to the Server:
1. After downloading the file, open the file with IDE and go into **ivyMagazine folder** where **manage.py** file is located.
2. In the terminal type: **python manage.py runserver**
3. Server connects to local address (http://127.0.0.1:8000/)

#### Connect to the Admin Page:
1. http://127.0.0.1:8000/admin
2. Admin User Name: **elizabeth**
3. Admin User Password: **victoria@1006**

#### Connection to the different Pages:
1. Home page: http://127.0.0.1:8000/
2. Blog page: http://127.0.0.1:8000/blog/
3. Portfolio page: http://127.0.0.1:8000/portfolio/
4. Magazine page: http://127.0.0.1:8000/magazine/
5. AboutUs page: http://127.0.0.1:8000/aboutUs/
6. ContactUs page: http://127.0.0.1:8000/contactUs/
7. Info Page: http://127.0.0.1:8000/info/
8. SignIn Page: http://127.0.0.1:8000/signIn/
8. SignUp Page: http://127.0.0.1:8000/signUp/
9. Admin Page: http://127.0.0.1:8000/admin/
10. User Manage: http://127.0.0.1:8000/admin/auth/user/
11. Customer Management & Number of Visits Graph: http://127.0.0.1:8000/admin/magazines/customer/
12. Create Update Delete Magazine: http://127.0.0.1:8000/admin/magazines/magazine/
13. Create Update Delete Portfolio: http://127.0.0.1:8000/admin/magazines/portfolio/
