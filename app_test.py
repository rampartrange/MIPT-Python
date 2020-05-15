import unittest
from application.models import User, is_username_valid, load_user, Post
from application import db


class TestUserModel(unittest.TestCase):

    def test_check_fields(self):
        user = User()
        user.set_username('test')
        user.set_password('test')
        user.bio = 'I am test'

        self.assertEqual(user.username, 'test')
        self.assertNotEqual(user.username, 'test1')
        self.assertTrue(user.check_password('test'))
        self.assertFalse(user.check_password('test1'))
        self.assertEqual(user.bio, 'I am test')
        self.assertNotEqual(user.bio, 'Python sucks')

    def test_user_load(self):
        self.assertEqual(load_user(1).id, 1)
        self.assertNotEqual(load_user(1).id, -1)

    def test_username_validity(self):
        self.assertTrue(is_username_valid('test'))
        self.assertFalse(is_username_valid(load_user(1).username))

    def test_user_representation(self):
        user = load_user(1)
        self.assertEqual(user.__repr__(), f'<User {user.username}>')


class TestPostModel(unittest.TestCase):

    def test_check_fields(self):
        post = Post()
        post.title = 'test'
        post.text = 'text_test'

        self.assertEqual(post.title, 'test')
        self.assertNotEqual(post.title, 'test1')
        self.assertTrue(post.text, 'text_test')
        self.assertNotEqual(post.text, 'Python sucks')


if __name__ == '__main__':
    unittest.main()
