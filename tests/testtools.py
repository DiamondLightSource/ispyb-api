from ispyb.factory import get_data_area_object, ConnectionType, DataAreaType
import os

conf_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../conf/config.cfg'))

def get_core():
    core = get_data_area_object(DataAreaType.CORE, ConnectionType.ISPYBMYSQLSP)
    core.get_connection().connect('dev', conf_file)
    return core

def get_mxacquisition():
    mxacquisition = get_data_area_object(DataAreaType.MXACQUISITION, ConnectionType.ISPYBMYSQLSP)
    mxacquisition.get_connection().connect('dev', conf_file)
    return mxacquisition

def get_emacquisition():
    emacquisition = get_data_area_object(DataAreaType.EMACQUISITION, ConnectionType.ISPYBMYSQLSP)
    emacquisition.get_connection().connect('dev', conf_file)
    return emacquisition

def get_mxprocessing():
    mxprocessing = get_data_area_object(DataAreaType.MXPROCESSING, ConnectionType.ISPYBMYSQLSP)
    mxprocessing.get_connection().connect('dev', conf_file)
    return mxprocessing

def get_mxscreening():
    mxscreening = get_data_area_object(DataAreaType.MXSCREENING, ConnectionType.ISPYBMYSQLSP)
    mxscreening.get_connection().connect('dev', conf_file)
    return mxscreening

def get_shipping():
    shipping = get_data_area_object(DataAreaType.SHIPPING, ConnectionType.ISPYBMYSQLSP)
    shipping.get_connection().connect('dev', conf_file)
    return shipping
