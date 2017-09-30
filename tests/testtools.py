from ispyb.connection import Connection, get_connection_class

def get_connection(dict_cursor=False):
    ConnClass = get_connection_class(Connection.ISPYBMYSQLSP)
    return ConnClass(conf='dev', dict_cursor=dict_cursor, conf_file='../conf/config.cfg')
