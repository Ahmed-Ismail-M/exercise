import json
from django.test import TestCase


class IndexTest(TestCase):
    def test1_post(self):
        data = {"exerciseName": "test", "hours": 2, "mins": 3}
        json_data = json.dumps(data)
        response = self.client.post(
            "/", data=json_data, content_type="application/json"
        )
        self.assertEqual(response.content.decode("utf-8"), data['exerciseName'])

    def test2_index(self):
        response = self.client.get("/")
        self.assertEqual(
            response.content,
            b"Please provide user_id(int), exerciseName(string),hours(tinyint),mins(tinyint))",
        )

    def test3_missing_hours(self):
        data = {"exerciseName": "test"}
        json_data = json.dumps(data)
        response = self.client.post(
            "/", data=json_data, content_type="application/json"
        )
        self.assertEqual(
            response.content.decode("utf-8") , "ERROR: NOT NULL constraint failed: vwn_exercise.hours"
        )

    def test4_get_days(self):
        response = self.client.get("/exercises")
        self.assertEqual(
            response.content.decode("utf-8"),
            "todo",
        )
