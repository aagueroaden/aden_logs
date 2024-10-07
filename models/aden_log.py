from odoo import api, models, fields
from odoo.exceptions import ValidationError
from ..service.logger import AdenLogger

class AdenLog(models.Model):
    _name = "aden.log"
    _description = "Aden Log"
    _rec_name = "message"
    _order = "create_date desc"


    user_name = fields.Char(
        string='Usuario',
        compute="_extract_user_name",
        help="campo computado",
    )

    model_id = fields.Many2one(
        comodel_name="ir.model",
        string="Modelo",
        required=False,
    )

    description = fields.Text(
        string="Descripcion",
    )

    message = fields.Char(
        string="Mensaje",
        required=True,
    )

    level = fields.Selection(
        selection=[
            ("info", "INFO"),
            ("warning", "ADVERTENCIA"), 
            ("error", "ERROR"),
            ("critical", "CRITICO"),
        ],
        string="Nivel",
    )

    log_uid = fields.Integer('Usuario ID', readonly=True)

    pid = fields.Integer('Id de Registro')

    def create_with_object(self, model_name, res_id, log_uid, message, description, level):
        if not level or level not in ["info", "warning", "error", "critical"]:
            raise ValidationError("Nivel especificado desconocido")
        model_id = self._extract_model_id(model_name=model_name)
        self.create({
            "level": level,
            "message": str(message),
            "description": str(description),
            "log_uid": log_uid,
            "model_id": model_id,
            "pid": res_id,
        })

    def _extract_user_name(self):
        for log in self:
            user = self.env['res.users'].browse(log.log_uid)
            if user.exists():
                log.user_name = "{name} [{uid}]".format(name=user.name, uid=log.log_uid)
            else:
                log.user_name = "[{uid}]".format(uid=log.log_uid)

    def _extract_model_id(self, model_name):
        """
        Busca el modelo utilizando el nombre _name del mismo
        """
        model_id = False
        if model_name:
            model_id = self.env['ir.model'].search([
                ('model', '=', model_name)
            ], limit=1)
        return model_id.id if model_id else False

    @api.model
    def log_post(self, level, message, description= False):
        try:
            self.create({
                "level": level,
                "message": str(message),
                "description": str(description),
            })
            return {"status": "success"}
        except Exception as e:
            # va como ejemplo de uso
            AdenLogger.error(
                model_name=self._name,
                res_id=self.id,
                log_uid=self._uid,
                message="Error al crear mensaje a travez de la api",
                description=str(e),
            )
            return {"status": "error", "message": str(e)}
