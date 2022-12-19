# bazel-python-proto-import-error
Demonstration of import problem when using Bazel to build python binary where the protos being imported reside in 
different directories.

## Details

My `py_binary` cannot run due to an import error. The python code relies on a
protobuf as dependency. That protobuf in turn depends on another protobuf in a subdirectory. It is this pattern which
seems to cause the issue as it only emerges once [sub_dependency_proto.proto](./distinct_directory/protos/sub_dependency/sub_dependency_proto.proto)
is introduced.

The error seems to stem from the generated python code for the protobuf where the import statement does not reflect the
directory structure that Bazel assembles.

Strangely, the python code works fine as a compiled library and test, indicating something strange is going on with 
`py_binary`.

Introducing the flag `build --incompatible_default_to_explicit_init_py` to [.bazelrc](./.bazelrc) solves the problem for
running the binary directory, but if the executable is called via a custom rule then the problem persists:

### Failing Command (custom rule)
* `bazel build //hello_world_printer/src:hello_world_via_custom_rule`

### Successful Commands (library, test, and direct call to binary)
* `bazel run //hello_world_printer/src:hello_world`
* `bazel build //hello_world_printer/src:hello_world_library`
* `bazel test //hello_world_printer/src:hello_world_test`

Any help would be much appreciated :confused:

### Error message

```
File "<REDACTED>/demo_bazel_issue/hello_world_printer/protos/same_directory_proto_python_pb/hello_world_printer/protos/same_directory_proto_pb2.py", line 15, in <module>
from distinct_directory.protos import distinct_directory_proto_pb2 as distinct__directory_dot_protos_dot_distinct__directory__proto__pb2
ImportError: cannot import name 'distinct_directory_proto_pb2' from 'distinct_directory.protos'
```
