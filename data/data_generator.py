from faker import Faker


# Создал генератор тестовых данных
class TestDataGenerator:
    def __init__(self):
        self.faker = Faker()

    def generate_random_email(self):
        return self.faker.email()

    def generate_random_password(self, length):
        return self.faker.password(length=length)

    def generate_random_name(self):
        return self.faker.first_name()

