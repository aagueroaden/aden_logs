class AdenLogger:

    @staticmethod
    def info(model_name, res_id, log_uid, env, message, description: str) -> None:
        """
        Loggear info con datos de odoo

        :param: model_name: debe ser el self._name
        :param: res_id: debe ser el self.id
        :param: log_uid: debe ser el self._uid
        :param: env: debe ser el self.env
        :param: message: un mensaje breve
        :param: description: ejemplo json payload
        """
        return __logger_with_object(
            model_name, res_id, log_uid, env, message, description,level="info"
        )

    @staticmethod
    def warning(model_name, res_id, log_uid, env, message, description: str) -> None:
        """
        Loggear warnings con datos de odoo

        :param: model_name: debe ser el self._name
        :param: res_id: debe ser el self.id
        :param: log_uid: debe ser el self._uid
        :param: env: debe ser el self.env
        :param: message: un mensaje breve
        :param: description: ejemplo json payload
        """
        return __logger_with_object(
            model_name, res_id, log_uid, env, message, description, level="warning"
        )

    @staticmethod
    def error(model_name, res_id, log_uid, env, message, description: str) -> None:
        """
        Loggear error con datos de odoo

        :param: model_name: debe ser el self._name
        :param: res_id: debe ser el self.id
        :param: log_uid: debe ser el self._uid
        :param: env: debe ser el self.env
        :param: message: un mensaje breve
        :param: description: ejemplo json payload
        """
        return __logger_with_object(
            model_name, res_id, log_uid, env, message, description, level="error"
        )

    @staticmethod
    def critical(model_name, res_id, log_uid, env, message, description: str) -> None:
        """
        Loggear criticos con datos de odoo

        :param: model_name: debe ser el self._name
        :param: res_id: debe ser el self.id
        :param: log_uid: debe ser el self._uid
        :param: env: debe ser el self.env
        :param: message: un mensaje breve
        :param: description: ejemplo json payload
        """
        return __logger_with_object(
            model_name, res_id, log_uid, env, message, description, level="critical"
        )



def __logger_with_object(
    model_name: str,
    res_id: int,
    log_uid: int,
    env,
    message: str,
    description: str,
    level: str="info"
) -> None:
    """
    No se deberia llamar a este metodo
    """
    env["aden.log"].sudo().create_with_object(
        model_name, res_id, log_uid, message, description, level
    )