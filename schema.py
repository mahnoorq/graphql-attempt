from datetime import date
import typing
import strawberry


@strawberry.type
class Account:
    name: str
    email: str
    dob: date


list_accounts = [
    Account(name="John Doe", email="john.doe@res-group.com", dob=date(2024, 7, 15)),
    Account(name="John2 Doe2", email="john2.doe2@res-group.com", dob=date(2024, 7, 5)),
    Account(name="John3 Doe3", email="john3.doe3@res-group.com", dob=date(2024, 7, 9)),
    Account(name="John4 Doe4", email="john4.doe4@res-group.com", dob=date(2024, 7, 8)),
]


def get_accounts(name: str, sort: str | None):
    if sort:
        list_accounts.sort(key=lambda account: account.__dict__[sort])
        return list_accounts
    if name:
        return [account for account in list_accounts if name in account.name]
    return list_accounts


@strawberry.type
class Query:
    accounts: typing.List[Account] = strawberry.field(resolver=get_accounts)


schema = strawberry.Schema(query=Query)
