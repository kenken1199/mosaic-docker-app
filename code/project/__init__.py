from flask import Flask

app = Flask(__name__)
app.config.from_object('project.config')

import project.views