from django.test import TestCase
from .models import Cheese, CheeseType, Review, Resource
from .views import index, gettypes, getcheese, cheesedetails
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import ResourceForm, CheeseForm

# Create your tests here.

class CheeseTypeTest(TestCase):
    def test_string(self):
        chtype=CheeseType(typename="soft")
        self.assertEqual(str(chtype), chtype.typename)

    def test_table(self):
        self.assertEqual(str(CheeseType._meta.db_table), 'cheesetype')    

class CheeseTest(TestCase):  
    def test_string(self):
        cheese=Cheese(cheesename="Manchego")
        self.assertEqual(str(cheese), cheese.cheesename) 

    def test_table(self):
        self.assertEqual(str(Cheese._meta.db_table), 'cheese')
 
class ResourceTest(TestCase):
    def test_string(self):
        source=Resource(resourcename="Great Cheeses")
        self.assertEqual(str(source), source.resourcename)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class IndexTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200)
  
class GetTypesTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('types'))
       self.assertEqual(response.status_code, 200)

class GetCheeseTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('cheese'))
       self.assertEqual(response.status_code, 200) 
 
 #Form tests
class ResourceFormTest(TestCase):
    def setUp(self):
        self.user=User.objects.create(username='user1', password='P@ssw0rd1')
    
    def test_resourceform(self):
        info={
            'resourcename':"cheese",
            'resourcetype': "web",
            'userid': self.user,
            'description': "cool stuff"
        }   
        form=ResourceForm(data=info)
        self.assertTrue(form.is_valid)

class CheeseFormTest(TestCase):
    def setUp(self):
        self.user=User.objects.create(username='user1', password='P@ssw0rd1')
        self.type=CheeseType.objects.create(typename='soft')
    
    def test_cheeseform(self):
        info={
            'cheesename':"cheese",
            'cheesetype': self.type,
            'userid': self.user,
            'cheesedesc': "cool stuff",
            'cheeseprice':12.95
        }   
        form=CheeseForm(data=info)
        self.assertTrue(form.is_valid)

#test authentication
class New_Resource_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.resource = Resource.objects.create(
            resourcename= "cheese", 
            resourcetype= "web",
            userid= self.test_user,
            description= "cool stuff")

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newresource'))
        self.assertRedirects(response, '/accounts/login/?next=/cheeseapp/newResource/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newresource'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cheeseapp/newresource.html')
