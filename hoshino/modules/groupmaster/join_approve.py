import hoshino
from nonetrip import RequestSession, on_request


@on_request('group.add')
async def join_approve(session: RequestSession):
    cfg = hoshino.config.groupmaster.join_approve
    gid = session.event.group_id
    if gid not in cfg:
        return
    for k in cfg[gid].get('keywords', []):
        if k in session.event.comment:
            await session.approve()
            return
    if cfg[gid].get('reject_when_not_match', False):
        await session.reject()
        return
