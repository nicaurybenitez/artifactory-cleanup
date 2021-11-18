from artifactory_cleanup import rules
from artifactory_cleanup.rules import CleanupPolicy
RULES = [

    CleanupPolicy(
       'Dejar las últimas versiones',
       rules.repo('core-docker-release'),
       rules.include_filename('manifest.json'),
       rules.exclude_docker_images(['*:latest', '*:release*']),
       rules.keep_latest_n_version_images_by_modified(count=1),
    ),
]
