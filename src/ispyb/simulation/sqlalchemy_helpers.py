import sqlalchemy
import ispyb.sqlalchemy

session = sqlalchemy.func.concat(
    ispyb.sqlalchemy.Proposal.proposalCode,
    ispyb.sqlalchemy.Proposal.proposalNumber,
    "-",
    ispyb.sqlalchemy.BLSession.visit_number,
).label("session")

proposal = sqlalchemy.func.concat(
    ispyb.sqlalchemy.Proposal.proposalCode, ispyb.sqlalchemy.Proposal.proposalNumber
).label("proposal")
