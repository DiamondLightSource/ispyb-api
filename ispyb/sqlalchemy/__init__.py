from sqlalchemy.orm import relationship

from ._auto_db_schema import *  # noqa F403
from ._auto_db_schema import AutoProcProgram, AutoProcScaling


AutoProcProgram.AutoProcProgramAttachments = relationship("AutoProcProgramAttachment")
AutoProcScaling.AutoProcScalingStatistics = relationship("AutoProcScalingStatistics")
