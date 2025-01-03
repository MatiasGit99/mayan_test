from django.core import management

from ...platform_templates import PlatformTemplate


class Command(management.BaseCommand):
    help = 'Render a platform configuration template.'

    def add_arguments(self, parser):
        parser.add_argument('name', nargs='?', help='Template name')
        parser.add_argument(
            '--list', action='store_true', dest='list',
            help='Show a list of available templates.',
        )
        parser.add_argument(
            '--context', action='store', default='', dest='context',
            help='Pass a context to the template in the form of a YAML '
            'encoded dictionary.',
        )

    def handle(self, *args, **options):
        if options.get('list'):
            self.stdout.write(msg='\nAvailable platform templates.')
            self.stdout.write(msg='----')

            maximum_name_length = max(
                len(template_class.name) for template_class in PlatformTemplate.get_all()
            )

            space_padding = maximum_name_length + 2

            for template_class in PlatformTemplate.get_all():
                template = template_class()
                self.stdout.write(
                    msg='* {:<{}}{}'.format(
                        template.name, space_padding, template.get_label()
                    )
                )

            self.stdout.write(msg='\n')
        else:
            if not options['name']:
                self.stderr.write(msg='Missing template name.')
                exit(1)

            try:
                template = PlatformTemplate.get(
                    name=options['name']
                )
            except KeyError:
                self.stderr.write(
                    msg='Unknown template "{}".'.format(
                        options['name']
                    )
                )
                exit(1)
            else:
                # Python 2 & 3 way to convert from SafeString to unicode
                self.stdout.write(
                    msg='{}'.format(
                        template().render(
                            context_string=options.get('context')
                        )
                    )
                )
