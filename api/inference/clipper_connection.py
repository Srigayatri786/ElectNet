from clipper_admin import ClipperConnection, DockerContainerManager

clipper_conn = ClipperConnection(DockerContainerManager())
clipper_conn.connect()
clipper_conn.start_clipper()
