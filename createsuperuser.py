from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError
from django.contrib.auth import get_user_model
from django.utils.text import capfirst

class Command(createsuperuser.Command):
    help = 'Create a superuser with a phone number instead of a username'

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument('--phone', type=str, help='Specifies the phone number for the superuser.')

    def handle(self, *args, **options):
        User = get_user_model()
        phone = options.get('phone')
        database = options.get('database')
        
        if not phone:
            raise CommandError('You must provide a phone number via --phone.')

        # Prompt for email and password interactively if not provided
        email = options.get('email')
        if not email:
            email = input('Email: ')

        password = options.get('password')
        if not password:
            password = input('Password: ')

        user_data = {
            'phone': phone,
            'email': email,
            'is_superuser': True,
            'is_staff': True,
        }

        user = User.objects.create_superuser(phone=phone, password=password, email=email)
        user.save(using=database)
        self.stdout.write(self.style.SUCCESS(f'Superuser created successfully with phone: {phone}'))
