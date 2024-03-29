# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import av_pb2 as proto_dot_av__pb2


class SendBinaryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.sendBinary = channel.stream_stream(
                '/proto.SendBinary/sendBinary',
                request_serializer=proto_dot_av__pb2.input.SerializeToString,
                response_deserializer=proto_dot_av__pb2.output.FromString,
                )


class SendBinaryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def sendBinary(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SendBinaryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'sendBinary': grpc.stream_stream_rpc_method_handler(
                    servicer.sendBinary,
                    request_deserializer=proto_dot_av__pb2.input.FromString,
                    response_serializer=proto_dot_av__pb2.output.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.SendBinary', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SendBinary(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def sendBinary(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/proto.SendBinary/sendBinary',
            proto_dot_av__pb2.input.SerializeToString,
            proto_dot_av__pb2.output.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
