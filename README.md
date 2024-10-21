# aden_logs
Repo odoo para Aden


### Uso

1. Importar el servicio `AdenLogger` donde se quiera usar

2. El servicio puede loggear 4 tipos CRITICOS, ADVERTENCIA, ERRORES E INFO

3. Para loggear se nescesita pasar:

    #### Parametros

    1. Nombre modelo -> self._name

    2. Id usuario que esta creando el error ->  ej: self._uid

    3. env, si bien es mucho, es nescesario para ejecutar metodos -> self.env

    3. Un breve mensaje que se quiere hacer, es obligatorio

    4. Puede ser un payload o un error de python mas extenso, no es obligatorio


