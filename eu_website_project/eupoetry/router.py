class EupoetryRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == "eupoetry":
            return "verses"
        else:
            return None
