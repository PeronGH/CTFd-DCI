from CTFd import CTFdFlask
from CTFd.plugins import register_plugin_assets_directory
from CTFd.plugins.challenges import CHALLENGE_CLASSES
from .challenge_type import DynamicInstanceChallenge
from .admin_dci import admin_dci_blueprint


def load(app: CTFdFlask):
    # init db
    app.db.create_all()

    # register assets
    register_plugin_assets_directory(app, base_path="/plugins/CTFd-DCI/assets/")

    # add challenge type
    CHALLENGE_CLASSES["dynamic_instance"] = DynamicInstanceChallenge

    # register admin management pages
    app.register_blueprint(admin_dci_blueprint, url_prefix="/admin/dci")
