# The Beginner's Guide to eBPF

This repo was originally created with the code samples to accompany my talk ["The Beginners Guide to eBPF Programming"](https://youtu.be/lrSExTfS-iQ) given at [eBPF Summit 2020](https://ebpf.io/summit-2020/). Since then I've created several other talks and code samples, and written a book on the topic. If you want to learn about eBPF, I hope you'll find some of these resources useful.

* This repo lists slides, example code, and recordings of talks that I've given that will help you get started with eBPF.
* To read a high-level introduction to the topic, check out my report "What is eBPF". 
* If you want to dive into eBPF programming, "Learning eBPF" might be the book you're looking for. 

"What is eBPF?" and "Learning eBPF" are both available for [download from Isovalent](https://isovalent.com/ebpf/) or with your subscription to [O'Reilly's learning platform](https://www.oreilly.com/library/view/what-is-ebpf/9781492097266/). You can buy "Learning eBPF" from any good bookstore (support your local bookshop by ordering it there!) If you're looking for the example code for "Learning eBPF", you'll find it over in [this repo](https://github.com/lizrice/learning-ebpf).

## Talks, presentations and example code

* The Beginners Guide to eBPF Programming as seen at [eBPF Summit 2020](https://ebpf.io/summit-2020/) 
  * ebpf.py in this repo is the code I write during that talk
  * [slides](https://speakerdeck.com/lizrice/liz-rice-beginners-guide-to-ebpf)
  * [YouTube](https://youtu.be/lrSExTfS-iQ)
  * You'll find more Python code examples in [this gist](https://gist.github.com/lizrice/47ad44a15cce912502f8667a403f5649)

* The Beginners Guide to eBPF Programming in Go 
  * This example using `libbpfgo` library is [here](https://github.com/lizrice/libbpfgo-beginners).
  * [YouTube](https://youtu.be/uBqRv8bDroc) 

* At [eBPF Summit 2021](https://ebpf.io/summit-2021) I wrote an eBPF load balancer from scratch - this is all in C
  * [Load balancer code](https://github.com/lizrice/lb-from-scratch)
  * [YouTube](https://youtu.be/L3_AOFSNKK8)

* For Cloud Native eBPF Day I've written some examples showing some of the ways eBPF programs can get involved with networking 
  * [Slides](https://speakerdeck.com/lizrice/beginners-guide-to-ebpf-programming-for-networking)
  * [Code](https://github.com/lizrice/ebpf-networking)
  * YouTube link coming soon
 
* eBPF Superpowers presentation at DockerCon 
  * [Slides](https://speakerdeck.com/lizrice/ebpf-superpowers)
  * [YouTube](https://youtu.be/4SiWL5tULnQ) 

* Packet counting example added for [O'Reilly Superstream "What's next for Infrastructure and Operations?"](https://learning.oreilly.com/live-events/infrastructure-ops-superstream-series-whats-next-for-infrastructure-and-operations/0636920054193/0636920054192/)
  * Examples: ebpf.py & packet.py 
