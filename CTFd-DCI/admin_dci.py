from flask import Blueprint, render_template
from CTFd.utils.decorators import admins_only

admin_dci_blueprint = Blueprint(
    "admin_dci", __name__, template_folder="templates", static_folder="assets"
)


# handle listing instance page
@admin_dci_blueprint.route("/list")
@admins_only
def list_dci_page():
    return render_template("dci/page.html", content="<h1>List Instances</h1>")


# handle configuration page
@admin_dci_blueprint.route("/config")
@admins_only
def config_dci_page():
    return render_template("dci/page.html", content="<h1>Configuration</h1>")
