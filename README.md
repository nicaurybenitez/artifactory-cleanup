# Artifactory Cleanup #

`artifactory-cleanup` es una herramienta la limpieza de artefactos en "Jfrog Artifactory".

# Tables of Contents

<!-- toc -->

- [Instalación](#instalación)
- [Uso](#uso)
  * [Comandos](#comandos)
  * [Reglas Disponibles](#reglas-disponibles)
  * [Políticas de Limpieza de Artefactos](#políticas-de-limpieza-de-artefactos)
  
<!-- tocstop -->

# Instalación
Actualiza/instala la versión más reciente disponible:
```bash
# Directamente desde git
python3 -mpip install git+https://github.com//nicaurybenitez/artifactory-cleanup.git

# Si quieres modificar algún archivo
git clone https://github.com//nicaurybenitez/artifactory-cleanup.git
cd artifactory-cleanup
python3 -mpip install -e .
```

# Uso

Suponiendo que deseas remover todos los artefactos con "n" días de antiguedad.
Puedes seguir los siguientes pasos:

1. Instala `artifactory-cleanup`
2. Сrea un archivo python, por ejemplo, `reponame.py` con el siguiente contenido:
```python
from artifactory_cleanup import rules
from artifactory_cleanup.rules import CleanupPolicy

RULES = [

    # ------ BORRAR ARCHIVOS CON 30 DIAS DE ANTIGUEDAD EN EL REPOSITORIO 'reponame' --------
    CleanupPolicy(
       'Borrar archivos con más de 30 días',
        rules.repo('reponame'),
        rules.delete_older_than(days=30),
    ),
]
```
3. Ejecuta el siguiente comando para MOSTRAR los artefactos que serían borrados por la regla:
```bash
artifactory-cleanup --user user --password password --artifactory-server https://repo.example.com/artifactory --config reponame.py
```
4. Agrega `--destroy` para REMOVER los artefactos
```bash
artifactory-cleanup --destroy --user user --password password --artifactory-server https://repo.example.com/artifactory --config reponame.py
```

## Comandos ##

```bash
# Debug
# Ejecución en modo "debug" - sólo imprime los artefactos encontrados. No los borra
artifactory-cleanup --user user --password password --artifactory-server https://repo.example.com/artifactory --config reponame.py

# Borrar Directorio Vacío
# --remove-empty-folder
# Necesitas usar el plugin https://github.com/jfrog/artifactory-user-plugins/tree/master/cleanup/deleteEmptyDirs para borrar directorios vacíos
artifactory-cleanup --remove-empty-folder --user user --password password --artifactory-server https://repo.example.com/artifactory

# Ejecución en modo "debug" solo para la regla `ruletestname`.
# Ejecución en modo "debug" - sólo imprime los artefactos encontrados. No los borra
artifactory-cleanup --rule-name ruletestname --user user --password password --artifactory-server https://repo.example.com/artifactory --config reponame.py

# REMOVER
# Para eliminar artefactos utiliza `--destroy`
artifactory-cleanup --destroy --user user --password password --artifactory-server https://repo.example.com/artifactory  --config reponame.py
```

## Reglas Disponibles ##

Todas las reglas son importadas del módulo `rules`.
Revisa también [Lista de Reglas Disponibles](docs/RULES)

## Políticas de Limpieza de Artefactos ##

Para agregar una política de limpieza necesitas:

- Сrea un archivo python, por ejemplo, `reponame.py`. `artifacroty-cleanup` importará la variable `RULES`.
- Agrega una regla de la [Lista de Reglas Disponibles](docs/RULES).

```python
from artifactory_cleanup import rules
from artifactory_cleanup.rules import CleanupPolicy

RULES = [

    CleanupPolicy(
       'Borra todos los repositorios `* .tmp` con más de 7 días de antiguedad',
        rules.repo_by_mask('*. tmp'),
        rules.delete_older_than(days = 7),
    ),
    CleanupPolicy(
        'Borra todas las imágenes docker con más de 30 días de antiguedad de `docker-registry` excluyendo `latest` y `release`',
        rules.repo('docker-registry'),
        rules.exclude_docker_images(['*:latest', '*:release*']),
        rules.delete_docker_images_not_used(days=30),
    ),
]
```
