class TodoRouter(object):
    """
    A router to control all database operations on models in the
    mdbapp application.
    """
    def db_for_read(self, model, **hints):

        if model._meta.app_label == 'mdbapp':
            return 'todo'
        return None

    def db_for_write(self, model, **hints):

        if model._meta.app_label == 'mdbapp':
            return 'todo'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label == 'mdbapp':
            return db == 'todo'
        return None
