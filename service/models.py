from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

def database(name):

	Session = sessionmaker()


	engine = create_engine(f'{name}')

	Session.configure(bind=engine)
	session = Session()
	return session

meta = MetaData()

class Country(Base):
	__tablename__ = 'countries'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	region = relationship('Region')
	wine = relationship('Wine')


class Region(Base):
	__tablename__ = 'regions'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	country = Column(Integer, ForeignKey('countries.id'))
	wine = relationship('Wine')

class Wine(Base):
	__tablename__ = 'wines'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	country_id = Column(Integer, ForeignKey('countries.id'))
	region_id = Column(Integer, ForeignKey('regions.id'))
	year = Column(Integer)

# Base.metadata.create_all(engine)

country = Country(
	name = 'France'
	)

region = Region(
	name = 'Bordeaux Premier Cru - left bank',
	country = 1
	)

wine1 = Wine(
	name = "Mouton Rothschild",
	country_id = 1,
	region_id = 1,
	year = 2016
	)
