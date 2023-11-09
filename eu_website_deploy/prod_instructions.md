.env
- there is no .env file in github, as it contains secrets, so it should be placed in the root manually

db directory
- folder for db_volume
- contains verses.sqlite3 file, which is will be synchronized (copied and replaced) with the file of the same name in django_gunicorn docker containers 
- be careful with verses.sqlite3 file. If you clone it from github repository, you will lose all data, added from the site's admin panel
- actually it makes sense to git push verses.sqlite3 file to git repository or copy to local PC

nginx_prod directory
- contains nginx.config for production
- the only dif with dev is server_name eupoetry.kyiv.ua instead of eupoetry.kyiv.ua.local;


How to clone one folder from git repository
git clone -n --depth=1 --filter=tree:0 https://github.com/EugenefedorovPro/eu_poetry_website.git
cd eu_poetry_website/
git sparse-checkout set --no-cone eu_website_deploy
git checkout
