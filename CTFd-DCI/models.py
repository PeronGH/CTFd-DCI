from CTFd.models import db


class Instances(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    challenge_id = db.Column(db.Integer, db.ForeignKey("challenges.id"))

    # basic info
    name = db.Column(db.Text)
    path = db.Column(db.Text)
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
