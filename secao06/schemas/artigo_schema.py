from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from secao06.core.settings import settings

class ArtigoModel(settings.DBBasemodel):
    pass