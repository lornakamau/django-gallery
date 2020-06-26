import tempfile
from django.test import TestCase
from .models import Location, Category, Image
from PIL import Image as Picture
from django.test import TestCase
from django.test import override_settings

class LocationTest(TestCase):
    def setUp(self):
        '''
        create new instances before a test
        '''
        self.nairobi = Location(name = "Nairobi")
        self.tokyo = Location(name = "Tokyo")

    def tearDown(self):
        '''
        clear database after each test
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
        creates new instances before a test
        '''
        self.nature = Category(name = "nature")
        self.animals = Category(name = "animals")

    def tearDown(self):
        '''
        clears database after each test
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

def get_temporary_image(temp_file):
        size = (200, 200)
        color = (255, 0, 0, 0)
        image = Picture.new("RGBA", size, color)
        image.save(temp_file, 'png')
        return temp_file

def get_temporary_image2(temp_file2):
        size = (200, 200)
        color = (255, 0, 0, 0)
        image = Picture.new("RGBA", size, color)
        image.save(temp_file2, 'png')
        return temp_file2

class ImageTestClass(TestCase):
    def setUp(self):
        '''
        creates new instances before a test
        '''
        self.nature = Category( name= "nature")
        self.nairobi = Location (name = "Nairobi")
        self.flower = Image(photo = "image.png", name ='maua', description = 'beautiful', category= self.nature, location= self.nairobi)

    def tearDown(self):
        '''
        clears database after each test
        '''
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    def test_image_instance(self):
        '''
        test whether the new image created is an instance of the Image class
        '''
        self.assertTrue(isinstance(self.flower, Image))

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_save_image(self):
        '''
        test whether new image is added to the db 
        '''
        self.nature.save_category()
        self.nairobi.save_location()
        temp_file = tempfile.NamedTemporaryFile()
        test_image = get_temporary_image(temp_file)
        #test_image.seek(0)
        self.test = Image(photo = test_image.name, name ='test', description = 'test image', category= self.nature, location= self.nairobi )
        self.test.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)> 0)

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_display_images(self):
        '''
        test whether we can display images from the db
        '''
        self.nature.save_category()
        self.nairobi.save_location()
        temp_file = tempfile.NamedTemporaryFile()
        test_image = get_temporary_image(temp_file)
        #test_image.seek(0)
        self.test = Image(photo = test_image.name, name ='test', description = 'test image', category= self.nature, location= self.nairobi )
        self.test.save_image()
        images = Image.display_all_images()
        self.assertEqual(len(images), 1)

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_delete_images(self):
        '''
        test whether image is deleted
        '''
        self.nature.save_category()
        self.nairobi.save_location()
        temp_file = tempfile.NamedTemporaryFile()
        test_image = get_temporary_image(temp_file)
        #test_image.seek(0)
        self.test = Image(photo = test_image.name, name ='test', description = 'test image', category= self.nature, location= self.nairobi )
        self.test.save_image()
        images1 = Image.objects.all()
        self.assertEqual(len(images1),1)
        self.test.delete_image()
        images2 = Image.objects.all()
        self.assertEqual(len(images2),0)

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_update_image(self):
        '''
        test whether the image description is updated
        '''
        self.nature.save_category()
        self.nairobi.save_location()
        temp_file = tempfile.NamedTemporaryFile()
        test_image = get_temporary_image(temp_file)
        self.test = Image(photo = test_image.name, name ='test', description = 'test image', category= self.nature, location= self.nairobi )
        self.test.save_image()

        temp_file2 = tempfile.NamedTemporaryFile()
        test_image2 = get_temporary_image2(temp_file2)
        self.test2 = Image(photo = test_image2.name, name ='test', description = 'test image', category= self.nature, location= self.nairobi )
        self.test.update_image(self.test.id, self.test2.photo)
        update = Image.objects.get(name = "test")
        self.assertEqual(update.photo, self.test2.photo)

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_get_image_by_id(self):
        '''
        test whether image is retrieved by id 
        '''
        self.nature.save_category()
        self.nairobi.save_location()
        temp_file = tempfile.NamedTemporaryFile()
        test_image = get_temporary_image(temp_file)
        self.test = Image(photo = test_image.name, name ='test', description = 'test image', category= self.nature, location= self.nairobi )
        self.test.save_image()
        image = Image.get_image_by_id(self.test.id)
        self.assertEqual(image.name, self.test.name)

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_search_image_by_category(self):
        '''
        Tests whether image is retrieved by category
        '''
        self.nature.save_category()
        self.nairobi.save_location()
        temp_file = tempfile.NamedTemporaryFile()
        test_image = get_temporary_image(temp_file)
        self.test = Image(photo = test_image.name, name ='test', description = 'test image', category= self.nature, location= self.nairobi )
        self.test.save_image()
        images = Image.search_image("nature")
        self.assertTrue(len(images) > 0)

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_search_location(self):
        '''
        Tests whether image is retrieved by location
        '''
        self.nature.save_category()
        self.nairobi.save_location()
        temp_file = tempfile.NamedTemporaryFile()
        test_image = get_temporary_image(temp_file)
        self.test = Image(photo = test_image.name, name ='test', description = 'test image', category= self.nature, location= self.nairobi )
        self.test.save_image()
        images = Image.filter_by_location("Nairobi")
        self.assertTrue(len(images) > 0)

    


