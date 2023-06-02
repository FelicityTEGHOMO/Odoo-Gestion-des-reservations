# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ReservationClient(models.Model):
    _name = 'gestion_reservations.customer'
    _description = 'customer'
    _rec_name = "email"

    id_customer = fields.Char(string="Numéro du client", unique=True)
    last_name = fields.Char(string="Nom du client")
    first_name = fields.Char(string="Prénom du client")
    country = fields.Char(string="Pays du client")
    phone = fields.Char(string="Téléphone du client")
    email = fields.Char(string="Email du client")    
    start_date = fields.Date(string='Date d\'arrivée')
    end_date = fields.Date(string='Date de départ')
    id_room = fields.Many2one('gestion_reservations.room', string='Chambre')
    id_reservation = fields.Many2one('gestion_reservations.reservation', string='Reservation')