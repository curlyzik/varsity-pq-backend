<a href="#introduction">Introduction<a/>

 ## <p id="introduction">Varsity PQ Backend</p>

This is the Backend Repo to Varsity PQ [Read more here to understand better 📖](https://github.com/curlyzik/varsity-pq-frontend)

## 🚀 Try out Varsity PQ API
- [Nigeria University Past Questions](https://rapidapi.com/curlyzik/api/nigeria-university-past-questions/): This is the all in one API where students from various universities / higher institutions could get past questions to different courses of their discipline. This API serves over 300+ curated past questions from 160+ universites in Nigeria.

- [Nigeria Universities](https://rapidapi.com/curlyzik/api/nigeria-universites/): Retrieve information about Nigeria universities

## 🛠️ Contributing, Installation Steps

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
4. Install project's requirements

```bash
pip install -r requirements.txt
```
5. Create `.env` file
Create `.env` file in [uni_project/settings](https://github.com/curlyzik/varsity-pq-backend/tree/main/uni_project/settings) and add your variables.
- Generate SECRET_KEY from [Djecrety](https://djecrety.ir/)

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

6. Push to your repo and open a pull request


## 💻 Built with

- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/): for building API
- [dj-rest-auth](https://django-rest-auth.readthedocs.io/en/latest/introduction.html): for authentication
- [djoser](https://djoser.readthedocs.io/en/latest/introduction.html/): for authentication
- [Postmark](https://postmarkapp.com/): for sending emails
- [Django Cloudinary Storage](https://pypi.org/project/django-cloudinary-storage/): Django Cloudinary Storage is a Django package that facilitates integration with Cloudinary by implementing Django Storage API.
- [django-cleanup](https://pypi.org/project/django-cleanup/) django-cleanup app automatically deletes files for FileField, ImageField and subclasses
- [Heroku](http://heroku.com/): for hosting

## 🛡️ License

This project is licensed under the MIT License - see the [`LICENSE`](LICENSE) file for details.

## 👨‍💻 Author

### 👤 Isaac Nzekwe

- Twitter: [@curlyzik](https://twitter.com/curlyzik)
- Github: [@curlyzik](https://github.com/curlyzik)
- LinkedIn: [@nzekwe-isaac](https://www.linkedin.com/in/nzekwe-isaac/)

## 🙏 Support

This project needs a ⭐️ from you. Please don't forget to leave a star ⭐️

If you found the app helpful, consider supporting me with a coffee.

<a href="https://www.buymeacoffee.com/curlyzik" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
---

<h3 align="center">
Varsity PQ needs a ⭐️ from you
</h3>
