from flask_restful import Resource, abort, request


class RESTResource(Resource):
    def get(self, resource_id=None):
        if resource_id:
            resource = self.model.find(resource_id)
            if resource:
                return resource.serialize()
            return abort(404)
        return self.model.order_by('created_at', 'desc').get().serialize()

    def post(self):
        data = request.get_json()
        resource = self.model.create(data)
        return resource.serialize()

    def put(self, resource_id):
        if not resource_id:
            return abort(404)
        resource = self.model.find(resource_id)
        data = request.get_json()
        resource.update(data)
        return resource.serialize()

    def delete(self, resource_id):
        if not resource_id:
            return abort(404)
        resource = self.model.find(resource_id)
        resource.delete()
        return resource.serialize()
