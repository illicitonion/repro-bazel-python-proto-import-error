def _my_custom_rule_impl(ctx):

    output_file = ctx.actions.declare_file(ctx.label.name + ".output")

    runfiles = ctx.runfiles(files = [ctx.executable._hello_world_executable])
    runfiles = runfiles.merge(ctx.attr._hello_world_executable[DefaultInfo].default_runfiles)

    ctx.actions.run(
        arguments = [],
        executable = ctx.executable._hello_world_executable,
        progress_message = "Running Hello world executable",
        outputs = [output_file],
    )

    return DefaultInfo(
        files = depset([output_file]),
        runfiles = runfiles
    )

my_custom_rule = rule(
    attrs = {
        "_hello_world_executable": attr.label(
            cfg = "exec",
            default = "//hello_world_printer/src:hello_world",
            executable = True,
        ),
    },
    implementation = _my_custom_rule_impl,
)
