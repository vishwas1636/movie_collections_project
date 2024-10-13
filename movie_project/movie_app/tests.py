from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Collections, Movie

class CollectionTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.force_authenticate(user=self.user)
    
    def test_create_collection(self):
        data = {
            "title": "salar",
            "description": "action suspense movie",
            "movies": [
                {
                    "uuid": "57ba56f4-c9ef-4197-9e4f-acf04eae5b4d",
                    "title": "Queerama",
                    "description": "50 years after decriminalisation of homosexuality in the UK, director Daisy Asquith mines the jewels of the BFI archive to take us into the relationships, desires, fears and expressions of gay men and women in the 20th century.",
                    "genres": "thriller"
                }
            ]
        }
        response = self.client.post(reverse('collections-get-or-add'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data['collection_uuid'])

    def test_get_collections(self):
        # First create a collection
        collection = Collections.objects.create(
            user=self.user,
            title="Test Collection",
            description="A test collection"
        )
        Movie.objects.create(
            uuid="57ba56f4-c9ef-4197-9e4f-acf04eae5b4d",
            title="Queerama",
            description="50 years after decriminalisation of homosexuality in the UK, director Daisy Asquith mines the jewels of the BFI archive to take us into the relationships, desires, fears and expressions of gay men and women in the 20th century.",
            genres="thriller",
            collection=collection
        )

        # Retrieve the collection
        response = self.client.get(reverse('collections-get-or-add'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['is_success'])
        self.assertEqual(response.data['data']['collections'][0]['title'], "Test Collection")

    def test_update_collection(self):
        # First create a collection
        collection = Collections.objects.create(
            user=self.user,
            title="Test Collection",
            description="A test collection"
        )
        Movie.objects.create(
            uuid="57ba56f4-c9ef-4197-9e4f-acf04eae5b4d",
            title="Queerama",
            description="50 years after decriminalisation of homosexuality in the UK, director Daisy Asquith mines the jewels of the BFI archive to take us into the relationships, desires, fears and expressions of gay men and women in the 20th century.",
            genres="thriller",
            collection=collection
        )

        # Update the collection
        data = {
            "title": "Updated Collection Title",
            "description": "Updated description of the collection",
            "movies": [
                {
                    "uuid": "57ba56f4-c9ef-4197-9e4f-acf04eae5b4d",
                    "title": "Updated Movie Title",
                    "description": "Updated description of the movie",
                    "genres": "Action, Adventure"
                }
            ]
        }
        response = self.client.put(reverse('collection-detail', kwargs={'uuid': collection.uuid}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Collection Title")

    def test_delete_collection(self):
        # First create a collection
        collection = Collections.objects.create(
            user=self.user,
            title="Test Collection",
            description="A test collection"
        )
        Movie.objects.create(
            uuid="57ba56f4-c9ef-4197-9e4f-acf04eae5b4d",
            title="Queerama",
            description="50 years after decriminalisation of homosexuality in the UK, director Daisy Asquith mines the jewels of the BFI archive to take us into the relationships, desires, fears and expressions of gay men and women in the 20th century.",
            genres="thriller",
            collection=collection
        )

        # Delete the collection
        response = self.client.delete(reverse('collection-detail', kwargs={'uuid': collection.uuid}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
