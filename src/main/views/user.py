import  falcon
from ..models import User
 
class UserView:
    
        def on_get(self, req, resp):
            user_data = User.objects.all()
            resp.body = "Success"
            resp.content_type = "text/plain"
            resp.status = falcon.HTTP_200

        def on_post(self, request, resp):
            print dir(request)
            print request.get_param('user_id')
            print request.get_param('name'),
            print request.get_param('book_name'),
            print request.get_param('author_name')

            u = User()
            u.user_id = request.get_param('user_id')
            u.name = request.get_param('name')
            u.book_name = request.get_param('book_name')
            u.author_name = request.get_param('author_name')
            u.save()

            resp.body = "Success"
            resp.content_type = "text/plain"
            resp.status = falcon.HTTP_200
            



         
