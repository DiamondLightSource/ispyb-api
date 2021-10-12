import os
import shutil
import logging
import time
from datetime import datetime, timedelta

import ispyb.sqlalchemy as isa

from ispyb.simulation.base import Simulation
from ispyb.simulation.sqla_helpers import session, proposal


logger = logging.getLogger(__name__)


class SimulateDataCollection(Simulation):
    def _get_container_position(self, ses, blsession, proposalid, beamline):
        shipment_name = "Simulation_Shipment"
        shipment = (
            ses.query(isa.Shipping)
            .filter(isa.Shipping.proposalId == proposalid)
            .filter(isa.Shipping.shippingName == shipment_name)
            .first()
        )

        if not shipment:
            logger.debug("Creating shipment")
            shipment = isa.Shipping(
                shippingName=shipment_name,
                proposalId=proposalid,
                creationDate=datetime.now(),
            )

            ses.add(shipment)
            ses.commit()

        dewar_name = "Simulation_Dewar"
        dewar = (
            ses.query(isa.Dewar.dewarId)
            .filter(isa.Dewar.shippingId == shipment.shippingId)
            .filter(isa.Dewar.code == dewar_name)
            .first()
        )

        if not dewar:
            logger.debug("Creating dewar")
            dewar = isa.Dewar(
                shippingId=shipment.shippingId,
                code=dewar_name,
                dewarStatus="processing",
            )
            ses.add(dewar)
            ses.commit()

        container_name = "Simulation_Container"
        container = (
            ses.query(isa.Container.containerId)
            .filter(isa.Container.dewarId == dewar.dewarId)
            .filter(isa.Container.code == container_name)
            .first()
        )

        if not container:
            logger.debug("Creating container")
            container = isa.Container(
                dewarId=dewar.dewarId,
                code=container_name,
                containerType="Box",
                capacity=25,
                bltimeStamp=datetime.now(),
                containerStatus="at facility",
                # beamlineLocation=beamline,
                # sampleChangerLocation=1,
            )
            ses.add(container)
            ses.commit()

            containerhistory = isa.ContainerHistory(
                containerId=container.containerId,
                status="at facility",
                location=1,
                beamlineName=beamline,
            )

            ses.add(containerhistory)
            ses.commit()

        samples = (
            ses.query(isa.BLSample)
            .filter(isa.BLSample.containerId == container.containerId)
            .all()
        )
        max_loc = 0
        for s in samples:
            if int(s.location) > max_loc:
                max_loc = int(s.location)

        return container.containerId, max_loc + 1

    def run(self, beamline, experiment_type, experiment_no=0, delay=0):
        blses = self.config["sessions"][beamline]

        if experiment_type not in self.config["experiments"]:
            raise KeyError(f"No such experiment type {experiment_type}")

        if experiment_no > len(self.config["experiments"][experiment_type]):
            raise KeyError(
                f"Invalid experiment number {experiment_no}, {len(self.config['experiments'][experiment_type])} exps available"
            )

        exp = self.config["experiments"][experiment_type][experiment_no]
        data = os.path.join(self.config["raw_data"], exp["data"])

        if not os.path.exists(data):
            raise AttributeError(f"Raw data file: {data} does not exist")

        if not exp.get("sample"):
            raise KeyError(
                f"No sample specified for experiment {experiment_type}:{experiment_no}"
            )

        if exp["sample"] not in self.config["samples"]:
            raise KeyError(
                f"Experiment sample {exp['sample']} is not defined in `samples`"
            )

        sample = self.config["samples"][exp["sample"]]

        with self.session() as ses:
            prop, blsession = (
                ses.query(proposal, isa.BLSession)
                .join(isa.Proposal)
                .filter(session == blses)
                .first()
            )

            blsample = (
                ses.query(isa.BLSample)
                .filter(isa.BLSample.name == sample["name"])
                .first()
            )

            if not blsample:
                for k in ["component", "name"]:
                    if not sample.get(k):
                        raise KeyError(f"No {k} specified for sample {exp['sample']}")

                if sample["component"] not in self.config["components"]:
                    raise KeyError(
                        f"Sample component {sample['component']} is not defined in `components`"
                    )

                comp = self.config["components"][sample["component"]]
                for k in ["acronym"]:
                    if not comp.get(k):
                        raise KeyError(
                            f"No {k} specified for component {sample['component']}"
                        )

                component = (
                    ses.query(isa.Protein)
                    .filter(isa.Protein.acronym == comp["acronym"])
                    .first()
                )

                if not component:
                    logger.info(f"Creating component {comp['acronym']}")
                    component = isa.Protein(
                        proposalId=blsession.proposalId,
                        acronym=comp.get("acronym"),
                        name=comp.get("name", comp.get("acronym")),
                        sequence=comp.get("sequence"),
                        density=comp.get("density"),
                        molecularMass=comp.get("molecularMass"),
                        description="Simulated component",
                    )
                    ses.add(component)
                    ses.commit()

                crystal = isa.Crystal(proteinId=component.proteinId)
                ses.add(crystal)
                ses.commit()

                logger.info(f"Creating sample {sample['name']}")
                containerid, position = self._get_container_position(
                    ses, blses, blsession.proposalId, beamline
                )
                blsample = isa.BLSample(
                    name=sample["name"],
                    crystalId=crystal.crystalId,
                    location=position,
                    containerId=containerid,
                )
                ses.add(blsample)
                ses.commit()

            subsampleid = None
            if exp.get("subsample"):
                logger.info("Creating subsample")
                sub = exp["subsample"]

                pos1id = None
                if sub.get("x") and sub.get("y"):
                    pos1 = isa.Position(
                        posX=sub["x"],
                        posY=sub["y"],
                    )
                    ses.add(pos1)
                    ses.commit()

                    pos1id = pos1.positionId

                pos2id = None
                if sub.get("x2") and sub.get("y2"):
                    pos2 = isa.Position(
                        posX=sub["x2"],
                        posY=sub["y2"],
                    )
                    ses.add(pos2)
                    ses.commit()

                    pos2id = pos2.positionId

                subsample = isa.BLSubSample(
                    positionId=pos1id,
                    position2Id=pos2id,
                    type=sub.get("type"),
                    blSampleId=blsample.blSampleId,
                    comments="Simulated sample",
                )
                ses.add(subsample)
                ses.commit()

                subsampleid = subsample.blSubSampleId

            logger.debug("Creating datacollection group")
            dcg = isa.DataCollectionGroup(
                sessionId=blsession.sessionId,
                experimentType=experiment_type,
                blSampleId=blsample.blSampleId,
            )
            ses.add(dcg)
            ses.commit()

            logger.debug("Creating datacollection")
            dc = isa.DataCollection(
                # TODO: Remove - legacy column
                BLSAMPLEID=blsample.blSampleId,
                blSubSampleId=subsampleid,
                dataCollectionGroupId=dcg.dataCollectionGroupId,
                fileTemplate=os.path.basename(exp["data"]),
                imageDirectory=os.path.dirname(exp["data"]),
                imageContainerSubPath=exp.get(
                    "imageContainerSubPath", "1.1/measurement"
                ),
                numberOfImages=exp.get("numberOfImages"),
                wavelength=exp.get("wavelength"),
                exposureTime=exp.get("exposureTime"),
                runStatus="Successful",
                comments="Simulated datacollection",
                startTime=datetime.now(),
                endTime=datetime.now() + timedelta(minutes=5),
            )
            ses.add(dc)
            ses.commit()

            if exp.get("grid"):
                logger.debug("Creating gridinfo")
                grid = isa.GridInfo(
                    dataCollectionId=dc.dataCollectionId,
                    steps_x=exp["grid"]["steps_x"],
                    steps_y=exp["grid"]["steps_y"],
                    snapshot_offsetXPixel=exp["grid"]["snapshot_offsetXPixel"],
                    snapshot_offsetYPixel=exp["grid"]["snapshot_offsetYPixel"],
                    dx_mm=exp["grid"]["dx_mm"],
                    dy_mm=exp["grid"]["dy_mm"],
                    pixelsPerMicronX=exp["grid"]["pixelsPerMicronX"],
                    pixelsPerMicronY=exp["grid"]["pixelsPerMicronY"],
                )
                ses.add(grid)
                ses.commit()

            logger.info(f"Created datacollection: {dc.dataCollectionId}")
            logger.info(
                f"{self.config['ispyb_url']}/visit/{blses}/id/{dc.dataCollectionId}"
            )

            logger.info("Triggering before start plugins")
            self.before_start(dc.dataCollectionId)

            # Create the dataset dir
            data_dir = os.path.join(
                self.config["data_dir"].format(beamline=beamline),
                prop,
                exp["sample"],
                f"{exp['sample']}_{dc.dataCollectionId}",
            )

            dc.imageDirectory = data_dir
            ses.commit()

            if os.path.exists(data_dir):
                logger.warning(f"Data directory already exists: {data_dir}")

            os.makedirs(data_dir)
            if not os.path.exists(data_dir):
                raise AttributeError(
                    f"Could not create output data directory: {data_dir}"
                )

            # Link data files / snapshots
            link = self.config.get("copy_method", "copy") == "link"
            if link:
                logger.debug("Linking data")
                os.link(data, os.path.join(data_dir, os.path.basename(data)))
            else:
                logger.debug("Copying data")
                shutil.copy(data, os.path.join(data_dir, os.path.basename(data)))

            snapshot_path = os.path.join(
                self.config["raw_data"], exp.get("xtalSnapshotFullPath1")
            )
            if snapshot_path:
                if os.path.exists(snapshot_path):
                    snapshot = os.path.join(data_dir, os.path.basename(snapshot_path))
                    if link:
                        logger.debug("Linking snapshot from '%s' to '%s'", snapshot_path, snapshot)
                        os.link(snapshot_path, snapshot)
                    else:
                        logger.debug("Copying snapshot from '%s' to '%s'", snapshot_path, snapshot)
                        shutil.copy(snapshot_path, snapshot)

                    snap, snap_extension = os.path.splitext(snapshot_path)
                    thumb = f"{snap}t{snap_extension}"
                    if os.path.exists(thumb):
                        if link:
                            logger.debug("Linking thumbnail from '%s'", thumb)
                            os.link(
                                thumb,
                                os.path.join(
                                    data_dir,
                                    f"{os.path.basename(snap)}t{snap_extension}",
                                ),
                            )
                        else:
                            logger.debug("Copying thumbnail from '%s'", thumb)
                            shutil.copy(
                                thumb,
                                os.path.join(
                                    data_dir,
                                    f"{os.path.basename(snap)}t{snap_extension}",
                                ),
                            )
                    else:
                        logger.warning(f"Snapshot thumbnail does not exist {thumb}")

                    dc.xtalSnapshotFullPath1 = snapshot
                    ses.commit()
                else:
                    logger.warning(f"Snapshot file does not exist {snapshot_path}")

            logger.info(f"Finshed copying data to: {data_dir}")

            if delay:
                time.sleep(delay)

            logger.info("Triggering after end plugins")
            self.after_end(dc.dataCollectionId)
