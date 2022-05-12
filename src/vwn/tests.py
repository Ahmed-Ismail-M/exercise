import json
from django.test import TestCase

from vwn.models import Exercise


class IndexTest(TestCase):
    def setUp(self) -> None:
        xrsyz = Exercise.objects.create(name='test', hours=24, min=30)
        xrsyz.save()
        xrsyz = Exercise.objects.create(name='test', hours=24, min=30)
        xrsyz.save()

    def test1_post(self):
        data = {"exerciseName": "test", "hours": 2, "mins": 3}
        json_data = json.dumps(data)
        response = self.client.post(
            "/api/v1/exercises", data=json_data, content_type="application/json"
        )
        self.assertEqual(response.content.decode("utf-8"), data["exerciseName"])

    def test2_index(self):
        response = self.client.get("/api/v1/exercises")
        self.assertEqual(
            response.content,
            b"Please provide exerciseName(string),hours(tinyint),mins(tinyint))",
        )

    def test3_missing_hours(self):
        data = {"exerciseName": "test"}
        json_data = json.dumps(data)
        response = self.client.post(
            "/api/v1/exercises", data=json_data, content_type="application/json"
        )
        self.assertEqual(
            response.content.decode("utf-8"),
            "ERROR: int() argument must be a string, a bytes-like object or a number, not 'NoneType'",
        )

    def test4_get_days(self):
        response = self.client.get("/api/v1/exercises/days/months")
        self.assertEqual(
            response.content.decode("utf-8"),
            json.dumps({"total days": 2, "total hrs": 1.0}),
        )
    def test5_get_heighest_month(self):
        response = self.client.get("/api/v1/exercises/month/years")
        self.assertEqual(
            response.content.decode("utf-8"),
            json.dumps({"total days": 2, "total hrs": 1.0}),
        )
