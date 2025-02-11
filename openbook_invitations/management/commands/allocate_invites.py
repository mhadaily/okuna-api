from django.core.management.base import BaseCommand
from django.db import IntegrityError

from django.contrib.auth import get_user_model
from django.db.models import F


class Command(BaseCommand):
    help = 'Allocates invites to users'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, help='Count by which each users invites will be increased')
        parser.add_argument('--total', type=int, help='Total final amount to which each users invites will be set')
        parser.add_argument('--username', type=str, help='Username to allocate invites to')

    def handle(self, *args, **options):
        username = None

        if options['username']:
            username = str(options['username'])

        if options['count']:
            count = int(options['count'])
            self.handle_increase_count(count, username)
        elif options['total']:
            count = int(options['total'])
            self.handle_set_total_count(count, username)

    def handle_increase_count(self, count, username):
        User = get_user_model()
        if username is not None:
            users = User.objects.filter(username=username)
            if not users.exists():
                self.stderr.write('No user found with username %s' % username)
                return
        else:
            users = User.objects.all()

        for user in users:
            try:
                user.invite_count = F('invite_count') + count
                user.save()
            except IntegrityError as e:
                print('IntegrityError %s '.format(e))
                self.stderr.write('Error during allocation for user %s'.format(user.username))

    def handle_set_total_count(self, total_count, username):
        User = get_user_model()
        if username is not None:
            users = User.objects.filter(username=username)
            if not users.exists():
                self.stderr.write('No user found with username %s' % username)
                return
        else:
            users = User.objects.all()

        for user in users:
            try:
                user.invite_count = total_count
                user.save()
            except IntegrityError as e:
                print('IntegrityError %s '.format(e))
                self.stderr.write('Error during allocation for user %s'.format(user.username))
