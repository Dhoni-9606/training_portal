from django.test import TestCase
from django.urls import reverse
from .models import Course, Trainer, Student

class HomePageTests(TestCase):
    def test_home_page_shows_database_counts(self):
        trainer = Trainer.objects.create(
            first_name='Jane',
            last_name='Doe',
            email='jane@example.com',
            expertise='Python',
        )
        course = Course.objects.create(
            course_name='Python Basics',
            description='Learn Python',
            duration=8,
        )
        course.trainers.add(trainer)
        Student.objects.create(
            first_name='Alex',
            last_name='Smith',
            email='alex@example.com',
            enrolled_courese=course,
            trainer=trainer,
        )

        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Python Basics')
        self.assertEqual(response.context['course_count'], 1)
        self.assertEqual(response.context['trainer_count'], 1)
        self.assertEqual(response.context['student_count'], 1)
