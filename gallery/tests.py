from django.test import TestCase
from .models import Location, Category, Image

class LocationTest(TestCase):
    def setUp(self):
        '''
        Create new instances before a test
        '''
        self.nairobi = Location(name = "Nairobi")
        self.tokyo = Location(name = "Tokyo")

    def tearDown(self):
        '''
        Clear database after each test
        '''
        Location.objects.all().delete()

    def test_location_instance(self):
        '''
        test whether the new location created is an instance of the Location class
        '''
        self.assertTrue(isinstance(self.nairobi, Location))
    
    def test_save_location(self):
        '''
        test whether new locations are added to the db 
        '''
        self.nairobi.save_location()
        self.tokyo.save_location()
        locations = Location.objects.all()
        self.assertEqual(len(locations),2)

    def test_delete_location(self):
        '''
        test whether a location is deleted
        '''
        self.nairobi.save_location()
        locations1= Location.objects.all()
        self.assertEqual(len(locations1),1)
        self.nairobi.delete_location()
        locations2= Location.objects.all()
        self.assertEqual(len(locations2),0)

    def test_update_location(self):
        '''
        test whether the location name is updated
        '''
        self.nairobi.save_location()
        self.nairobi.update_location(self.nairobi.id,'Helsinki')
        update = Location.objects.get(name = "Helsinki")
        self.assertEqual(update.name, 'Helsinki')

    def test_display_locations(self):
        '''
        This tests whether the display location function is getting the locations from the db
        '''
        self.nairobi.save_location()
        self.tokyo.save_location()
        self.assertEqual(len(Location.display_all_locations()), 2)
    
class CategoryTest(TestCase):
    def setUp(self):
        '''
        Creates new instances before a test
        '''
        self.nature = Category(name = "nature")
        self.animals = Category(name = "animals")

    def tearDown(self):
        '''
        Clears database after each test
        '''
        Category.objects.all().delete()

    def test_category_instance(self):
        '''
        test whether the new locations are an instance of the Location class
        '''
        self.assertTrue(isinstance(self.nature, Category))
        self.assertTrue(isinstance(self.animals, Category))

    def test_save_category_method(self):
        '''
        test whether new locations are added to the db 
        '''
        self.nature.save_category()
        self.animals.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 2)

    def test_delete_category(self):
        '''
        tests whether category is deleted
        '''
        self.nature.save_category()
        self.animals.save_category()
        categories1 = Category.objects.all()
        self.assertEqual(len(categories1),2)
        self.nature.delete_category()
        categories2 = Category.objects.all()
        self.assertEqual(len(categories2),1)

    def test_update_category(self):
        '''
        tests whether the category name is updated
        '''
        self.nature.save_category()
        self.nature.update_category(self.nature.id,'travel')
        update = Category.objects.get(name = "travel")
        self.assertEqual(update.name, 'travel')