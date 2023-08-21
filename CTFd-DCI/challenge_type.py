from flask import Blueprint
from CTFd.plugins.challenges import BaseChallenge
from .models import DynamicInstanceChallenges


class DynamicInstanceChallenge(BaseChallenge):
    id = "dynamic_instance"  # Unique identifier used to register challenges
    name = "dynamic_instance"  # Name of a challenge type
    templates = {  # Templates used for each aspect of challenge editing & viewing
        "create": "/plugins/CTFd-DCI/templates/create.html",
        "update": "/plugins/CTFd-DCI/templates/update.html",
        "view": "/plugins/CTFd-DCI/templates/view.html",
    }
    scripts = {  # Scripts that are loaded when a template is loaded
        "create": "/plugins/CTFd-DCI/assets/create.js",
        "update": "/plugins/CTFd-DCI/assets/update.js",
        "view": "/plugins/CTFd-DCI/assets/view.js",
    }
    # Route at which files are accessible. This must be registered using register_plugin_assets_directory()
    route = "/plugins/CTFd-DCI/assets/"
    # Blueprint used to access the static_folder directory.
    blueprint = Blueprint(
        "dynamic_instance",
        __name__,
        template_folder="templates",
        static_folder="assets",
    )
    challenge_model = DynamicInstanceChallenges
