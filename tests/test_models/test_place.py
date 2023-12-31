#!/usr/bin/python3
import unittest
from models.place import Place
from datetime import datetime
from time import sleep
"""Unit tests for class Place"""


class TestUser(unittest.TestCase):
    """ Unit tests for class Place """

    def test_instantiate(self):
        """pass instantiation """
        self.assertEqual(Place, type(Place()))

    def test_id(self):
        """ Happy pass public id string format """
        self.assertEqual(str, type(Place().id))

    def test_created_at(self):
        """pass created at datetime """
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at(self):
        """ pass updated at datetime """
        self.assertEqual(datetime, type(Place().updated_at))

    def test_uid(self):
        """ UID created at each instantiation """
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_city_id(self):
        """pass city_id correctly"""
        place1 = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertTrue(hasattr(place1, "city_id"))

    def test_user_id(self):
        """pass user_id correctly """
        place1 = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertTrue(hasattr(place1, "user_id"))

    def test_name(self):
        """pass name correctly"""
        place1 = Place()
        self.assertEqual(str, type(Place.name))
        self.assertTrue(hasattr(place1, "name"))

    def test_description(self):
        """pass description correctly """
        place1 = Place()
        self.assertEqual(str, type(Place.description))
        self.assertTrue(hasattr(place1, "description"))

    def test_number_rooms(self):
        """pass rooms correctly """
        place1 = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertTrue(hasattr(place1, "number_rooms"))

    def test_number_bathrooms(self):
        """pass bathrooms correctly"""
        place1 = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertTrue(hasattr(place1, "number_bathrooms"))

    def test_max_guest(self):
        """pass max guest correctly """
        place1 = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertTrue(hasattr(place1, "max_guest"))

    def test_price_by_night(self):
        """pass price by night correctly """
        place1 = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertTrue(hasattr(place1, "price_by_night"))

    def test_latitidue(self):
        """pass latitude correctly """
        place1 = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertTrue(hasattr(place1, "latitude"))

    def test_longitude(self):
        """pass longitude correctly """
        place1 = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertTrue(hasattr(place1, "longitude"))

    def test_amenity_ids(self):
        """pass amenity id correctly """
        place1 = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertTrue(hasattr(place1, "amenity_ids"))

    """def test_instantiate_kwargs(self):
        '''Single instantiate with kwargs'''
        dt = datetime.today()
        place1 = Place(
            id="123", created_at=dt.isoformat(), updated_at=dt.isoformat()
        )
        self.assertEqual(place1.id, "123")
        self.assertEqual(place1.created_at, dt)
        self.assertEqual(place1.updated_at, dt)"""

    def test_str_rep(self):
        """pass str representation correctly """
        place1 = Place()
        str_rep = "[{}] ({}) {}".format(
            place1.__class__.__name__,
            place1.id,
            place1.__dict__
            )
        self.assertEqual(str_rep, str(place1))

    def test_save(self):
        """ save method """
        place1 = Place()
        sleep(2)
        update = place1.updated_at
        place1.save()
        self.assertNotEqual(update, place1.updated_at)

    def test_to_dict(self):
        """pass to_dict method correctly"""
        place1 = Place()
        self.assertTrue(dict, type(place1.to_dict))

    def test_to_dict_add_attr(self):
        """ add attribute to dict """
        place1 = Place()
        place1.city = "The"
        place1.state = "Angeles"
        self.assertIn("city", place1.to_dict())
        self.assertIn("state", place1.to_dict())

    def test_to_dict_wrong_arg(self):
        """ add an undefined arg """
        place1 = Place()
        with self.assertRaises(NameError):
            place1.to_dict(hello)


if __name__ == "__main__":
    unittest.main()
