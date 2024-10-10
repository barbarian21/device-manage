def jwt_response_payload_handler(token,user,request):
    return {
        'token':token,
        'user':user.username,
        'id':user.id    
    }