from demo_bazel_issue.hello_world_printer.protos.same_directory_proto_python_pb.hello_world_printer.protos import (
    same_directory_proto_pb2 as same_directory_proto
)


def instantiate_proto():

    proto_instance = same_directory_proto.SomeMessageUsingImport(
        some_string = "Hello world"
    )

    return proto_instance


if __name__ == "__main__":
    proto_instance = instantiate_proto()
    print(proto_instance.some_string)

    with open("hello_world_via_custom_rule.output", mode="wt") as open_file:
        open_file.write(proto_instance.some_string)
