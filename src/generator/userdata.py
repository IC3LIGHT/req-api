from faker import Faker


class UserData:
    def __init__(self):
        self.fake = Faker()
        self.result = {}
        self.create_user()

    def gen_name(self):
        self.result['name'] = self.fake.name()

    def gen_job(self):
        self.result['job'] = self.fake.job()

    def create_user(self):
        self.gen_name()
        self.gen_job()
        return self.result
