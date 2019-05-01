# Quilt POS

This is a toy project to experient with/learn about flask, sqlalchemy, and associated libraries.

It is meant to mimic the functionality of a point-of-sale system that might be used at a quilt shop.

The app is based on Miguel Grinberg's excellent <a href="https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world">Flask tutorial</a>.

<p>
In order to get Docker working I had to do the following:<br>
# add this line to Dockerfile after the creation of the venv:<br>
RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev

still fails:<br>
Collecting cloud-init>=0.7.9 (from -r requirements.txt (line 10))<br>
  Could not find a version that satisfies the requirement cloud-init>=0.7.9 (from -r requirements.txt (line 10)) (from versions: )<br>
No matching distribution found for cloud-init>=0.7.9 (from -r requirements.txt (line 10))<br>