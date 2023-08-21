from flask import render_template
from CTFd import CTFdFlask
from CTFd.utils.decorators import admins_only
from CTFd.plugins import register_plugin_assets_directory
from CTFd.plugins.challenges import CHALLENGE_CLASSES
from .challenge_type import DynamicInstanceChallenge


def load(app: CTFdFlask):
    # init db
    app.db.create_all()

    # register assets
    register_plugin_assets_directory(app, base_path="/plugins/CTFd-DCI/assets/")

    # add challenge type
    CHALLENGE_CLASSES["dynamic_instance"] = DynamicInstanceChallenge

    # handle listing instance page
    @app.route("/admin/dci/list")
    @admins_only
    def list_dci_page():
        return render_template("admin/page.html", content="<h1>List Instances</h1>")

    # handle configuration page
    @app.route("/admin/dci/config")
    @admins_only
    def config_dci_page():
        return render_template("admin/page.html", content="<h1>Configuration</h1>")
