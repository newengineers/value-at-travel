import sqlalchemy

Engine = sqlalchemy.create_engine(
    'mysql+pymysql://root:@localhost/travalue',
    pool_recycle = 3600,
    echo=False
)

class Query:

    def __init__(self):
        pass

    def insert_test(self, email_adress, password):

        conn = self.engine.connect()

        query = sqlalchemy.text(
            'insert into travalue.user_info (email_adress, PASSWORD, user_definition_id) '
            'VALUES ("'+email_adress+'", "'+password+'", 1)'
        )
        result = conn.execute(query)

    def get_username_password(self, username, password):
        conn = self.engine.connect()

        query = sqlalchemy.text('SELECT ui.email_adress, ui.password FROM travalue.user_info ui ' 
                'WHERE ui.username = "'+username+'" '
        )



        result = conn.execute(query)

        for username, password in result:
            print("Username: ", username)
            print("password", password)


        return result
query = Query(Engine)
#query.insert_test()
query.get_username_password("Test", "12345")