from artifactory_cleanup import rules
from artifactory_cleanup.rules import CleanupPolicy
RULES = [

    CleanupPolicy(
       'Borrar archivos con más de 30 días',
       rules.repo('core-docker-release'),
       #rules.include_docker_images(['hello-world:*','king_ssh:*']),
       rules.include_filename('manifest.json'),
       rules.exclude_docker_images('*:latest'),
       rules.keep_latest_n_version_images_by_property(count=3,custom_regexp=r'(^\d*\.\d*\.\d*$)',number_of_digits_in_version=0),
    ),
]
