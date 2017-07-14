
class SavePreUrlMiddleware:
    def process_request(self,request):
        # print '--------middleware--------'
        if request.path not in [
            '/login/',
            '/register/',
            '/register_handle/',
            '/login_handle/',
            '/quit_login/',
            '/islogin/',
            ]:
            request.session['pre_path'] = request.get_full_path()
            print request.session['pre_path']
