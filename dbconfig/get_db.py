import dataset
import json
import os
script_dir = os.path.dirname(os.path.abspath(__file__))




class Configurator:
    def __init__(self, dbname, script_dir=script_dir):
        self.jsonpath = str(script_dir) + '/config.json' 
        self.dbname = dbname

        with open(self.jsonpath) as config:
            self.CONFIG = json.load(config)
            self.dbms = self.CONFIG['dbms']
            self.user = self.CONFIG['user']
            self.module = self.CONFIG['module']
            self.password = self.CONFIG['password']
            self.host = self.CONFIG['host']
            self.port = self.CONFIG['port']
            if self.dbname != '':
                self.dbname = '/' + self.dbname
            self.url ='{dbms}+{module}://{user}:{password}@{host}:{port}{dbname}'.format(dbms=self.dbms,module=self.module, user=self.user, password=self.password, host=self.host, port=self.port, dbname=self.dbname)
    
    
    
    def get_db(self):
        return dataset.connect(self.url)

    def get_engine(self):
        db = self.get_db()
        return db.engine
