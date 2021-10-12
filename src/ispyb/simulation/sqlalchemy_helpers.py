from sqlalchemy import func
import ispyb.sqlalchemy as isa

session = func.concat(
    isa.Proposal.proposalCode,
    isa.Proposal.proposalNumber,
    "-",
    isa.BLSession.visit_number,
).label("session")

proposal = func.concat(isa.Proposal.proposalCode, isa.Proposal.proposalNumber).label(
    "proposal"
)
