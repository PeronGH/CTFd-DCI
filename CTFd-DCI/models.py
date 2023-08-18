from CTFd.models import db
from CTFd.plugins.challenges import Challenges


class DynamicInstances(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    challenge_id = db.Column(db.Integer, db.ForeignKey("challenges.id"))

    # basic info
    project_name = db.Column(db.Text)
    stack_path = db.Column(db.Text)
    env = db.Column(db.JSON)

    # renew logic
    create_at = db.Column(db.DateTime)
    expire_at = db.Column(db.DateTime)
    renew_count = db.Column(db.Integer)

    def __init__(
        self, user_id, challenge_id, name, path, env, create_at, expire_at, renew_count
    ):
        self.user_id = user_id
        self.challenge_id = challenge_id
        self.name = name
        self.path = path
        self.env = env
        self.create_at = create_at
        self.expire_at = expire_at
        self.renew_count = renew_count


class DynamicInstanceChallenges(Challenges):
    __mapper_args__ = {"polymorphic_identity": "dynamic_instance"}
    id = db.Column(
        db.Integer, db.ForeignKey("challenges.id", ondelete="CASCADE"), primary_key=True
    )
    stack_path = db.Column(db.Text)
