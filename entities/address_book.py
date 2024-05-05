"""Address book entity."""

from collections import UserDict
from .record import Record

class AddressBook(UserDict):
    """Represents address book with contact records.
    
    Attributes:
        data:
          Dictionary with contact records.  
    """

    def add_record(self, record: Record) -> None:
        """Adds record into address book.
        
        Args:
            record:
                Record type object with name and the list of phones.
        
        Returns:
            None.
        
        Raises:
            TypeError: if argument isn't passed.
            AttributeError: if argument doesn't have name attribute.
        """
        self.data[record.name.value] = record

    def find(self, name: str) -> Record|None:
        """Finds record object from the address book by name.
        
        Args:
            name:
                String with name of the contact by which record must be found.
        
        Returns:
             Record type object with name and the list of phones.
             None type if any record isn't found by the given name.
        
        Raises:
            TypeError: if missing 1 required positional argument.
        """
        return self.data.get(name)
    
    def delete(self, name: str) -> None:
        """Deletes record from address book by name
        
        Args:
            name:
                String with name of the contact by which record must be found.
        
        Returns:
            None.
        
        Raises:
            KeyError: if incorrect argument type or value is passed.
            TypeError: if argument is missed.
        """
        del self.data[name]
