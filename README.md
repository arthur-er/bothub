<h1 align="center">Bothub</h1>
<p align="center"><strong>A interface for using multiple chatterbot bots</strong>
</p><div align="center">Built for studying purposes in 2018</div>
<br/>

<h2>Goal and requirements</h2>

- Allow users to register and login
- Allow users to create and interact with chatbots

<h2>Key learnings</h2>

- Using flask to build a monolith application
- Using SQLAlchemy to interact with a database
- Using Chatterbot to build simple chatbots
- Dockerizing applications for deploy
- Deploying applications to heroku

<h2>How to run</h2>

1. Clone this project
2. Run `docker build -t bothub` to build the docker image
3. Run `docker run -p 5000:5000 bothub`
