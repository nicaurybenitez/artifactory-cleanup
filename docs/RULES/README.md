# Reglas Disponibles

## Comunes - Reglas que aplican a todos los repositorios

| Name | Description |
| --- | --- |
| `delete_older_than(days=N)` | Borra artefactos con más de N días de antiguedad. |
| `delete_without_downloads()` | Borra artefactos que no han sido descargados. |
| `delete_older_than_n_days_without_downloads(days=N)` | Borra artefactos con más de N días de antiguedad y no han sido descargados. |
| `repo('reponame')` | La regla aplica específicamente al repositorio `reponame`. |
| `repo_by_mask('*.banned')` | La regla aplica a los repositorios que coincidan con la máscara `*.banned`. |
| `property_eq(property_key, property_value)`| Borra los artefactos del repositorio que contengan específicamente el valor `property_value` en el parámetro `property_key`. |
| `property_neq(property_key, property_value)`| Borra los artefactos del repositorio que NO contengan específicamente el valor `property_value` en el parámetro `property_key`. |

## Docker - Reglas que aplican para las imágenes docker

| Name | Description |
| ---        | --- |
| `delete_docker_images_older_than(days=N)` | Borra las imágenes docker con más de N días de antiguedad. |
| `delete_docker_images_older_than_n_days_without_downloads(days=N)` | Borra las imágenes docker con más de N días de antiguedad y no han sido descargados. |

## Filtros - Reglas con diferentes filtros

| Name | Description | 
| --- | --- |
| `filter_by_path_mask('my/path*')` | Aplica la regla sólo a los artefactos cuya ruta concida con el patrón de ruta especificado. |
| `filter_without_path_mask('master*'), filter_without_path_mask(['release*', 'master*'])` | Aplica la regla sólo a los artefactos cuya ruta NO concida con el patrón especificado. (puede ser list, str) |
| `filter_without_filename_mask('*.nupkg*')` | Aplica la regla sólo a los artefactos cuyo nombre NO concida con el patrón especificado. (puede ser list, str)  |
