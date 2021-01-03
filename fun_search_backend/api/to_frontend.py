from database.models import Member


def get_all_member_info():
    all_member = Member.query.all()
    return all_member
