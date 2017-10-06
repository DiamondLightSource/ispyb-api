# from ispyb.factory import get_data_area_object, get_connection_object, DataAreaType
import ispyb.factory
import os

conf_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../conf/config.cfg'))

def get_core():
    conn = ispyb.factory.get_connection_object(conf_file)
    return ispyb.factory.get_data_area_object(ispyb.factory.DataAreaType.CORE, conn)

def get_mxacquisition():
    conn = ispyb.factory.get_connection_object(conf_file)
    return ispyb.factory.get_data_area_object(ispyb.factory.DataAreaType.MXACQUISITION, conn)

def get_emacquisition():
    conn = ispyb.factory.get_connection_object(conf_file)
    return ispyb.factory.get_data_area_object(ispyb.factory.DataAreaType.EMACQUISITION, conn)

def get_mxprocessing():
    conn = ispyb.factory.get_connection_object(conf_file)
    return ispyb.factory.get_data_area_object(ispyb.factory.DataAreaType.MXPROCESSING, conn)

def get_mxscreening():
    conn = ispyb.factory.get_connection_object(conf_file)
    return ispyb.factory.get_data_area_object(ispyb.factory.DataAreaType.MXSCREENING, conn)

def get_shipping():
    conn = ispyb.factory.get_connection_object(conf_file)
    return ispyb.factory.get_data_area_object(ispyb.factory.DataAreaType.SHIPPING, conn)
