from flask_app.config.mysqlconnection import connectToMySQL
my_db ="users"

class User:
    def __init__(self, user_data):
        self.id = user_data['id']
        self.user_name = user_data['user_name']
        self.email = user_data['email']
        self.created_at = user_data['created_at']
        self.updated_at = user_data['updated_at']

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (user_name, email) VALUES (%(user_name)s,%(email)s);"
        return connectToMySQL(my_db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"

        user_results = connectToMySQL(my_db).query_db(
            query
        )
        users = []
        for user in user_results:
            users.append(cls(user))
        return users
