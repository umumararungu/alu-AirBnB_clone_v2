class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Instantiation of DBStorage class"""
        MySQL_user = getenv("HBNB_MYSQL_USER")
        MySQL_pwd = getenv("HBNB_MYSQL_PWD")
        MySQL_host = getenv("HBNB_MYSQL_HOST")
        MySQL_db = getenv("HBNB_MYSQL_DB")
        MySQL_env = getenv("HBNB_ENV")
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                MySQL_user, MySQL_pwd, MySQL_host, MySQL_db
            ),
            pool_pre_ping=True,
        )
        Base.metadata.create_all(self.__engine)
        if MySQL_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Show all class objects in DBStorage or specified class if given"""
        if cls:
            objects = self.__session.query(cls).all()
        else:
            classes = [State, City, User, Place, Review, Amenity]
            objects = []
            for c in classes:
                objects += self.__session.query(c)
        my_dict = {}
        for obj in objects:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            my_dict[key] = obj
        return my_dict
