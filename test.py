import unittest
import requests
import json

# post use cases
valid_user = {"email": "roni@gmail.com", "password": "Rr159753!"}
extra_field = {"email": "ron@gmail.com", "password": "R159753!", "phone": "054-9874563"}
missing_field = {"password": "R159753!"}
existing = {"email": "a@f.com", "password": "Aa123456!"}
existing_diff_pass = {"email": "a@f.com", "password": "Aa23456!"}
# put and delete use cases
valid = {"email": "koni@gmail.com", "password": "Kk159783!", "new_password": "Kk11233!"}
wrong_pass = {"email": "roni@gmail.com", "password": "R159753!", "new_password": "Kk11233!"}
non_existing_user = {"email": "erni@gmail.com", "password": "Rr16753!", "new_password": "Kk11233!"}
missing_email = {"password": "Kk159783!", "new_password": "Kk11233!"}
missing_new_pass = {"email": "roni@gmail.com"}
delete_wrong_pass = {"email": "ron@gmail.com", "password": "R159753!"}

class ApiTest(unittest.TestCase):
    BASE = "http://127.0.0.1:5000/"

    def test_get_all_users(self):
        response = requests.get(ApiTest.BASE, json={})
        self.assertEqual(response.status_code, 200)

    def test_post_new_user(self):
        response = requests.post(ApiTest.BASE, json=valid_user)
        self.assertEqual(response.status_code, 200)

    def test_post_extra_field(self):
        response = requests.post(ApiTest.BASE, json=extra_field)
        self.assertEqual(response.status_code, 200)

    def test_post_missing_field(self):
        response = requests.post(ApiTest.BASE, json=missing_field)
        self.assertEqual(response.status_code, 422)

    def test_post_empty(self):
        response = requests.post(ApiTest.BASE, json={})
        self.assertEqual(response.status_code, 422)

    def test_post_user_exists(self):
        response = requests.post(ApiTest.BASE, json=existing)
        self.assertEqual(response.status_code, 409)

    def test_post_exists_diff_pass(self):
        response = requests.post(ApiTest.BASE, json=existing_diff_pass)
        self.assertEqual(response.status_code, 409)

# --------------------------------Testing PUT---------------------------------------
    def test_put_valid_req(self):
        response = requests.put(ApiTest.BASE, json=valid)
        self.assertEqual(response.status_code, 200)

    def test_put_wrong_pass(self):
        response = requests.put(ApiTest.BASE, json=wrong_pass)
        self.assertEqual(response.status_code, 404)

    def test_put_non_existing_user(self):
        response = requests.put(ApiTest.BASE, json=non_existing_user)
        self.assertEqual(response.status_code, 404)

    def test_put_missing_email(self):
        response = requests.put(ApiTest.BASE, json=missing_email)
        self.assertEqual(response.status_code, 422)

    def test_put_missing_new_pass(self):
        response = requests.put(ApiTest.BASE, json=missing_new_pass)
        self.assertEqual(response.status_code, 422)

    def test_put_empty(self):
        response = requests.put(ApiTest.BASE, json={})
        self.assertEqual(response.status_code, 422)

#-------------------------Testing DELETE--------------------------------------
    def test_delete_valid_req(self):
        response = requests.delete(ApiTest.BASE, json=valid_user)
        self.assertEqual(response.status_code, 200)

    def test_delete_non_existing_user(self):
        response = requests.delete(ApiTest.BASE, json=non_existing_user)
        self.assertEqual(response.status_code, 404)

    def test_delete_missing_email(self):
        response = requests.delete(ApiTest.BASE, json=missing_email)
        self.assertEqual(response.status_code, 422)

    def test_delete_wrong_pass(self):
        response = requests.put(ApiTest.BASE, json=delete_wrong_pass)
        self.assertEqual(response.status_code, 422)

    def test_delete_empty(self):
        response = requests.delete(ApiTest.BASE, json={})
        self.assertEqual(response.status_code, 422)