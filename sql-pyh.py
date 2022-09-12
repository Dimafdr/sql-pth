import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from models import Publisher , Book , Shop , Stock , Sale


Base = declarative_base()

DSN = "postgresql://postgres:17072004@localhost:5432/HomeWork6"
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

def searching_publisher_name():
    quere_join = session.query(Shop).join(Stock).join(Book).join(Publisher)
    quere_publisher_name = input('Введите имя (name) издателя: ')
    quere_result = quere_join.filter(Publisher.publisher_name == quere_publisher_name)
    for result in quere_result.all():
        print(f'Издатель "{query_publisher_name}" найден в магазине "{result.name}" с идентификатором {result.id}')

def searching_publisher_id():
    query_join = session.query(Shop).join(Stock).join(Book).join(Publisher)
    query_publisher_name = input('Введите идентификатор (id) издателя: ')
    query_result = query_join.filter(Publisher.id_publisher == query_publisher_name)
    for result in query_result.all():
        print(
            f'Издатель c id: {query_publisher_name} найден в магазине "{result.name}" '
            f'с идентификатором {result.id}')


if __name__ == "__main__":
    searching_publisher_name()
    searching_publisher_id()

session.close()