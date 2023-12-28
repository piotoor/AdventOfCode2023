from enum import Enum
from collections import OrderedDict
from collections import deque
from math import lcm


def parse_day20_a():
    with open("day20.txt", "r") as f:
        data = list(f.read().splitlines())

    parsed = [
        [],
        {

        },
        {

        }
    ]

    for row in data:
        src, dst = row.split(" -> ")
        dst_list = dst.split(", ")

        if src == "broadcaster":
            parsed[0] += dst_list
        elif src[0] == "%":
            parsed[1][src[1:]] = [dst_list]
        else:
            parsed[2][src[1:]] = [dst_list, []]

    for x in parsed[1]:
        src, dst = x, parsed[1][x][0]
        for y in dst:
            if y in parsed[2]:
                parsed[2][y][1].append(src)

    for x in parsed[2]:
        src, dst = x, parsed[2][x][0]
        for y in dst:
            if y in parsed[2]:
                parsed[2][y][1].append(src)

    # for x in parsed[1]:
    #     print(x, parsed[1][x])
    # print()
    #
    # for x in parsed[2]:
    #     print(x, parsed[2][x])

    return parsed


class Signal(Enum):
    LO = 0
    HI = 1


class Module:
    hi_count = 0
    lo_count = 0

    btn = 1
    modules_h = {
        "vm": set(),
        "kb": set(),
        "dn": set(),
        "vk": set()
    }

    modules_all_h_iter = {
        "vm": -1,
        "kb": -1,
        "dn": -1,
        "vk": -1
    }

    all_data_present = False

    def __init__(self, num_of_dst):
        self.state = Signal.LO
        self.output = False
        self.num_of_dst = num_of_dst

    def get_state(self):
        if self.output:
            return self.state
        else:
            return None


class FlipFlopModule(Module):
    def __init__(self, num_of_dst):
        Module.__init__(self, num_of_dst)
        self.state = Signal.LO

    def process_signal(self, signal, src, tag):
        if signal == Signal.HI:
            self.output = False
            # print(tag + " >>>>>>>> NONE")
        else:
            self.output = True
            if self.state == Signal.LO:
                self.state = Signal.HI
                Module.hi_count += self.num_of_dst
                # print(tag + " >>>>>>>> " + "HI" * self.num_of_dst)
            else:
                self.state = Signal.LO
                Module.lo_count += self.num_of_dst
                # print(tag + " >>>>>>>> " + "LO" * self.num_of_dst)


class ConjunctionModule(Module):
    def __init__(self, connected_modules, num_of_dst):
        Module.__init__(self, num_of_dst)
        self.connected_modules = {}
        for x in connected_modules:
            self.connected_modules[x] = Signal.LO

    def process_signal(self, signal, src, tag):
        # print("conjunction {} connected = {}".format(tag, self.connected_modules))
        self.output = True
        self.connected_modules[src] = signal

        if tag in ["vm", "kb", "dn", "vk"]:
            s = connected_to_string(self.connected_modules)
            Module.modules_h[tag].add(s)
            if all([x == '1' for x in s]):
                Module.modules_all_h_iter[tag] = Module.btn

        if all([Module.modules_all_h_iter[x] != -1 for x in Module.modules_all_h_iter]):
            Module.all_data_present = True

        if all(list(x == Signal.HI for x in self.connected_modules.values())):
            self.state = Signal.LO
            Module.lo_count += self.num_of_dst
            # print(tag + " >>>>>>>> " + "LO" * self.num_of_dst)
        else:
            self.state = Signal.HI
            Module.hi_count += self.num_of_dst
            # print(tag + " >>>>>>>> " + "HI" * self.num_of_dst)


class BroadcastModule(Module):
    def __init__(self):
        Module.__init__(self, 1)
        self.state = Signal.LO

    def process_signal(self, signal):
        self.output = True
        self.state = signal
        if self.state == Signal.HI:
            Module.hi_count += 1
            # print("broadcaster >>>>>>>> HI")
        else:
            Module.lo_count += 1
            # print("broadcaster >>>>>>>> LO")


class Button(Module):
    def __init__(self):
        Module.__init__(self, 1)
        self.state = Signal.LO

    def process_signal(self):
        Module.lo_count += 1
        # print("button >>>>>>>> LO")


def pulses_multiplied(data):
    Module.hi_count = 0
    Module.lo_count = 0
    bc, ff, con = data
    broadcaster = BroadcastModule()
    modules = OrderedDict()
    for k in ff:
        modules[k] = FlipFlopModule(len(ff[k][0]))

    for k in con:
        modules[k] = ConjunctionModule(con[k][1], len(con[k][0]))

    ff_con = {}
    ff_con |= ff
    ff_con |= con

    button = Button()
    for btn in range(0, 1000):
        button.process_signal()
        qq = deque()    # (module, input_signal)
        for x in bc:
            broadcaster.process_signal(Signal.LO)
            qq.append((x, broadcaster.get_state(), "broadcaster"))

        while qq:
            tag, input_signal, src = qq.popleft()
            if tag not in modules or input_signal is None:
                continue
            module = modules[tag]
            module.process_signal(input_signal, src, tag)

            for trgt in ff_con[tag][0]:
                qq.append((trgt, module.get_state(), tag))

    return Module.lo_count * Module.hi_count


def day20_a():
    data = parse_day20_a()
    print("day20a = {}".format(pulses_multiplied(data)))


def stoi(signal):
    return 1 if signal == Signal.HI else 0


def connected_to_string(connected):
    ans = ""

    for x in connected:
        ans += str(stoi(connected[x]))

    return ans


def presses_until_rx(data):
    Module.hi_count = 0
    Module.lo_count = 0
    bc, ff, con = data
    broadcaster = BroadcastModule()
    modules = OrderedDict()
    for k in ff:
        modules[k] = FlipFlopModule(len(ff[k][0]))

    for k in con:
        modules[k] = ConjunctionModule(con[k][1], len(con[k][0]))

    ff_con = {}
    ff_con |= ff
    ff_con |= con

    button = Button()
    low_rx = False

    while not low_rx:
        if Module.all_data_present:
            break
        button.process_signal()
        qq = deque()    # (module, input_signal)
        for x in bc:
            broadcaster.process_signal(Signal.LO)
            qq.append((x, broadcaster.get_state(), "broadcaster"))

        while qq:
            tag, input_signal, src = qq.popleft()
            if input_signal == Signal.LO and tag == "rx":
                low_rx = True
                break
            if tag not in modules or input_signal is None:
                continue
            module = modules[tag]
            module.process_signal(input_signal, src, tag)

            for trgt in ff_con[tag][0]:
                qq.append((trgt, module.get_state(), tag))
        Module.btn += 1

    vals = list(Module.modules_all_h_iter.values())
    return lcm(vals[0], vals[1], vals[2], vals[3])


def day20_b():
    data = parse_day20_a()
    print("day20b = {}".format(presses_until_rx(data)))
