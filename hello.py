#!/usr/bin/python
from bcc import BPF

program = """
int hello_world(void *ctx) {
    bpf_trace_printk("Hello World  !\\n");
    return 0;
}
"""

b = BPF(text=program)
syscall = b.get_syscall_fnname("execve")
b.attach_kprobe(event=syscall, fn_name="hello_world")

b.trace_print()

