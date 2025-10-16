from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        with transaction.atomic():
            # Clear existing data
            Activity.objects.all().delete()
            Leaderboard.objects.all().delete()
            User.objects.all().delete()
            Team.objects.all().delete()
            Workout.objects.all().delete()

            # Create Teams
            marvel = Team.objects.create(name='Marvel')
            dc = Team.objects.create(name='DC')

            # Create Users
            tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
            steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
            bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
            clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

            # Create Activities
            Activity.objects.create(user=tony, type='Running', duration=30, calories=300)
            Activity.objects.create(user=steve, type='Cycling', duration=45, calories=400)
            Activity.objects.create(user=bruce, type='Swimming', duration=60, calories=500)
            Activity.objects.create(user=clark, type='Yoga', duration=20, calories=100)

            # Create Workouts
            Workout.objects.create(name='Super Strength', description='Heavy lifting and resistance', difficulty='Hard')
            Workout.objects.create(name='Flight Training', description='Aerobic and balance', difficulty='Medium')

            # Create Leaderboard
            Leaderboard.objects.create(team=marvel, points=700)
            Leaderboard.objects.create(team=dc, points=600)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
