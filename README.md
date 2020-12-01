# IVY web magazine v0.1
* CSE 416 team project
* ivymagazine.koreasouth.cloudapp.azure.com


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

### Operating System Requirements:
1. Windows10
2. MacOS (Catalina10.15.7)

#### Both Operating Systems can run with the instruction above.

### To report a bug or check for existing bugs:
   + Click on the “Issues” tab on the top left corner of the Github page.
     - A list of existing bugs will be displayed, whose details can be viewed once clicked.
   + To report a new bug, click on the green “New issue” button on the top right corner of the page.
     - The following page will display a form that requires you to fill in the title of bug and comments about the bug.
     - Once all necessary fields are filled in, click on the green “Submit new issue” button on the  bottom right corner of the form.

### Instructions for deploying website:
1. Create VM resource in Microsoft Azure portal
2. ssh into the virtual machine with the IP address provided by Azure
3. Install necessary update and upgrade in the virtual machine
4. run "sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl"
   to install postgres and other necessities to the vm
5. Enter command "sudo -u postgres psql"
6. Configure installed postgresql database to match the needs. Detailed description
   of how PostgreSQL database can be configured is included in the link provided at the end of this instruction
7. Download ivy-magazine folder from github
8. Use command "scp -r /directory/to/where/you/downloaded/ivy-magazine/ vm_username@provided_ip:/home/vm_username" to copy the folder into the vm
9. Use "chmod -R 755 ivy-magazine/" to get full authority over this directory
10. Install virtualenv to work through setup in virtual environment
11. Run "source venv/bin/activate" to enter virtual environment
12. Install django, gunicorn, psycopg2-binary, and pillow 
13. Run python manage.py migrate to migrate data from the project into PostgreSQL database
14. Run python manage.py collectstatic to collect all static files into a directory
15. Run gunicorn --bind 0.0.0.0:8000 ivy-magazine.wsgi to bind gunicorn with port 8000
16. Type in "deactivate" to exit virtual environment
17. Follow steps provided by the youtube link from 20:44 to 24:28 to create and run gunicorn.socket and gunicorn.service files.
18. Follow steps provided by the youtube link below from 25:27 to 28:02 to activate nginx in this project
19. Run "sudo ufw delete allow 8000" and "sudo ufw allow 'Nginx Full'"
20. In the Azure VM Resource you have created, go to "Network" tab and under "Inbound port rules", click "Add inbound security rule"
    and change "destination port ranges" to 80, and give it a name in the "Name" tab. This will only allow network requests over HTTP to access this project.
21. To enable the email policy suitable for azure vm environment, open settings.py file in the ivyMagazine/ivyMagazine directory, comment the "Email Settings" block, and uncomment the "Sendgrid Email Settings" block.
22. Before the emailing ability in this software is enabled, the host must have a sendgrid account with an API key, as well as a Single Sender Identity configured. You may find more about this in www.sendgrid.com



### Step to release a New Version
1. Download the folder from this page
2. Use command "scp -r /directory/to/where/you/downloaded/ivy-magazine/ vm_username@provided_ip:/home/vm_username" to copy the folder into the vm
3. Use "chmod -R 755 ivy-magazine/" to get full authority over this directory
4. Run "source venv/bin/activate" to enter virtual environment
5. Run python manage.py migrate to migrate data from the project into PostgreSQL database
6. Run python manage.py collectstatic to collect all static files into a directory
7. Follow steps 15~20 in "instructions for deploying the website" from above to finalize the deploying steps for the New Version.

### Steps to carry out Unit Tests
1. Travel down to the directory that contains manage.py.
2. Type in "python manage.py test magazines"
3. There will be 12 Unit Test that have been run successfully after the execution.
4. If you are prompted with a message that contains "Ran 12 tests in X.XXXs", the process is complete.