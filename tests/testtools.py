# from ispyb.factory import create_data_area, create_connection, DataAreaType
import ispyb.factory
import os

conf_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../conf/config.cfg'))

def get_core():
    conn = ispyb.factory.create_connection(conf_file)
    return ispyb.factory.create_data_area(ispyb.factory.DataAreaType.CORE, conn)

def get_mxacquisition():
    conn = ispyb.factory.create_connection(conf_file)
    return ispyb.factory.create_data_area(ispyb.factory.DataAreaType.MXACQUISITION, conn)

def get_emacquisition():
    conn = ispyb.factory.create_connection(conf_file)
    return ispyb.factory.create_data_area(ispyb.factory.DataAreaType.EMACQUISITION, conn)

def get_mxprocessing():
    conn = ispyb.factory.create_connection(conf_file)
    return ispyb.factory.create_data_area(ispyb.factory.DataAreaType.MXPROCESSING, conn)

def get_mxscreening():
    conn = ispyb.factory.create_connection(conf_file)
    return ispyb.factory.create_data_area(ispyb.factory.DataAreaType.MXSCREENING, conn)

def get_shipping():
    conn = ispyb.factory.create_connection(conf_file)
    return ispyb.factory.create_data_area(ispyb.factory.DataAreaType.SHIPPING, conn)
