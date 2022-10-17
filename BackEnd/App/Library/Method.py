from App.Library.Methods.Delete import Delete
from App.Library.Methods.Get import Get
from App.Library.Methods.Others import Others
from App.Library.Methods.Post import Post
from App.Library.Methods.Put import Put


def Method(request, id, model, serializer, modelFieldID=None):
    match request.method:
        case 'GET':
            return Get(id, model, serializer)
        case 'POST':
            return Post(request, id, serializer)
        case 'PUT':
            return Put(request, id, model, serializer, modelFieldID)
        case 'DELETE':
            return Delete(id, model)
        case _:
            return Others(request)