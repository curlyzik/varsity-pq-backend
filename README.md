- <a href="#introduction">Introduction<a/>
- <a href="#api">Our API<a/>
- <a href="#contribution">Contribution<a/>
- <a href="#built-with">Built With<a/>
- <a href="#license">License<a/>
- <a href="#author">About author<a/>
- <a href="#support">Support<a/>
 
 ## <p id="introduction">Varsity PQ Backend</p>

This is the Backend Repo to Varsity PQ [Read more here to understand better 📖](https://github.com/curlyzik/varsity-pq-frontend)

 ## <p id="api">🚀 Try out Varsity PQ API on RapidApi Hub</p>
- [Nigeria University Past Questions](https://rapidapi.com/curlyzik/api/nigeria-university-past-questions/): This is the all in one API where students from various universities / higher institutions could get past questions to different courses of their discipline. This API serves over 300+ curated past questions from 160+ universites in Nigeria.

- [Nigeria Universities](https://rapidapi.com/curlyzik/api/nigeria-universites/): Retrieve information about Nigeria universities

 ## <p id="contribution">🛠️ Contributing, Installation Steps</p>

1. Fork and Clone the repository
  - Fork the [repository](https://github.com/curlyzik/varsity-pq-backend) first and then clone it.

2. Change the working directory

```bash
cd varsity-pq-backend
```
3. Create virtual environment

```bash
virtualenv venv
```
 - Switch to virtual env
   - For Linux users ``` source env/bin/activate ```
   - For Windows users ``` env\Source\activate ```
 
4. Install project's requirements

```bash
pip install -r requirements.txt
```
5. Create `.env` file
  - Create `.env` file in <a href="https://github.com/curlyzik/varsity-pq-backend/tree/main/uni_project/settings">uni_project/settings</a> and add your variables.
  - Generate SECRET_KEY from <a href="https://djecrety.ir/">Djecrety</a>

```bash
SECRET_KEY=

EMAIL_HOST=you can use post mark
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=

CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=
```
5. Run the app

```bash
python manage.py runserver --settings=uni_project.settings.development
```
You are all set! Open [localhost:8000](http://localhost:8000/) to see the app.

6. Make commits,push to your repo and open a pull request

 ## <p id="built-with">💻 Built with</p>

- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/): for building API
- [dj-rest-auth](https://django-rest-auth.readthedocs.io/en/latest/introduction.html): for authentication
- [djoser](https://djoser.readthedocs.io/en/latest/introduction.html/): for authentication
- [Postmark](https://postmarkapp.com/): for sending emails
- [Django Cloudinary Storage](https://pypi.org/project/django-cloudinary-storage/): Django Cloudinary Storage is a Django package that facilitates integration with Cloudinary by implementing Django Storage API.
- [django-cleanup](https://pypi.org/project/django-cleanup/) django-cleanup app automatically deletes files for FileField, ImageField and subclasses
- [Heroku](http://heroku.com/): for hosting

 ## <p id="license">🛡️ License</p>

This project is licensed under the MIT License - see the [`LICENSE`](LICENSE) file for details.

 ## <p id="author">👨‍💻 Author</p>

### 👤 Isaac Nzekwe

- Twitter: [@curlyzik](https://twitter.com/curlyzik)
- Github: [@curlyzik](https://github.com/curlyzik)
- LinkedIn: [@nzekwe-isaac](https://www.linkedin.com/in/nzekwe-isaac/)

 ## <p id="support">🙏 Support</p>

This project needs a ⭐️ from you. Please don't forget to leave a star ⭐️

If you found the app helpful, consider supporting me with a coffee.

<a href="https://www.buymeacoffee.com/curlyzik" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
---

<h3 align="center">
Varsity PQ needs a ⭐️ from you
</h3>
