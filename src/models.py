import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class usuario(Base):
    __tablename__ = 'usuario'
    
    id = Column(Integer, ForeignKey('seguidores.id'))
    nombre = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    clave = Column(String(250), nullable=False)


class seguidores(Base):
    __tablename__ = 'seguidores'
    
    id = Column(Integer, primary_key=True)
    seguidor_id = Column(Integer)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))

class likes(Base):
    __tablename__ = 'likes'
    
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))

class post(Base):
    __tablename__ = 'likes'
    
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    foto= Column(String(250), nullable=False)
    descripcion= Column(String(250), nullable=False)
    fechacreacion=Column(String(250))
    update=Column(String(250))
    foto1= Column(String(250), nullable=False)


class comentarios(Base):
    __tablename__ = 'comentarios'
    
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    contenido= Column(String(250), nullable=False)
    fechacreacion=Column(String(250))
    update=Column(String(250))

    def to_dict(self):
        return {}



    def to_dict(self):
        return {}        

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

