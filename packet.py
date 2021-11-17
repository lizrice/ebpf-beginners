#!/usr/bin/python
from bcc import BPF
from time import sleep

# Counts number of IP packets received per protocol on the eth0 interface

program = """
#include "packet.h"

BPF_HASH(packets);

int hello_packet(struct xdp_md *ctx) {
    u64 counter = 0;
    u64 key = 0;
    u64 *p;

    key = lookup_protocol(ctx);
    if (key != 0) {
        p = packets.lookup(&key);
        if (p != 0) {
            counter = *p;
        }
        counter++;
        packets.update(&key, &counter);
    }

    return XDP_PASS;
}
"""

b = BPF(text=program)
b.attach_xdp(dev="eth0", fn=b.load_func("hello_packet",
             BPF.XDP))

while True:
    sleep(2)
    s = ""
    for k, v in b["packets"].items():
        s += "Protocol {}: counter {},".format(k.value, v.value)
    print(s)
