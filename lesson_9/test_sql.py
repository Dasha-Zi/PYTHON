from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://postgres:123@localhost:5432/QA"
def test_db_connection():
    db = create_engine(db_connection_string)
    names = db.table_names()
    assert names[0] == 'subject'

def test_insert():
    db = create_engine(db_connection_string)
    sql_insert = text("insert into subject (subject_title) values (:new_subject)")
    db.execute(sql_insert, new_subject = 'Informatics')
    
    sql_new_sub = text("select * from subject where subject_title = 'Informatics'")

    result = db.execute(sql_new_sub).all()
    
    assert len(result) == 1, f"Количество предметов не равно 1"

    sql = text("delete  from subject where subject_title = :sb_title")
    db.execute(sql, sb_title = 'Informatics' )
    

def test_update():
    db = create_engine(db_connection_string)
    sql_insert = text("insert into subject (subject_title) values (:new_subject)")
    db.execute(sql_insert, new_subject = 'Informatics')
    
    sql_update = text("update subject set subject_title = :new_titile where subject_title = :old_title")
    
    db.execute(sql_update, new_titile = "Advanced IT", old_title = 'Informatics' )

    sql_check_old = text("select * from subject where subject_title = 'Informatics'")
    res_old = db.execute(sql_check_old).all()
    assert (len(res_old) == 0), f"Ошибка: Предмет со старым названием 'Informatics' всё еще существует!"
    
    sql_delete = text("delete  from subject where subject_title = :sb_title")
    db.execute(sql_delete, sb_title = 'Advanced IT' )

def test_delete():
    db = create_engine(db_connection_string)
    sql_insert = text("insert into subject (subject_title) values (:new_subject)")
    db.execute(sql_insert, new_subject = 'Informatics')

    sql_new_sub = text("select * from subject where subject_title = 'Informatics'")
    result = db.execute(sql_new_sub).all()
        
    assert len(result) == 1, f"Количество предметов не равно 1"

    sql_delete = text("delete  from subject where subject_title = :sb_title")
    db.execute(sql_delete, sb_title = 'Informatics' )
    
    result = db.execute(sql_new_sub).all()
    assert (len(result)== 0), f"Ошибка: Предмет не был удален! В базе найдено записей: {len(result)}"
    