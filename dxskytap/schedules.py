# Created by wiggins@concentricsky.com on 12/18/15.
from dxskytap.restobject import RestObject, RestMap, RestAttribute, RestBoolAttribute


class Schedule(RestObject):

    uid = RestAttribute('id', readonly=True)
    url = RestAttribute('url', readonly=True)
    title = RestAttribute('title')
    time_zone = RestAttribute('time_zone')
    start_at = RestAttribute('start_at')
    end_at = RestAttribute('end_at')
    delete_at_end = RestBoolAttribute('delete_at_end')
    notify_user = RestBoolAttribute('notify_user')
    executions = RestAttribute('executions', readonly=True)

    def __init__(self, connect, uid, initial_data):
        super(Schedule, self).__init__(connect, "schedules/%s" % (uid,), initial_data)


class Schedules(RestMap):
    def __init__(self, connect):
        super(Schedules, self).__init__(connect, 'schedules',
                                        lambda conn, data: Schedule(conn, data['id'], data))

    def create_schedule(self, title, start_at, time_zone, **kwargs):
        kwargs.update({
            'title': title,
            'time_zone': time_zone,
            'start_at': start_at,
        })
        result = self._connect.post("schedules", body=kwargs)
        return Schedule(self._connect, result['id'], result)
