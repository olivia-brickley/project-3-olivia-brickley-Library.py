# Author: Olivia Brickley
# GitHub username: olivia-brickley
# Date: 1/25/23
# Description: Library simulator for books, albums, and movies


class LibraryItem:
    """Represents a Library Item's ID, title, location, who it was checked out by, requested by, and date checked out"""
    def __init__(self, library_item_id, title, location, checked_out_by, requested_by, date_checked_out):
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = None

    def get_title(self):
        """Returns an item's title"""
        return self._title

    def get_location(self):
        """Returns an item's location"""
        return self._location

    def set_location(self, location):
        """Sets/updates the item's location"""
        return self._location

    def get_checked_out_by(self):
        """Returns who an item was checked out by"""
        return self._checked_out_by

    def set_checked_out_by(self, patron):
        """Sets/updates who the item was checked out by"""
        return self._checked_out_by

    def get_requested_by(self):
        """Returns who the item was requested by"""
        return self._requested_by

    def get_date_checked_out(self):
        """Returns the date an item was checked out on"""
        return self._date_checked_out

    def set_date_checked_out(self, date):
        """Sets/updates the date an item was checked out on"""
        self._date_checked_out = date

    def set_location_hold(self):
        self._location = "ON_HOLD_SHELF"

    def set_location_on_shelf(self):
        self._location = "ON_SHELF"

    def set_location_checked_out(self):
        self._location = "CHECKED_OUT"


class Book(LibraryItem):
    """Represents a Book with data members inherited from LibraryItem"""
    def __init__(self, library_item_id, title, author):
        """Inherits book's data members from LibraryItem and also adds in and initializes the author"""
        super().__init__(library_item_id, title)
        self._author = author

    def get_author(self):
        """Returns a book's author"""
        return self._author

    def get_check_out_length(self):
        """Returns the max checkout length in days, which is 21 days for a book"""
        return "21 days"


class Album(LibraryItem):
    """Represents an Album with data members inherited from LibraryItem"""
    def __init__(self, library_item_id, title, artist):
        """Inherits album's data members from LibraryItem and also adds in and initializes the artist"""
        super().__init__(library_item_id, title)
        self._artist = artist

    def get_artist(self):
        """Returns album's artist"""
        return self._artist

    def get_check_out_length(self):
        """Returns the max checkout length in days, which is 14 for albums"""
        return "14 days"


class Movie(LibraryItem):
    """Represents a Movie with data members inherited from LibraryItem"""
    def __init__(self, library_item_id, title, director):
        """Inherits movie's data members from LibraryItem and also adds in and initializes the director"""
        super().__init__(self, title)
        self._director = director

    def get_director(self):
        """Returns movie's director"""
        return self._director

    def get_check_out_length(self):
        """Returns the max checkout length in days, which is 7 for movies"""
        return "7 days"


class Patron:
    """Represents a patron's ID, name, items they checked out, and how much the Patron owes the Library in late fees"""
    def __init__(self, patron_id, name, checked_out_items, fine_amount):
        self._parton_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def get_name(self):
        """Returns name of Patron"""
        return self.get_name

    def get_fine_amount(self):
        """Returns the fine amount a Patron owes the Library"""
        return self.get_fine_amount

    def set_fine_amount(self, fine_amount):
        """Sets/updates the fine amount a Patron owes the Library"""
        self._fine_amount = fine_amount

    def add_library_item(self, library_item):
        """Adds the library items a Patron has checked out to a list"""
        self._checked_out_items.append(library_item)

    def remove_library_item(self, library_item):
        """Removes the library items a Patron has checked in from the list"""
        self._checked_out_items.remove(library_item)

    def amend_fine(self, amount):
        """Amends fine with positive argument increasing fine_amount and negative argument decreasing fine_amount"""
        self._fine_amount += amount

    def get_checked_out_items(self):
        return self._checked_out_items


class Library:
    def __init__(self, holdings, members, current_date):
        self._holdings = []
        self._members = []
        self._current_date = 0

    def current_date(self, days):
        self._current_date += days

    def add_library_item(self, library_item):
        self._holdings.append(library_item)

    def add_patron(self, patron):
        self._members.append(patron)

    def lookup_library_item_from_id(self, holdings):
        for library_item in self._holdings:
            if library_item in holdings:
                library_item = LibraryItem()
                return library_item
            else:
                return None

    def lookup_patron_from_id(self, members):
        for patron in self._members:
            if patron in members:
                patron = Patron()
                return patron
            else:
                return None

    def check_out_library_item(self, patron_id, library_item_id):
        if Patron not in self._members:
            return "patron not found"
        if LibraryItem not in self._holdings:
            return "item not found"
        if self._current_date != 0:
            return "item already checked out"
        if LibraryItem.get_requested_by is not None:
            return "item on hold by other patron"
        else:
            checked_out_by = LibraryItem.checked_out_by
            date_checked_out = LibraryItem.date_checked_out
            location = "ON_HOLD_SHELF"
            return checked_out_by, date_checked_out, location

    def return_library_item(self, library_item_id):
        if LibraryItem not in self._holdings:
            return "item not found"
        if LibraryItem.get_checked_out_by is not None:
            return "item already in library"
        update_checked_out_items = Patron.get_checked_out_items[library_item_id.get_item_id()]
        update_item_location = library_item_id.get_item_location()
        update_checked_out_by = library_item_id.get_checked_out_by()
        return "return successful"

    def request_library_item(self, patron_id, library_item_id):
        if Patron not in self._members:
            return "patron not found"
        if LibraryItem not in self._holdings:
            return "item not found"
        if LibraryItem.get_requested_by is not None:
            return "item already on hold"
        update_requested_by = library_item_id.get_requested_by()
        if LibraryItem.set_location_on_shelf():
            update_item_location = LibraryItem.set_location_hold
        return "request successful"


    def pay_fine(self, patron_id, fine_amount):
        if Patron not in self._members:
            return "patron not found"
        else:
            return Patron.amend_fine

    def increment_current_date(self):
        increment_current_date = Library.current_date
        return increment_current_date
