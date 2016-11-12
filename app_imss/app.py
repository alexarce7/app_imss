import json
import web

render = web.template.render('views/')
urls = ('/app_imss(.*)', 'imss')

class dataRead:
        def dataRead(self,file_name):
            with open(file_name,"r") as file:
                self.data = json.load(file)

class dataImss:

    def __init__(self):
        pass

    def GET(self, datos):
        data = ['Nombre UMF', 'Genero', 'Rango de Edad']
        return render.imss(datos)

        if __name__=='__main__':
            app = web.application(urls, globals())
            web.config.debug = True
            app.run()
