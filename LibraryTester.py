# Author: Olivia Brickley
# GitHub username: olivia-brickley
# Date: 1/25/23
# Description: testing


import unittest
from Library import LibraryItem
from Library import Book
from Library import Album
from Library import Movie
from Library import Patron
from Library import Library


class TestLibraryItem(unittest.TestCase):
    def test_1(self):
        """test get_location"""
        item1 = LibraryItem("book", "Chronicles of Narnia", "ON_SHELF", "John Johnson", "None", "1/2/23")
        self.assertEqual(item1.get_title(), "Chronicles of Narnia")


class TestBook(unittest.TestCase):
    def test_2(self):
        """test get_author"""
        item2 = Book("123", "Lord of the Flies", "Golding")
        self.assertEqual(item2.get_author(), "Golding")


class TestAlbum(unittest.TestCase):
    def test_3(self):
        item3 = Album("456", "Fearless", "Swift")
        self.assertNotEqual(item3.get_artist(), "Bieber")


class TestMovie(unittest.TestCase):
    def test_4(self):
        item4 = Movie("789", "The Godfather", "Coppola")
        self.assertNotEqual(item4.get_director(), "Spielberg")


class TestPatron(unittest.TestCase):
    def test_4(self):
        patron1 = Patron("abc", "Norman Allen", "Chronicles of Narnia", "5")
        self.assertIsNot(patron1.get_name(), "Edwin Rufus")


class TestLibrary(unittest.TestCase):
    def test_5(self):
        item2 = Book("123", "Lord of the Flies", "Golding")
        item3 = Album("456", "Fearless", "Swift")
        item4 = Movie("789", "The Godfather", "Coppola")
        lib = Library()
        lib.add_library_item(item2)
        lib.add_library_item(item3)
        lib.add_library_item(item4)
        patron1 = Patron("abc", "Norman Allen", "Chronicles of Narnia", "5")
        patron2 = Patron("def", "Edwin Rufus", "Harry Potter", "2.5")
        lib.add_patron(patron1)
        lib.add_patron(patron2)
        self.assertIn(item2, lib)


if __name__ == "__main__":
    unittest.main(exit=False)
